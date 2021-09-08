from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from werkzeug.utils import secure_filename
import os
import pandas as pd
app = Flask(__name__)
from temp import  analyse,compare,fun
app.config['UPLOAD_PATH'] = 'uploads'
app.config['UPLOAD_EXTENSIONS'] = ['.csv']


@app.route("/")
def index():
    title = "Solutions"
    return render_template("index.html",title=title)

@app.route("/login")
def login():
    title = " KINDLY LOGIN "
    mail_id = request.form.get("mail_id")
    password = request.form.get("password_")
    return render_template("login.html",title=title)



@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
    data = pd.read_csv(uploaded_file)
    fun(data)
    data_dict = dict()
    for col in data.columns:
        data_dict[col] = data[col].to_list()
    return jsonify(data_dict)


if __name__=="__main__":
    app.run(debug=True,port=8000)