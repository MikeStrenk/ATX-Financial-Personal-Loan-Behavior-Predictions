from flask import Flask, render_template, flash, redirect, request, url_for
from sklearn.externals import joblib
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from forms import ApplicationForm


tfidf_model = None


def load_tfidf_model():
    global tfidf_model
    tfidf_model = joblib.load('data/model3.pkl')


def convert_to_binary(x):
    if x == 'No':
        return 0
    if x == 'Yes':
        return 1
    else:
        raise ValueError


def convert_credit_grade(grade):
    grade_dict = {
        '>750': 1,
        '>700': 2,
        '>650': 3,
        '>625': 4,
        '>600': 5,
        '>550': 6,
        "Bad Credit": 7
    }
    return grade_dict[grade]


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
        age = form.age.data
        occupation = form.occupation.data

        grade = convert_credit_grade(form.grade.data)
        Years_At_present_Employment = form.Years_At_present_Employment.data

        expenses = form.expenses.data
        income = form.income.data
        dti = round((expenses / (income / 12)*100), 2)

        Delinquency = convert_to_binary(form.Delinquency.data)
        Collections = convert_to_binary(form.Collections.data)
        Derogatory = convert_to_binary(form.Derogatory.data)
        Housing = form.Housing.data

        application_data = [[grade, dti, Delinquency, Collections, Derogatory]]

        probabs_result = tfidf_model.predict_proba(application_data)

        default_chance = probabs_result[1][0][1]

        print('Chance of default: {}'.format(default_chance*100))

        # db logic goes here

        if default_chance > .3:
            message = 'However you have been rejected :('
        else:
            message = 'You have been accepted! :)'

        return render_template('application_complete.html', message=message)

    return render_template('loan_application.html', form=form)


@app.route('/application_complete', methods=['GET', 'POST'])
def return_application_complete(message):
    message = message
    return render_template('application_complete.html', message=message)


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

    try:
        load_tfidf_model()
        print("Model loaded")

    except Exception as e:
        print("Model loading failed")
        print(str(e))

    app.run(debug=False)
