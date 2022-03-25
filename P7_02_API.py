import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, make_response
import joblib
import json
import pickle
from sklearn.neighbors import NearestNeighbors
import shap

app = Flask(__name__)

# Load the joblib model (logistic regression and KNN)
model_LR = joblib.load(open("models//LR_pipeline.joblib", "rb"))

# load the data test and train
data_test_app = pd.read_csv('data_API/X_test_app_sample.csv.zip')
data_test_app = data_test_app.drop(['Unnamed: 0'], axis= 1)
#data_train_app = pd.read_csv('data_API/x_train_app.csv.zip')
#data_train_app = data_train_app.drop(['Unnamed: 0'], axis= 1)

feats = [f for f in data_test_app.columns if f not in ['SK_ID_CURR', 'TARGET']]
#x_train = data_train_app[feats]
#y_train = data_train_app['TARGET']
x_test = data_test_app[feats]
y_test = data_test_app['TARGET']

# ID clients list (data test)
id_clients_test = data_test_app["SK_ID_CURR"].sort_values()
id_clients_test = pd.DataFrame(id_clients_test)
# ID clients list (data train)
#id_clients_train = data_train_app["SK_ID_CURR"].sort_values()
#id_clients_train = pd.DataFrame(id_clients_train)

def generateMetrics():  # page de bienvenue
    description = "Welcome to the API of project \" Implement a scoring model\" \n__________________________________________________________________________________ \n\n\nHere are the endpoints of this API:\n\n---------------------------------------------------------------------------------\nload_data: query to load the id of clients \n---------------------------------------------------------------------------------\npredict: query to predict the score of a selected customer(accepted or refused)\n---------------------------------------------------------------------------------\nload_data_predict: query to load the data with the predicted score\n---------------------------------------------------------------------------------"
    return (description)

@app.route("/", methods=["GET"])  # afficher la description en format texte
def home():
    response = make_response(generateMetrics(), 200)
    response.mimetype = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True)








