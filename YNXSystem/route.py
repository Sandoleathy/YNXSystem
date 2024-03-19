from YNXSystem import app
from flask import render_template, Flask, request, jsonify

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    return render_template("index.html")
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.form["date"]
    timeSet = data.split("-")
    print(timeSet)
    year = int(timeSet[0])
    month = int(timeSet[1])
    day = int(timeSet[2])
    return jsonify({
        "result": day,
        "month": month,
        "year": year,
        })