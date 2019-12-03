# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    #Adjectives for holding state 
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = ['test', 'item1', 'item2', 'item3',]

    #Methods for changing state
    def add_item(self, item_obj):
        self.items.append(item_obj)
        print(f"You picked up a/an: {item_obj}")

    def remove_item(self, item_obj):
        self.items.remove(item_obj)
        print(f"You put down a/an: {item_obj}")