from YNXSystem import app
from flask import render_template, Flask, request, jsonify

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    return render_template("index.html")
@app.route('/calculate', methods=['POST'])
def calculate():
    print("gooo")
    data = request.form["date"]
    return jsonify({"data": data})