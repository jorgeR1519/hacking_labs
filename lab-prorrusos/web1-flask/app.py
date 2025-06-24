from flask import Flask, request, send_from_directory
import os

app = Flask(__name__, static_folder="www", static_url_path="")

WWW = os.path.join(os.getcwd(), "www")

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(WWW, "index.html")

@app.route("/", methods=["PUT"])
def deface():
    try:
        data = request.data
        with open(os.path.join(WWW, "index.html"), "wb") as f:
            f.write(data)
        return "Defacement aplicado!", 200
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
