from flask import Flask, request

app = Flask(__name__)

@app.route('/beacon', methods=['POST'])
def beacon():
    data = request.json
    print(f"Beacon from {data.get('host')}: {data}")
    return {"cmd": "sleep 10"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
