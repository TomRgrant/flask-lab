from models.event import *
import datetime

event_1 = Event (datetime.date(2024,3,23), "Wedding", 120, 4, "Chriss and Chrissy's Wedding", False)
event_2 = Event (datetime.date(2024,3,23), "Birthday", 20, 8, "Harry's Birthday", False)
event_3 = Event (datetime.date(2024,3,23), "Hackathon", 75, 17, "Local Hackathon", True)

event_list = [event_1, event_2, event_3]

def add_new_event(new_event):
    event_list.append(new_event)

def delete_event(event_name, event_date):
    for event in event_list:
        if event_name == event.name and event_date == event.date:
            event_list.pop(event)
    return event_list
