import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

model = pickle.load(open('outputs/models/model.pkl', 'rb'))

app = Flask(__name__, template_folder='template') #Initialize the flask App

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST', 'GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    lst = [float(x) for x in request.form.values()]
    features = [np.array(lst)]
    result = model.predict_proba(features)
    output = round((result[0][0] * 100), 2)

    model_prediction = 'Patient has about {}% chance of survival.'.format(output)

    return render_template('index.html', prediction=model_prediction, show_prediction=True)

if __name__ == '__main__':
    app.run(debug=True)