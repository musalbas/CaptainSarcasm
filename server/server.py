from flask import Flask

from detector import evaluate

app = Flask(__name__)

@app.route('/api')
def api():
    return "hi"

if __name__ == "__main__":
    app.run()
