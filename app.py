from flask import Flask, render_template, request, jsonify
from openai_api import generate_mitigation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/generate_mitigation", methods=["POST"])
def handle_generate_mitigation():
    description = request.json["description"]
    mitigation = generate_mitigation(description)
    return jsonify({ "mitigation": mitigation })

if __name__ == '__main__':
    app.run()
