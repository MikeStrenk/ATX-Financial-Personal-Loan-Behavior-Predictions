from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def return_homepage():
    return render_template('homepage.html')


@app.route('/loan_history')
def return_loan_history():
    return render_template('loan_history.html')


@app.route('/loan_application')
def return_loan_application():
    return render_template('loan_application.html')


if __name__ == '__main__':
    app.run(debug=True)
