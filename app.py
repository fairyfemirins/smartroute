from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Mock traffic camera data
TRAFFIC_CAMERAS = {
    "San Francisco": [
        {"id": 1, "lat": 37.7749, "lon": -122.4194, "url": "https://example.com/camera1.jpg"},
        {"id": 2, "lat": 37.7849, "lon": -122.4094, "url": "https://example.com/camera2.jpg"},
    ],
    "New York": [
        {"id": 3, "lat": 40.7128, "lon": -74.0060, "url": "https://example.com/camera3.jpg"},
        {"id": 4, "lat": 40.7306, "lon": -73.9352, "url": "https://example.com/camera4.jpg"},
    ]
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/route", methods=["GET"])
def get_route():
    start = request.args.get("start", "San Francisco")
    end = request.args.get("end", "New York")
    
    # In a real app, use a routing API (e.g., OpenStreetMap, Google Maps)
    route = {
        "start": start,
        "end": end,
        "coordinates": [
            {"lat": 37.7749, "lon": -122.4194},
            {"lat": 38.5816, "lon": -121.4944},
            {"lat": 40.7128, "lon": -74.0060}
        ]
    }
    
    # Find traffic cameras along the route
    cameras = []
    for city in TRAFFIC_CAMERAS:
        for camera in TRAFFIC_CAMERAS[city]:
            cameras.append(camera)
    
    return jsonify({"route": route, "cameras": cameras})


if __name__ == "__main__":
    app.run(debug=True)