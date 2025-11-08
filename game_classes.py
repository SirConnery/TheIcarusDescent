class Room:
    def __init__(self, name, description, forward=None, backward=None, left=None, right=None, actions=None, on_enter=None):
        
        # Descriptions
        self.name = name
        self.description = description

        # Exits
        self.forward = forward
        self.backward = backward
        self.left = left
        self.right = right

        # Actions and events
        self.on_enter = on_enter

    # Helpers
    def get_exits(self, direction):
        direction = direction.upper()
        
        match direction:
            case "FORWARD" | "F":
                return self.forward
            case "BACKWARD" | "B":
                return self.backward
            case "LEFT" | "L":
                return self.left
            case "RIGHT" | "R":
                return self.right
            case _:
                return None