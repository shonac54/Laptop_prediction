import os
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Get the correct path to 'model.pkl'
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')

# Load the model
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError as e:
    print(f"Error loading the model: {e}")
    exit(1)

@app.route("/", methods=["GET"])
def some():
    return render_template("home.html")

@app.route("/", methods=["POST"])
def hello():
    ram = float(request.form['ram'])
    hdd = float(request.form['hdd'])
    ssd = float(request.form['ssd'])
    flash = float(request.form['flash'])
    hybrid = float(request.form['hybrid'])
    predict = model.predict([[ram, hdd, ssd, flash, hybrid]])

    predict = round(predict[0], 2)
    return render_template("home.html", price=predict, ram=ram, hdd=hdd, ssd=ssd, flash=flash, hybrid=hybrid)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

