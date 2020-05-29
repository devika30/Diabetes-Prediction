from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def diabetes():
    return render_template("diabetes.html")


@app.route('/predict',methods=['POST','GET'])
def predict():  
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final=[np.array(int_features)]
    print(final)
    prediction=model.predict(final)
    output=round(prediction[0],2)
    print(output)
    if output==1:
        return render_template('diabetes.html',pred='You have diabetes',result="diabetes")
    else:
        return render_template('diabetes.html',pred='You dont have diabetes',result="not diabetes")

if __name__ == '__main__':
    app.run(debug=True)