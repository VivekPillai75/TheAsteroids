#!/usr/bin/env python
# coding: utf-8


from flask import Flask, render_template, request, redirect, url_for, send_file
import os

#we are importing the function that makes predictions.
from Prediction import predictor, plots
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True
#print(app.instance_path)
#from os import chdir

@app.route('/')
def index():
    #chdir('C:/Users/abhir/OneDrive/Untitled Folder/templates')
    return render_template('index.html')



@app.route("/", methods=['POST'])
def uploadFiles():
    uploaded_file = request.files['file']
    
    if uploaded_file.filename != '':
        file_path = ( "file.csv")
        uploaded_file.save(file_path)
    return redirect(url_for('downloadFile'))


@app.route('/download')
def downloadFile ():
    path = ("file.csv")
    
    predictions=predictor(pd.read_csv(path))
    predictions.to_csv('predictions.csv',index=False)
    plots(pd.read_csv('predictions.csv'))
    return send_file("predictions.csv", as_attachment=True)



if (__name__ == "__main__"):
     app.run(debug=True,host='0.0.0.0', port=9010)





