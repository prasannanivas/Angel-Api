
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS
import struct
import csv
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)  # ✅ Allow CORS for all origins


def parse_int64(byte_array):
    """Convert 8-byte array to int64"""
    if len(byte_array) != 8:
        return "Invalid input"
    # Little-endian signed int64
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
    # Convert the trade dict to a JSON string with double quotes
    trade_json = json.dumps(trade_data.get("trade"))
    with open("trades.csv", "a", newline="") as csvfile:
        # Use pipe character as delimiter since it won't appear in our JSON
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow([
            trade_data.get("action"),
            trade_json,
            trade_data.get("timestamp")
        ])
    return jsonify({"status": "success"})

# Endpoint to save the watchlist to a CSV file


@app.route("/api/saveWatchlist", methods=["POST"])
def save_watchlist():
    new_data = request.json.get("watchlist")
    if new_data is None:
        return jsonify({"error": "No watchlist provided"}), 400
    try:
        # Read existing data
        existing_data = []
        try:
            with open("watchlist.csv", "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                existing_data = [{"label": row["label"],
                                  "token": row["token"]} for row in reader]
        except FileNotFoundError:
            pass  # File doesn't exist yet, start with empty list

        # Combine existing and new data, avoiding duplicates
        combined_data = existing_data
        for new_item in new_data:
            if not any(item["token"] == new_item["token"] for item in existing_data):
                combined_data.append(new_item)

        # Write back combined data
        with open("watchlist.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["label", "token"])
            for item in combined_data:
                writer.writerow([item["label"], item["token"]])

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get the saved watchlist from the CSV file


@app.route("/api/getWatchlist", methods=["GET"])
def get_watchlist():
    try:
        watchlist = []
        with open("watchlist.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                watchlist.append(
                    {"label": row["label"], "token": row["token"]})
        return jsonify({"watchlist": watchlist})
    except FileNotFoundError:
        return jsonify({"watchlist": []})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/getTradeHistory", methods=["GET"])
def get_trade_history():
    try:
        trades = {}
        with open("trades.csv", "r", newline="") as csvfile:
            # Use pipe character as delimiter
            reader = csv.reader(csvfile, delimiter='|')
            for row in reader:
                try:
                    if len(row) != 3:
                        print(f"Skipping invalid row: {row}")
                        continue

                    action, trade_data, timestamp = row
                    trade = json.loads(trade_data)

                    if action == "Buy":
                        trades[trade["symbolToken"]] = {
                            "entryPrice": float(trade["entryPrice"]),
                            "targetPrice": float(trade["targetPrice"]),
                            "stopLoss": float(trade["stopLoss"]),
                            "sma20": float(trade.get("sma20", 0)),
                            "rsi": float(trade.get("rsi", 0)),
                            "timestamp": timestamp
                        }
                    elif action == "Sell" and trade["symbolToken"] in trades:
                        trades[trade["symbolToken"]]["exitPrice"] = float(
                            trade["exitPrice"])
                        trades[trade["symbolToken"]
                               ]["exitReason"] = trade["reason"]
                        trades[trade["symbolToken"]]["exitTime"] = timestamp

                except (json.JSONDecodeError, KeyError, IndexError, ValueError) as e:
                    print(f"Error processing row: {row}")
                    print(f"Error details: {str(e)}")
                    continue

        return jsonify({"trades": trades})
    except FileNotFoundError:
        return jsonify({"trades": {}})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
