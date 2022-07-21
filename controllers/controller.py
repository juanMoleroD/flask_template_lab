from flask import render_template, request, redirect
from app import app
from models.event_list import events, add_event, remove_event
from models.event import Event


@app.route('/events')
def index():
    return render_template('events.html', title='Our Event Planner', events=events)

@app.route('/events/new')
def new_event():
    return render_template('new_event.html', title='new event')

@app.route('/events', methods=['POST'])
def create_event():
    print(request.form)
    date = request.form['date']
    name = request.form['name']
    num_attendees = request.form['num_attendees']
    room = request.form['room']
    description = request.form['description']
    recurring = request.form['recurring']
    new_event = Event(date, name, num_attendees, room, description, recurring)
    add_event(new_event)
    return redirect('/events')

@app.route('/events/delete/<index>', methods=['POST'])
def delete_event_by_index(index):
    remove_event(int(index))
    return redirect('/events')

