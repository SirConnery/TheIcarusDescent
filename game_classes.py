class Room:
    def __init__(self, name, description,
                 forward=None, backward=None, left=None, right=None, 
                 on_first_enter=None, on_revisit=None, has_been_visited=False, 
                 on_survey=None,
                 items = {}, interactables = {}, use_targets = {}):
        
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
        self.items = items
        self.interactables = interactables
        self.use_targets = use_targets
        
        # Functions

    def get_entry_event(self):
        # print("DEBUG Executing room entered function")
        if not self.has_been_visited:
            self.has_been_visited = True
            return self.on_first_enter
        return self.on_revisit
        

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