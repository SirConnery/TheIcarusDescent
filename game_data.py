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


def c_on_enter_text_for_all_initial_rooms():
    CryoBay.on_first_enter = "You awaken to silence… \nCold air brushes across your skin, prickling through the thin fabric of your long underwear and undershirt. As you sit up, a faint hiss of the cryochamber releasing the last of its frost escapes from beneath you. Soft, intermittent bleeps echo from the nearby computer panels, a quiet rhythm that pulses through the room. \n\nThe room around you glows faintly in shades of white and pale blue. Rows of cyan metallic cryochambers curve around a white central pillar, their surfaces lit by strips of neon light. The walls are padded with soft, white panels, and bulky computer screens are embedded between them, their glass dim and lifeless. \nEvery other chamber stands open and empty. \n\nMaybe the others awoke before you…"
    CryoVestibule.on_first_enter = "You have entered CryoVestibule"

def c_on_survey_text_for_all_initial_rooms():
    CryoBay.on_survey = "You awaken... You are lying down in some kind of cryochamber wearing noth-ing but long underwear and a thin shirt. You carefully get up and feel a soft sensation of cold air flowing on your skin. Around you see a mostly white room full of neon-blue metallic cryochambers arranged around a grayish central pil-lar. The walls look softly padded with white plates. Embedded on the walls are some bulky-looking computer screens. The other cryochambers are empty and their lids are raised. Maybe the others awoke before you?"
    

def initial_rooms_setup():
    connect_all_initial_rooms()
    c_on_enter_text_for_all_initial_rooms()
    c_on_survey_text_for_all_initial_rooms()

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

def interacted_test_terminal():
    print("You interacted with the test terminal")


# Interactables data

initial_interactables = {
    "CryoBayTerminal": Interactable(
        name="Cryo Bay Terminal",
        keywords=["terminal", "console", "terminal console", "cryo terminal"],
        description="Act 1 Broken down door, open with jack",
        on_look="The terminal console is dark and coated with condensation, its screen flickering with amber error codes.",
        on_interact=interacted_cryo_terminal
    ),
    "TestTerminal": Interactable(
        name="Test Terminal",
        keywords=["terminal", "console", "terminal console"],
        description="Testing",
        on_look="Test",
        on_interact=interacted_test_terminal
    ),
}

CryoBayTerminal = initial_interactables["CryoBayTerminal"]
TestTerminal = initial_interactables["TestTerminal"]

def initial_interactables_setup():
    CryoBay.interactables['CryoBayTerminal'] = CryoBayTerminal
    Galley.interactables['TestTerminal'] = TestTerminal


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


# Sceneries

sceneries = {}

def run_all_setups():
    initial_rooms_setup()
    initial_interactables_setup()

run_all_setups()