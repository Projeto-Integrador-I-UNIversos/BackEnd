from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/Login", methods=['GET'])
def login():
    data =  {"usuarios":["Lara", "Larissa"]}
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=8000)