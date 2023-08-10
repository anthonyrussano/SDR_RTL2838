from flask import Flask, jsonify, render_template
import subprocess
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/aircraft_data")
def get_aircraft_data():
    with open("json/aircraft.json", "r") as f:
        data = json.load(f)

    # Add additional data for each flight
    for aircraft in data["aircraft"]:
        # Replace the following placeholders with the actual values from your data
        aircraft["speed"] = 500
        aircraft["heading"] = 120
        aircraft["vertical_speed"] = 1000

    return jsonify(data)


if __name__ == "__main__":
    subprocess.Popen(["./dump1090", "--quiet", "--net", "--write-json", "json/"])
    app.run(debug=True, host="0.0.0.0", port=5000)
