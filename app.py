from flask import Flask, render_template

app = Flask(__name__)

from data import personal_data


@app.route('/')
def index():
    return render_template('index.html', **personal_data)


if __name__ == '__main__':
    app.run(debug=True)
