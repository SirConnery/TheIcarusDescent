from game_classes import Room, Item, Interactable, UseTarget, Scenery

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

def initial_rooms_setup():
    connect_all_initial_rooms()
    c_text_for_all_initial_rooms()

def add_object_keywords_to_room():
    pass

## Items

initial_items = {
    "Backpack": Item(name="Backpack", keywords = ["backpack", "pack", "bag"],
        description="Brown utility backpack",
        on_look="is a durable, brown canvas backpack, clearly built for field utility rather than comfort."),
     "Radio": Item(name="Radio", keywords = ["radio"],
        description="Radio broken down",),
     "MaintenanceJack": Item(name="Maintenance Jack", keywords = ["maintenance jack", "jack", "maintenancejack"],
        description="Medium sized maintenance tool for turning things",)   
}


# Interactables functions

def interacted_cryo_terminal():
    print("You interacted with the cryo terminal")

# Interactables data

initial_interactables = {
    "CryoBayTerminal": Interactable(name="Cryo Bay Terminal,",
        keywords = ["terminal", "console", "terminal console", "cryo terminal"],
        description="Act 1 Broken down door, open with jack",
        on_look="The terminal console is dark and coated with a thin layer of condensation, its screen flickering with amber error codes.",
        on_interact=interacted_cryo_terminal),
}

CryoBayTerminal = initial_interactables["CryoBayTerminal"]

def initial_interactables_setup():
    CryoBay.interactables['CryoBayTerminal'] = CryoBayTerminal

# use_targets functions
def mess_hall_blast_door_used():
    print("Mess hall blast door used")

# use_targets data

initial_use_targets = {
    "MessHallBlastDoor": UseTarget(name="MessHallBlastDoor",
        keywords = ["door", "blast door", "blastdoor", "broken door", "broken down door"],
        description="Act 1 Broken down door, open with jack",
        on_look="You observe the heavy metallic edge of the Blast Door. The emergency hydraulic bolts are partially retracted, but the frame is visibly seized and fused. There are no electronic panels or keypads visible; the mechanism appears to be locked purely by immense mechanical pressure. This is a job for focused, brute force.",
        on_use=mess_hall_blast_door_used),
}

MessHallBlastDoor = initial_use_targets["MessHallBlastDoor"]

def initial_use_targets_setup():
    Galley.use_targets['MessHallBlastDoor'] = MessHallBlastDoor

sceneries = {}


def run_all_setups():
    initial_rooms_setup()
    initial_interactables_setup()
    build_key_list(initial_items)

keyword_map = {}

def build_key_list(item_list):
    temp_keywords = {}

    for item in item_list:
        temp_keywords[]


    global keyword_map
    keyword_map = temp_keywords




run_all_setups()