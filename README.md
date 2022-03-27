# P7_ISSA_Walaa
# OpenClassrooms - Projet 7 - Implémentez un modèle de scoring

## Objectives du projet :

1. Construire un modèle de scoring qui donnera une prédiction sur la probabilité de faillite d'un client de façon automatique.
2. Construire un dashboard interactif à destination des gestionnaires de la relation client permettant d'interpréter les prédictions faites par le modèle, et d’améliorer la connaissance client des chargés de relation client.

## Data
Les données utilisées dans ce projet sont disponible sur kaggle : https://www.kaggle.com/c/home-credit-default-risk/data

Le projet est developé avec Jupyter Notebook et Python 3.7

## Les fichiers et les dossiers du projet :

* Dossier **data_API** : Données des clients utiliser dans l'API et le Dashboard
* Dossier **models** : Modèle de scoring (logistic regression) et Modèle KNN (pour la visualisation des clients similaires)
* Fichier **P7_01_exploration.ipynb** : Notebook de l'exploration des données et feature engineering
* Fichier **P7_01_modélisation.ipynb** : Notebook du dévelopement du modèle de scoring pour la prédiction de la faillite d'un client
* fichier **P7_02_API** : API de prédiction de probabilité de faillite des clients
* Fichier **P7_03_dashboard** : Dashbord interactif détail dans le repository https://github.com/Line30/P7_dashboard_streamlit

## Déployement du modèle sous forme d'API ;
L'API est développée avec Flask et déployée sur heroku, les endpoints de l'API : 
* load_data : requête pour charger l'id des clients
* predict : requête pour prédire le score d'un client sélectionné (accepté ou refusé)
* load_data_predict : requête pour charger les données avec le score prédit

## Lien de l'API et du Dashboard :
* API : https://p7-scoring-model.herokuapp.com/ (en local : http://127.0.0.1:5000/)
* Dashboard : https://p7-scoring-model-dashboard.herokuapp.com/ (en local : http://localhost:8506/)
