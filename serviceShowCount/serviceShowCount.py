import requests
from flask import Flask

__name__ = "showCount"
app = Flask(__name__)


@app.route('/show')
def show():
    r = requests.get('http://localhost:5000/count')
    result = "The result returned by the counter Webservice is : " + r.text
    return result


if __name__ == 'showCount':
    app.run(host="0.0.0.0", debug=True)
