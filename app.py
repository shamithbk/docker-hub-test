from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

@app.route('/status/verify', methods=['GET'])
def verify():
    return jsonify({"info": "Everything looks good"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
