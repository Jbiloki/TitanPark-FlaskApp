from flask import Flask, render_template, request
import datetime
import os
import pandas as pd
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', title='Titan Park | Home')

@app.route('/student', methods=['GET','POST'])
def student():
    return render_template('student.html', title='Titan Park | Get parking prediction', currDay = datetime.datetime.now().strftime('%m/%d/%Y'),
    currTime = datetime.datetime.time(datetime.datetime.now()).strftime('%H:%M'))

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
    date = request.form['date']
    time = request.form['time']
    try:
        datetime.datetime.strptime(date, '%m/%d/%Y')
    except ValueError:
        return render_template('badinput.html', title='Titan Park | Get parking prediction', error = 'Bad date')
    try:
        datetime.datetime.strptime(time, '%H:%M')
    except ValueError:
        return render_template('badinput.html', title='Titan Park | Get parking prediction', error = 'Bad time')
    given_time = datetime.datetime.strptime(time, '%H:%M').time()
    given_date = datetime.datetime.strptime(date, '%m/%d/%Y').date()
    dt = pd.to_datetime(datetime.datetime.combine(given_date, given_time))
    eastside = joblib.load('eastsidemodel.pkl')
    statecollege = joblib.load('statecollegemodel.pkl')
    nutwood = joblib.load('nutwoodmodel.pkl')
    hour = dt.hour
    minute = dt.minute
    dow = dt.dayofweek
    mo = dt.month
    day = dt.day
    week = dt.week
    woy = dt.weekofyear
    resulteastside = eastside.predict([0,hour,minute,dow,mo,day,woy,week])
    resultstatecollege = statecollege.predict([0,hour,minute,dow,mo,day,woy,week])
    resultnutwood = nutwood.predict([0,hour,minute,dow,mo,day,woy,week])
    structure = 0
    eastsidecap = 1365
    nutwoodcap = 2439
    statecollegecap = 1339
    resultString = 'Here are the lot results'
    return render_template('result.html', title='Titan Park | Parking results', resulteastside = eastsidecap - int(resulteastside), resultstatecollege = statecollegecap - int(resultstatecollege),resultnutwood = nutwoodcap - int(resultnutwood),resultString = resultString)
    #if int(result) < cap/2:
#        resultString = 'There is more than half the lot empty'
#        return render_template('result.html', title='Titan Park | Parking results', resulteastside = eastsidecap - int(resulteastside), resultstatecollege = statecollegecap - int(resultstatecollege),resultnutwood = nutwoodcap - int(resultnutwood),resultString = resultString)
#    elif int(result) > cap:
#        resultString = 'The lot is full'
#        return render_template('result.html', title='Titan Park | Parking results', resulteastside = eastsidecap - int(resulteastside), resultstatecollege = statecollegecap - int(resultstatecollege),resultnutwood = nutwoodcap - int(resultnutwood),resultString = resultString)
#    else:
#        resultString = 'The lot is more than half full'
#        result = cap - int(result)
#        return render_template('result.html', title='Titan Park | Parking results', resulteastside = eastsidecap - int(resulteastside), resultstatecollege = statecollegecap - int(resultstatecollege),resultnutwood = nutwoodcap - int(resultnutwood),resultString = resultString)


if __name__ == '__main__':
    app.run(debug=True)
