# Radar Cleo Skin

**Voir l'outil : https://oumaymal1.github.io/radar-cleo-skin/**

Un prototype construit par Oumayma Lamine pour Primaa, dans le cadre d'une candidature de stage de fin d'études. Il note 30 laboratoires de France et de Belgique selon leur capacité à adopter Cleo Skin, à partir de sources publiques uniquement.

> Prototype indépendant, ni produit ni validé par Primaa. Aucune donnée patient, aucune image médicale, aucune allégation sur la performance clinique de Cleo.

---

## Pourquoi cet outil

Le meilleur moyen de montrer ce que je sais faire m'a semblé être de le faire pour Primaa. Voici le cheminement qui m'y a menée.

### 1. Je suis d'abord partie de Primaa

Avant de construire quoi que ce soit, j'ai étudié l'entreprise à partir de sources publiques : ses produits, ses clients, ses partenaires et sa dernière levée de fonds. Un point a retenu mon attention : Primaa a levé 7 millions d'euros, notamment pour renforcer son équipe commerciale et accélérer son déploiement en Europe. J'en ai déduit qu'à ce stade, le développement commercial occupe sans doute une place importante dans ses priorités, aux côtés du développement de Cleo.

### 2. J'ai ensuite cherché le problème concret derrière cet enjeu

Cleo ne peut fonctionner que dans un laboratoire qui a déjà numérisé ses lames. Or beaucoup de laboratoires travaillent encore au microscope. Pour une équipe commerciale, la vraie question est donc : quels laboratoires sont prêts aujourd'hui, et lesquels faut-il appeler en premier ?

Cette information existe, mais elle est éparpillée : communiqués des éditeurs de logiciels, actualités des hôpitaux, appels d'offres, réseaux de spécialistes. L'équipe de Primaa dispose très probablement déjà de sa propre vision du marché ; j'ai voulu voir ce qu'il était possible de reconstituer à partir des seules sources publiques.

### 3. J'ai donc construit un outil qui rassemble ces informations

Je me suis concentrée sur Cleo Skin, en France et en Belgique. L'outil note chaque laboratoire sur 100 à partir de cinq questions simples.

| Question | Points |
|---|---|
| Le laboratoire est-il passé au diagnostic sur écran ? | 25 |
| Traite-t-il beaucoup de cancers de la peau ? | 25 |
| Utilise-t-il un logiciel dans lequel Cleo peut déjà s'intégrer ? | 20 |
| A-t-il annoncé quelque chose de récent qui en fait le bon moment pour le contacter ? | 15 |
| Est-il proche d'un établissement qui utilise déjà Cleo ? | 15 |

Chaque réponse renvoie à sa source et à sa date. Quand une information n'est pas publique, l'outil ne devine pas : il l'indique, et cela devient une question à poser lors du premier appel.

La note place chaque laboratoire dans un niveau :

- **Chaud, 75 et plus** : on appelle maintenant.
- **Tiède, de 50 à 74** : on prépare l'approche.
- **À surveiller, moins de 50** : on suit les signaux.

### 4. Ce que cela apporte

L'équipe commerciale voit en un coup d'œil, sur une carte et une liste classée, quels laboratoires appeler en priorité, pourquoi c'est le bon moment et comment les aborder. Deux exemples de ce que l'outil fait ressortir :

- Unilabs vient d'adopter la plateforme Proscia, dans laquelle Cleo Skin est déjà intégré.
- Le centre hospitalier de Saint-Nazaire a annoncé en octobre 2026 qu'il se préparait à l'arrivée de l'IA dans son service de pathologie.

Aujourd'hui, l'outil couvre 30 laboratoires. La même méthode pourrait s'étendre à d'autres pays, aux États-Unis ou à Cleo Breast.

---

## Ce que contient la page

- **Les chiffres clés** du radar.
- **Ce qui bouge sur le marché** : quatre faits publics récents, avec leur source.
- **Le radar** : une carte et une liste classée, filtrables par niveau, pays et type d'établissement. Un clic sur un laboratoire ouvre sa fiche, avec le détail de la note, les preuves, « pourquoi maintenant » et « comment l'aborder ».
- **Les références déjà en place** : les établissements qui utilisent déjà Cleo, d'après les sources publiques.
- **La méthode de notation.**

## Comment c'est construit

| Fichier | Rôle |
|---|---|
| `index.html` | La page : mise en forme et interactions, sans bibliothèque externe. Elle lit ses données au chargement. |
| `comptes.json` | Les 30 laboratoires, les 6 références et le contexte du marché. Chaque critère porte ses points, sa preuve, sa source et sa date. |
| `carte.json` | Le tracé de la France et de la Belgique, généré depuis les données libres world-atlas. |
| `carte.py` | Génère `carte.json`. |

**Mettre à jour le radar** : modifier `comptes.json` (ajouter un laboratoire, corriger une source). La page relit le fichier à chaque ouverture et recalcule toute seule les notes à partir des points de chaque critère.

## Limites connues

- Les données datent du 23 octobre 2026 et ne se mettent pas à jour automatiquement.
- Sectra est compté comme logiciel compatible parce qu'il figure parmi les partenaires sur le site de Primaa. L'intégration de Cleo Skin dans Sectra reste à confirmer.
- Certaines sources sont anciennes (par exemple la liste des centres experts CARADERM, de 2015). La date est affichée à côté de chaque preuve.
- Le style visuel s'inspire du site de Primaa, sans reprendre son logo ni sa police.

---

Oumayma Lamine
