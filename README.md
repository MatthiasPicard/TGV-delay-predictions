# TGV-delay-predictions

## Objectif
- prédire le temps de retard moyen des trains sur une ligne sur un mois (retard_moyen_arrivee)
- prédire la cause du retard (en pourcentage pour chaque cause potentielle) sur une ligne sur un mois, en rajoutant comme feature le retard moyen prédit juste avant

Ces prédictions se font se font sur tout les mois de l'année 2023 en se basant sur les données disponibles depuis janvier 2018. Nous avons d'abord effectuer une analyse de donnée pour mieux cerner nos problématique, puis nous avons appliquer plusieurs fonctions de preprocessing pour rendre notre dataset compréhensible pour les modèles que nous avons ensuite entraîner.

Vous trouverez deux notebook pythons: 

- **data_visualization.ipynb**: notebook contenant l'ensemble des visualisations de nos données
- **processing_modèle.ipynb**: notebook contenant la partie preprocessing et les modèles entraînés sur chaque problématique.
  
