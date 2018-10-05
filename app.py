from flask import Flask, render_template, flash, redirect, request, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from forms import ApplicationForm


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
    form = ApplicationForm()
    message = ''
    if form.validate_on_submit():
        first_name = form.firstname.data
        last_name = form.lastname.data

        grade = form.grade.data
        Years_At_present_Employment = form.Years_At_present_Employment.data

        expenses = form.expenses.data
        income = form.income.data
        dti = (expenses / (income / 12)*100)

        Delinquency = form.Delinquency.data
        Collections = form.Collections.data
        Derogatory = form.Derogatory.data
        Housing_MORTGAGE = form.Housing_MORTGAGE.data
        Housing_OWN = form.Housing_OWN.data
        Housing_RENT = form.Housing_RENT.data

        print(first_name)
        print(last_name)

        print(grade)
        print(Years_At_present_Employment)
        print(expenses)
        print(income)
        print(dti)
        print(Delinquency)
        print(Collections)
        print(Derogatory)
        print(Housing_MORTGAGE)
        print(Housing_OWN)
        print(Housing_RENT)

        # db logic goes here

        print("\nData received. Now redirecting ...")
        return redirect(url_for('return_loan_application'))

    return render_template('loan_application.html', form=form, message=message)


# @app.route('/application_complete', methods=['GET', 'POST'])
# def return_application_complete():
#     return render_template('application_complete.html', form=form)


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
