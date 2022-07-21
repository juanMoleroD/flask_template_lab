class Event:
    def __init__(self, date, name, num_attendees, room, description, recurring):
        self.date = date
        self.name = name
        self.num_attendees = num_attendees
        self.room = room
        self.description = description
        self.recurring = recurring