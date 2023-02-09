from flask import render_template, request, redirect
from app import app
from models.event_list import event_list, add_new_event
from models.event import *
import datetime

# if 'recurring' in request.form:
#     recurring = True
# else:
#     recurring = False

@app.route('/events')
def index():
    return render_template('index.html', title="Home", event_list=event_list)

@app.route('/events/new')
def new_event():
    return render_template('new_event.html')

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    split_date = event_date.split('-')
    date_year = int(split_date[0])
    date_month = int(split_date[1])
    date_day = int(split_date[2])
    event_date = datetime.date(date_year, date_month, date_day)
    event_name = request.form['name']
    event_guest_amount = request.form['guest_amount']
    event_room_location = request.form['room_num']
    event_desc = request.form['desc']
    event_recurring = request.form['recurring']
    new_event = Event(event_date, event_name, event_guest_amount, event_room_location, event_desc, event_recurring)
    add_new_event(new_event)
    return redirect('/events')

@app.route('/events/delete')
def choose_event_to_delete():
    return render_template('delete_event.html')

@app.route('/events', methods=['POST'])
def delete_event():
    event_name = request.form['name_to_delete']
    split_date = event_date.split('-')
    date_year = int(split_date[0])
    date_month = int(split_date[1])
    date_day = int(split_date[2])
    event_date = datetime.date(date_year, date_month, date_day)
    new_list = delete_event(event_name, event_date)
    return redirect('/events', event_list = new_list)


