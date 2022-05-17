#%%file app.py

from flask_restful import Resource, Api
from flask import Flask
from flask import request, jsonify
import joblib


app = Flask(__name__)
api = Api(app)

@app.route('/predict', methods=['GET'])
model = joblib.load('model.pkl')
def predict():
    sepal_length = float(request.args.get('sl'))
    petal_length = float(request.args.get('pl'))

    features = [sepal_length, petal_length]
    prediction = int(model.predict(features))
    return jsonify(features=features,
    predicted_class=prediction)

if __name__ == '__main__':
    app.run(port = 3333, host='0.0.0.0', debug = True)

api.add_resource(Main, '/testClass')    
