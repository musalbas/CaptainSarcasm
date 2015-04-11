from flask import request
from flask import Flask
from flask import Response

from detector import evaluate

app = Flask(__name__)

@app.route('/reply', methods=['POST'])
def reply():
    sarcasm = evaluate.tweetscore(request.form['Body'])
    if sarcasm <= 0:
        xml = "<Response></Response>"
    else:
        xml = "<Response><Sms>Your message has been blocked as sarcasm was detected.</Sms></Response>"
    return Response(xml, mimetype='text/xml')

if __name__ == "__main__":
    app.run(port=8001, host='0.0.0.0')
