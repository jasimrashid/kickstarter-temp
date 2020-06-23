# web_app/routes/stats_routes.py

from flask import Blueprint, request, jsonify, render_template

from sklearn.linear_model import LogisticRegression

from web_app.models import User
from web_app.services.basilica_service import connection as basilica_api_client
import os
import pickle
from sklearn.datasets import load_iris
from pandas import read_csv

MODEL_FILEPATH = os.path.join(os.path.dirname(__file__), "..","..", "models", "latest_model.pkl")

stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form)) #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    category = request.form["category"]
    pitch = request.form["pitch"]
    x = int(request.form["x"])
    y = int(request.form["y"])
    z = int(request.form["z"])

    #FOR TESTING PURPOSES ONLY - THE MODEL ONLY USES X AND Y FROM THE FORM
    classifier = LogisticRegression()
    clf = load_model()
    print("CLASSIFIER:", clf)
    inputs = [[x, y]]
    print(type(x))
    print(type(inputs), inputs)
    result = clf.predict(inputs)
    print("RESULT:", result)
    print("-----------------")
    print("MAKING A PREDICTION...")
    
    return render_template("prediction_results.html",
        x=x,
        y=y,
        z=z,
        category = category,
        result=result[0]
    )


def train_and_save_model():
    print("TRAINING THE MODEL...")
    X, y = load_iris(return_X_y=True)
    classifier = LogisticRegression() # for example
    classifier.fit(X, y)

    print("SAVING THE MODEL...")
    with open(MODEL_FILEPATH, "wb") as model_file:
        pickle.dump(classifier, model_file)

    return classifier

def load_model():
    print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model

if __name__ == "__main__":

    train_and_save_model()

    clf = load_model()
    print("CLASSIFIER:", clf)

    X, y = load_iris(return_X_y=True) # just to have some data to use when predicting
    inputs = [[1,2]]
    print(type(inputs), inputs)

    result = clf.predict(inputs)
    print("RESULT:", result)