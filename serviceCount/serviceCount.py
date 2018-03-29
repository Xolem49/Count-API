from flask import Flask

__name__ = "counterAPI"
app = Flask(__name__)
total = 0


@app.route('/count')
def counter():
    global total
    total += 1
    return str(total)


if __name__ == 'counterAPI':
    app.run(host="0.0.0.0", debug=True)
