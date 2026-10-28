"""Génère le tracé SVG de la France métropolitaine et de la Belgique (world-atlas 50m)."""
import json, math, sys

LAT0 = 46.5
K = math.cos(math.radians(LAT0))
# Cadre : longitude -5.5 à 9.8, latitude 41.2 à 51.6
LON_MIN, LON_MAX, LAT_MIN, LAT_MAX = -5.5, 9.8, 41.2, 51.6
W = 600
SCALE = W / ((LON_MAX - LON_MIN) * K)
H = round((LAT_MAX - LAT_MIN) * SCALE)

def proj(lon, lat):
    return ((lon - LON_MIN) * K * SCALE, (LAT_MAX - lat) * SCALE)

def decode(topo):
    sx, sy = topo["transform"]["scale"]; tx, ty = topo["transform"]["translate"]
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0; pts = []
        for dx, dy in arc:
            x += dx; y += dy
            pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)
    return arcs

def ring(arcs, idxs):
    pts = []
    for i in idxs:
        a = arcs[i] if i >= 0 else arcs[~i][::-1]
        pts.extend(a if not pts else a[1:])
    return pts

def path(arcs, geom):
    polys = geom["arcs"] if geom["type"] == "MultiPolygon" else [geom["arcs"]]
    out = []
    for poly in polys:
        for r in poly:
            pts = ring(arcs, r)
            if not any(LON_MIN <= lo <= LON_MAX and LAT_MIN <= la <= LAT_MAX for lo, la in pts):
                continue  # territoires d'outre-mer
            xy = [proj(lo, la) for lo, la in pts]
            simp = [xy[0]]
            for p in xy[1:]:
                if math.dist(p, simp[-1]) > 0.8:
                    simp.append(p)
            if len(simp) < 4:
                continue
            out.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in simp) + "Z")
    return "".join(out)

topo = json.load(open(sys.argv[1]))
arcs = decode(topo)
geoms = {g["properties"]["name"]: g for g in topo["objects"]["countries"]["geometries"]}
print(json.dumps({
    "viewBox": f"0 0 {W} {H}",
    "france": path(arcs, geoms["France"]),
    "belgique": path(arcs, geoms["Belgium"]),
    "proj": {"lonMin": LON_MIN, "latMax": LAT_MAX, "k": K, "scale": SCALE},
}))
