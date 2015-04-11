from flask import request
from flask import Flask

from detector import evaluate

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    return str(evaluate.tweetscore(request.form['message']))

if __name__ == "__main__":
    app.run(port=8002, host='0.0.0.0')
