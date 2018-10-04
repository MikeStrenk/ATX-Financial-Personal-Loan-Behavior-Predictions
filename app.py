from flask import Flask, render_template, flash, redirect, request
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from forms import TestForm


@app.route('/')
def return_homepage():
    return render_template('homepage.html')


@app.route('/charts')
def return_charts():
    return render_template('charts.html')


@app.route('/loan_history')
def return_loan_history():
    return render_template('loan_history.html')


@app.route('/loan_application', methods=['GET', 'POST'])
def return_loan_application():
    form = TestForm()
    return render_template('loan_application.html', form=form)


@app.route('/application_complete', methods=['GET', 'POST'])
def return_loan_application():
    return render_template('application_complete.html', form=form)


# @app.route('/handle_data', methods=['GET', 'POST'])
# def handle_data():
#     form = LoginForm(request.form)

#     if request.method == 'POST' and form.validate():
#         username = form.username.data
#         # db_session.add(user)
#         flash('Thanks for registering')
#         return redirect(url_for('application_complete.html'))
#     return render_template('loan_application.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
