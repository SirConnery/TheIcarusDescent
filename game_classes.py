class Game:
    def __init__(self):
        self.running = True
        self.cur_act = 1

class Player:
    def __init__(self):
        self.cur_room = None
        self.output = ""
        self.output_debug = ""
        self.output_error = ""
        self.output_help = ""
        self.output_act_title = ""

        self.name = "Natalie"
        self.status = "Healthy"
        self.warmth = "Cold"
        self.heartrate = "Calm"
        self.inventory = {}
        self.inventory_names = []

    # Helpers

    def add_item(self, item):
        item_name = item.name.lower()
        self.inventory[item_name] = item
    def remove_item(self, item):
        item_name = item.name.lower()
        if item_name in self.inventory:
            del self.inventory[item_name]

    
    # Actions

    def enter_room(self, room_moved_to):
        self.cur_room = room_moved_to
        self.output += self.cur_room.get_entry_event()

    def move(self, direction):
        if not self.cur_room:
            self.output_error = "You are nowhere!"
            return

        new_room = self.cur_room.get_exits(direction)
        if new_room:
            self.output += f"You enter {new_room.name}. \n\n"
            self.enter_room(new_room)
        else:
            self.output_error = "Unrecognized or invalid direction"

    def survey(self):
        self.output = self.cur_room.on_survey

    def interact(self, keyword):
        self.output_debug = "Interacted."
        sources = [self.cur_room.interactables]

        obj = get_object_by_keyword(sources, keyword)
        if obj:
            obj.on_interact()
        else:
            self.output_error = f"No interactable {keyword} in this room."

    
    def look(self, keyword):
        self.output_debug = "Looked"
        sources = [self.cur_room.interactables, self.cur_room.items, self.cur_room.sceneries, self.inventory]

        obj = get_object_by_keyword(sources, keyword)
        if obj:
            self.output = obj.on_look
        else:
            self.output_error = f"No interesting {keyword} in this location."

    def take(self, keyword):
        self.output_debug = "Take"

        sources = [self.cur_room.items]

        item = get_object_by_keyword(sources, keyword)
        if item:
            item.pick_up(self, self.cur_room)
            self.output_debug = f"You have taken {item.name}."
        else:
            self.output_error = f"No item named {keyword} in this location."
    
    def drop(self, keyword):
        self.output_debug = "Drop"

        sources = [self.inventory]

        item = get_object_by_keyword(sources, keyword)
        if item:
            item.drop(self, self.cur_room)
            self.output_debug = f"You have dropped {item.name}."
        else:
            self.output_error = f"No item named {keyword} in your inventory."    
    
    def help(self):
        self.output_help = f"""
            Use commands like below:

            1. Move: move in 4 directions. You can use either WASD or f,b,l,r.
            Example: move w
            Usage: move [w,a,s,d,forward,backward,left,right,f,b,l,r]

            2. Survey: observe your surroundings.
            Usage: survey

            3. Interact: interact with objects in the room or your inventory.
            Example: interact terminal
            Usage: interact [object]

            4. Look: examine objects in the room or inventory.
            Example: look object
            Usage: look [object]

            5. Take: pick up objects from the room.
            Example: take object
            Usage: take [object]

            6. Use: use objects from your inventory on objects in the room.
            Example: use keycard on terminal
            Usage: use [inventory_item] [object]

            7. Help: shows this command list.
            Usage: help

            8. Quit: quit the game.
            Usage: quit
            """



class Room:
    def __init__(self, name, description,
                 forward=None, backward=None, left=None, right=None, 
                 on_first_enter=None, on_revisit=None, has_been_visited=False, 
                 on_survey=None,
                 items = None, interactables = None, use_targets = None, sceneries = None):
        
        # Descriptions
        self.name = name
        self.description = description

        # Exits
        self.forward = forward
        self.backward = backward
        self.left = left
        self.right = right

        # Actions and events
        self.on_first_enter = on_first_enter
        self.on_revisit = on_revisit
        self.has_been_visited = has_been_visited
        self.on_survey = on_survey

        # Items
        self.items = {}
        self.interactables = {}
        self.use_targets = {}
        self.sceneries = {}
        
    # Functions

    def get_entry_event(self):
        if not self.has_been_visited:
            self.has_been_visited = True
            return self.on_first_enter
        return self.on_revisit
    
    def add_item(self, item):
        item_name = item.name.lower()
        self.items[item_name] = item

    def remove_item(self, item):
        item_name = item.name.lower()
        if item_name in self.items:
            del self.items[item_name]
        

    # Helpers

    def get_exits(self, direction):
        direction = direction.upper()
        
        match direction:
            case "FORWARD" | "F" | "W":
                return self.forward
            case "BACKWARD" | "B" | "S":
                return self.backward
            case "LEFT" | "L" | "A":
                return self.left
            case "RIGHT" | "R" | "D":
                return self.right
            case _:
                return None

class Item:
    def __init__(self, name, description, keywords, on_look="", can_take=False):
        
        # Descriptions
        self.name = name
        self.description = description
        self.keywords = keywords
        self.on_look = on_look

        # Utility
        self.can_take = can_take

    def pick_up(self, player, room):
        player.add_item(self)
        room.remove_item(self)
    
    def drop(self, player, room):
        player.remove_item(self)
        room.add_item(self)

    

class Interactable:
    def __init__(self, name, description, keywords, on_interact, on_look=""):
        
        # Descriptions
        self.name = name
        self.description = description
        self.keywords = keywords
        self.on_look = on_look

        # Interact
        self.on_interact = on_interact

class UseTarget:
     def __init__(self, name, description, keywords, on_use, on_look=""):
        
        # Descriptions
        self.name = name
        self.description = description
        self.keywords = keywords
        self.on_look = on_look

        # Interact
        self.on_use = on_use

class Scenery:
    def __init__(self, name, keywords, description, on_look=""):

         # Descriptions
        self.name = name
        self.keywords = keywords
        self.description = description
        self.on_look = on_look



# Universal helper
def get_object_by_keyword(sources, keyword):
    for source in sources:
        for obj in source.values():
            if hasattr(obj, "keywords") and keyword in obj.keywords:
                return obj
    return None