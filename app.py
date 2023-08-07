from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aircraft_data')
def get_aircraft_data():
    with open('json/aircraft.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
