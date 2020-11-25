import sklearn
import joblib
import pandas as pd
from fonctions_maisons import extaire_la_premiere_lettre
from flask import Flask, request

# Load Model
pipeline = joblib.load('titanic.model')

# Démarrer l'appli Flask
app = Flask('__name__')

# Faire des predictions 
@app.route('/predict', methods=['POST'])
def predict():
  df = pd.DataFrame(request.json)
  résultat = pipeline.predict(df)[0]
  return (str(résultat), 201)

# Page d'accueil
@app.route('/')
def index():
  return "<h1>Bievenue dans notre API. Utiliser /predict en POST pour faire des preédictions sur le Titanic</h1>"

# Tester l'api
@app.route('/ping', methods=['GET'])
def ping():
  return ('pong', 200)


# Si on est dans le main, on lance.
if __name__ == "__main__":
  app.run(host='0.0.0.0')


