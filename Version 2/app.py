from flask import Flask, render_template, jsonify, request, Markup
from model import predict_image
import pandas as pd

app = Flask(__name__)

#Importing the Disease File and Supplements File
disease_info = pd.read_csv('disease_info.csv' , encoding='cp1252')
supplement_info = pd.read_csv('supplement_info.csv',encoding='cp1252')

#Home Page
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

#Contact Us Page
@app.route('/contact')
def contact():
    return render_template('contact-us.html')

#Index page
@app.route('/index')
def ai_engine_page():
    return render_template('index.html')

#Market Page
@app.route('/market', methods=['GET', 'POST'])
def market():
    return render_template('market.html', supplement_image = list(supplement_info['supplement image']),
                           supplement_name = list(supplement_info['supplement name']), disease = list(disease_info['disease_name']), buy = list(supplement_info['buy link']))

#Predict Route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            title = disease_info['disease_name'][prediction]
            description =disease_info['description'][prediction]
            prevent = disease_info['Possible Steps'][prediction]
            image_url = disease_info['image_url'][prediction]
            supplement_name = supplement_info['supplement name'][prediction]
            supplement_image_url = supplement_info['supplement image'][prediction]
            supplement_buy_link = supplement_info['buy link'][prediction]
            #print(supplement_name,title, description, prevent, image_url)
            return render_template('submit.html' , title = title , desc = description , prevent = prevent , 
                               image_url = image_url , pred = prediction ,sname = supplement_name , simage = supplement_image_url , buy_link = supplement_buy_link)
        except:
            pass
    return render_template('index.html', status=500, res="Internal Server Error")

#Running the Main Method
if __name__ == "__main__":
    app.run(debug=True)