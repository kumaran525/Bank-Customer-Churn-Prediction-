import numpy as np
from flask import Flask, request, jsonify, render_template
from Transform import Transform
import pickle

application = Flask(__name__) #Initialize the flask App
model = pickle.load(open('Pickles/model.pkl', 'rb'))

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    T=Transform()
    print(len(int_features))
    Usage_features=list(int_features[2:])
    prediction = T.transform(Usage_features)
    if prediction == 0:
        output = "Bank may lose this customer who is having  id no {id}".format(id=int_features[1])
    elif prediction == 1:
        output = "Customer may continue to stay as a customer in the bank who is having id no {id}".format(id=int_features[1])
    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    application.run(debug=True)
