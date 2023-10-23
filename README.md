# TGV-delay-predictions

## Objectif
- prédire le temps de retard moyen des trains sur une ligne sur un mois (retard_moyen_arrivee)
- prédire la cause du retard (en pourcentage pour chaque cause potentielle) sur une ligne sur un mois

## Questions

### faire deux modèles distincts ou dépendants pour ces deux problématique?
- si dépendant --> NN avec une regression et des classifs en sortie
- si indépendant --> on a le choix
- mix --> on prédit la regression d'abord puis la classif en se servant des resultats de la regression ( ou inversement)

### Modèles independants pour chaque ligne de train ou tout lier?
- si indépendant, plus facile à gérer on peut facilement créer des séries temporelles, mais beaucoup(beaucoup) de modèle à créer
- si liée, on peut exploiter des correlations en plus et on n'a qu'un modèle, mais on doit encoder l'année, le mois et toutes les gares (avec un one hot ça va faire beaucoup de colonne, avec un ordinal on introduit une relation d'ordre qui n'existe pas, remarque on aurait pas ce soucis avec des arbres de décision)

### Analyse à faire 
- autocorrelation mois et année sur le temps de retard et les causes du retard
- regarder correlation retard moyen entre paris-lyon et lyon-paris (pour tout les couples de gares)
- pleins d'autres trucs qui nous permettront d'enlever/modifier/rajouter des colonnes

### Données qu'on peut rajouter
- longueur de chaque lignes (pas forcement nécessaire?)
- nombre d'habitants dans chaques ville

### Infos importantes
- https://www.data.gouv.fr/fr/datasets/regularite-mensuelle-tgv-par-liaisons/

### Entree/Sortie
- entrées: date (mois), service,gare départ/arrivée