# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.room_items = []

    def current_items(self):
        if len(self.room_items) > 0:
            return f'Items: {self.room_items}'
        else:
            return f'\nThere are not items here'