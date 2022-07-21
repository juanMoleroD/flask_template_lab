from models.event import Event

event_1 = Event("2022-07-07", 'Meeting 1', 7, "room 1", "To talk about all things.", False)
event_2 = Event("2022-07-10", 'gathering', 4, "room 2", "Small catch up on today's work", True)
event_3 = Event("2022-07-15", "party", 20, "the Party Room", "Its the end of the week, let's have a party!", True)

events = [event_1, event_2, event_3]


def add_event(event):
    events.append(event)


def remove_event(index):
    events.pop(index)