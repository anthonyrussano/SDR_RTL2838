from flask import Flask, jsonify, render_template
import subprocess
import json
import atexit

app = Flask(__name__)


# Shutdown handler to release resources
def shutdown_handler():
    global sdr_thread
    if sdr_thread:
        sdr_thread.stop()  # Implement the stop method for your data collection thread


# Register the shutdown handler
atexit.register(shutdown_handler)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/aircraft_data")
def get_aircraft_data():
    with open("json/aircraft.json", "r") as f:
        data = json.load(f)

    # Add additional data for each flight
    for aircraft in data["aircraft"]:
        aircraft["speed"] = 500
        aircraft["heading"] = 120
        aircraft["vertical_speed"] = 1000

    return jsonify(data)


if __name__ == "__main__":
    subprocess.Popen(["./dump1090", "--quiet", "--net", "--write-json", "json/"])
    app.run(debug=True, host="0.0.0.0", port=5000)
