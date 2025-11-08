from game_classes import Room, Item, Interactables, Scenery

## Rooms

room_map = {}

initial_rooms = {
    "CryoBay": Room(name="Cryo Bay", 
        description="It is a room with cryo stuff.",),
    "CryoVestibule": Room(name="Cryo Vestibule",
        description="It is a vestibule connecting CryoBay, Mess Hall and Crew Lockers.",),
    "Galley": Room(name="Galley",
        description="A room with small kitchen and dinner table, some sofas",),
    "CrewLockers": Room(name="Crew Lockers",
        description="A room with small kitchen and dinner table, some sofas",),
    "Deck4MidAftPassage": Room(name="Deck 4 Mid-Aft Passage",
        description="A passage connecting Act 1 and Act 2",)
}

CryoBay = initial_rooms["CryoBay"]
CryoVestibule = initial_rooms["CryoVestibule"]
Galley = initial_rooms["Galley"]
CrewLockers = initial_rooms["CrewLockers"]
Deck4MidAftPassage = initial_rooms["Deck4MidAftPassage"]


def connect_all_initial_rooms():
    CryoBay.forward = CryoVestibule

    CryoVestibule.backward = CryoBay
    CryoVestibule.left = Galley
    CryoVestibule.right = CrewLockers

    Galley.forward = Deck4MidAftPassage
    Galley.backward = CryoVestibule

    CrewLockers.backward = CryoVestibule


def c_text_for_all_initial_rooms():
    CryoBay.on_first_enter = "This is your first time here"

    CryoVestibule.on_first_enter = "You have entered CryoVestibule"

def create_final_rooms():
    connect_all_initial_rooms()
    c_text_for_all_initial_rooms()

create_final_rooms()


## Items

items = {
    "Backpack": Item(name="Backpack", 
        description="Brown utility backpack",
        on_look="is a durable, brown canvas backpack, clearly built for field utility rather than comfort."),
     "Radio": Item(name="Radio", 
        description="Radio broken down",),
     "MaintenanceJack": Item(name="MaintenanceJack", 
        description="Medium sized maintenance tool for turning things",)   
}

interactables = {
    "MessHallBlastDoor": Interactables(name="MessHallBlastDoor", 
        description="Act 1 Broken down door, open with jack",
        on_look="You observe the heavy metallic edge of the Blast Door. The emergency hydraulic bolts are partially retracted, but the frame is visibly seized and fused. There are no electronic panels or keypads visible; the mechanism appears to be locked purely by immense mechanical pressure. This is a job for focused, brute force."),
}