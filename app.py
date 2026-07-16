from flask import Flask,jsonify
import datetime

app = Flask(__name__)
@app.route('/health')

def health():
    return jsonify({
        "status": "ok",
        "timestamp": str(datetime.datetime.now())
    })

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)