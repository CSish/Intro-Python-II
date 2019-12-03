# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []

    def make_move(self, new_location):
        self.location = new_location
        print(f'Location: {self.location.name}')
        print(self.location.desc)


    #Crud Operations
    def add_item(self, item_obj):
        self.items.append(item_obj)
        print(f'You picke up a/an: {item_obj}')
        return self.items

    def list_items(self):
        return self.items

    def show_item(self, item_obj): #retruns index
        return self.items.index(item_obj)

    def remove_item(self, item_obj):
        self.items.remove(item_obj)
        self.location.add_item(item_obj)
        print(f'You put down a/an: {item_obj}')