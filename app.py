from flask import Flask, request, jsonify
import subprocess
import json

from gen2 import start

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    k = request.args.get('k')
    return jsonify(start(k))

if __name__ == '__main__':
    app.run(debug=True)