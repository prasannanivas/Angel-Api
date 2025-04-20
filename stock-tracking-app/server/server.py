from flask import Flask, request, jsonify
from flask_cors import CORS
import struct
import csv
from datetime import datetime

app = Flask(__name__)
CORS(app)

def parse_int64(byte_array):
    if len(byte_array) != 8:
        return "Invalid input"
    return struct.unpack("<q", bytearray(byte_array))[0]

@app.route("/parse-int64", methods=["POST"])
def parse():
    data = request.json.get("data")
    if not data or len(data) != 8:
        return jsonify({"error": "Invalid input, expected 8-byte array"}), 400

    parsed_value = parse_int64(data)
    return jsonify({"parsedInt64": parsed_value})

@app.route("/api/recordTrade", methods=["POST"])
def record_trade():
    trade_data = request.json
    with open("data/trades.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([trade_data.get("action"), trade_data.get("trade"), trade_data.get("timestamp")])
    return jsonify({"status": "success"})

@app.route("/api/saveWatchlist", methods=["POST"])
def save_watchlist():
    data = request.json.get("watchlist")
    if data is None:
        return jsonify({"error": "No watchlist provided"}), 400
    try:
        with open("data/watchlist.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["label", "token"])
            for item in data:
                writer.writerow([item.get("label"), item.get("token")])
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/getWatchlist", methods=["GET"])
def get_watchlist():
    try:
        watchlist = []
        with open("data/watchlist.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                watchlist.append({"label": row["label"], "token": row["token"]})
        return jsonify({"watchlist": watchlist})
    except FileNotFoundError:
        return jsonify({"watchlist": []})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)