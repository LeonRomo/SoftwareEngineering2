from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('register.html')


@app.route('/techfundi')
def tech_home():
    return render_template('homepage.html')


@app.route('/login/techfundi')
def tech():
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)
