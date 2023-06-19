import numpy as np
from flask import Flask,render_template,request,jsonify
import pickle


# Initialize the app
app = Flask(__name__)

# Loading the model
model = pickle.load(open('src/linear_regressor.pkl','rb'))

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict',methods = ['POST'])
def prediction():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    result = np.round(prediction[0],2)
    return render_template('index.html', prediction_text = 'Predicted Price = $ {}'.format(result))

app.run(debug = True)