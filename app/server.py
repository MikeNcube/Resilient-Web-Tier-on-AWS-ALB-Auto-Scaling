import os
import socket
from flask import Flask, jsonify, Response

app = Flask(__name__)

# Dashboard Endpoint (Root)
@app.route("/", methods=["GET"])
def dashboard():
    host = socket.gethostname()
    az = os.environ.get("AWS_AZ", "unknown-az")
    msg = f"Dashboard data served from host {host}.ec2.internal in {az} availability zone"
    return Response(msg, mimetype="text/plain")

# "Private" Endpoint (Demo Only)
@app.route("/private", methods=["GET"])
def private_data():
    return jsonify({"secret": "simulated private data – not for public exposure"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
