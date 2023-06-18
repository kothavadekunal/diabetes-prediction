import numpy as np
from flask import Flask,render_template,request,jsonify
import pickle


# Initialize the app
app = Flask(__name__)

# Loading the model
model = pickle.load(open('linear_regressor.pkl','rb'))

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict',methods = ['POST'])
def prediction():
    # carat = request.form.get("carat")
    # depth = request.form.get("depth")
    # table = request.form.get("table")
    # x = request.form.get("x")
    # y = request.form.get("y")
    # z = request.form.get("z")
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    result = np.round(prediction[0],2)
    return render_template('index.html', prediction_text = 'Predicted Price = $ {}'.format(result))

app.run(debug = True)