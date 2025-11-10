from game_classes import Player, Room, Item, Interactable, UseTarget, Scenery

player = Player()

## Rooms

initial_rooms = {
    "cryo_bay": Room(name="Cryo Bay", 
        description="It is a room with cryo stuff.",),
    "cryo_vestibule": Room(name="Cryo Vestibule",
        description="It is a vestibule connecting CryoBay, Mess Hall and Crew Lockers.",),
    "galley": Room(name="Galley",
        description="A room with small kitchen and dinner table, some sofas",),
    "crew_lockers": Room(name="Crew Lockers",
        description="A room with small kitchen and dinner table, some sofas",),
    "deck_4_mid_aft_passage": Room(name="Deck 4 Mid-Aft Passage",
        description="A passage connecting Act 1 and Act 2"),
    "deck_4_med_env_corridor": Room(name="Deck 4 Med-Env Corridor",
        description="Start of Act 2."),
    "medical_labs": Room(name="Medical Labs",
        description="Medical laboratory where you find a keycard"),
    "environmental_controls": Room(name="Environmental Controls",
        description="Needs passcode. Find flashlight."),
    "upper_aft_lobby": Room(name="Upper Aft Lobby",
        description="Connecting room to cargo and utility."),
    "central_freight_bay": Room(name="Central Freight Bay",
        description="Massive cargo bay."),
    "deck_5_aft_utility": Room(name="Deck 5 Aft Utility",
        description="Small utility room."),
    "cargo_staging_room": Room(name="Cargo Staging Room",
        description="Small room for cargo.")
}

# Act 1
cryo_bay = initial_rooms["cryo_bay"]
cryo_vestibule = initial_rooms["cryo_vestibule"]
galley = initial_rooms["galley"]
crew_lockers = initial_rooms["crew_lockers"]
deck_4_mid_aft_passage = initial_rooms["deck_4_mid_aft_passage"]
# Act 2
deck_4_med_env_corridor = initial_rooms["deck_4_med_env_corridor"]
medical_labs = initial_rooms["medical_labs"]
environmental_controls = initial_rooms["environmental_controls"]
upper_aft_lobby = initial_rooms["upper_aft_lobby"]
central_freight_bay = initial_rooms["central_freight_bay"]
deck_5_aft_utility = initial_rooms["deck_5_aft_utility"]
# Act 3
cargo_staging_room = initial_rooms["cargo_staging_room"]


# Room custom events

def crew_lockers_event():
    player.take("backpack")
    player.take("radio")
    

def connect_all_initial_rooms():
    #Act 1
    cryo_bay.forward = cryo_vestibule
    cryo_vestibule.left = galley
    cryo_vestibule.right = crew_lockers
    cryo_vestibule.backward = cryo_bay
    galley.forward = deck_4_mid_aft_passage
    galley.backward = cryo_vestibule
    crew_lockers.backward = cryo_vestibule
    deck_4_mid_aft_passage.forward = deck_4_med_env_corridor
    deck_4_mid_aft_passage.backward = galley
    # Act 2
    deck_4_med_env_corridor.forward = upper_aft_lobby
    deck_4_med_env_corridor.left = medical_labs
    deck_4_med_env_corridor.right = environmental_controls
    medical_labs.backward = deck_4_med_env_corridor
    environmental_controls.backward = deck_4_med_env_corridor
    upper_aft_lobby.left = central_freight_bay
    upper_aft_lobby.right = deck_5_aft_utility
    central_freight_bay.right = cargo_staging_room
    central_freight_bay.backward = upper_aft_lobby
    deck_5_aft_utility.backward = upper_aft_lobby
    # Act 3
    cargo_staging_room



def set_rooms_defaults():
    # Act 1
    cryo_bay.on_first_enter = "\n\nYou awaken to silence… \n\nCold air brushes across your skin, prickling through the thin fabric of your long underwear and undershirt. As you sit up, a faint hiss of the cryochamber releasing the last of its frost escapes from beneath you. Soft, intermittent bleeps echo from the nearby computer panels, a quiet rhythm that pulses through the room. \n\nThe room around you glows faintly in shades of white and pale blue. Rows of cyan metallic cryochambers curve around a white central pillar, their surfaces lit by strips of neon light. The walls are padded with soft, white panels, and bulky computer screens are embedded between them, their glass dim and lifeless. \nEvery other chamber stands open and empty. \n\nMaybe the others awoke before you…"
    cryo_bay.on_revisit = "The cryochamber lies silent, bathed in pale blue light. A lone terminal hums near the door.."
    cryo_bay.is_act_event_trigger = True
    cryo_bay.act_number = "1"
    cryo_bay.act_subtitle = "The Beginning"
    cryo_bay.on_survey = "You survey the room."
    cryo_vestibule.on_first_enter = "You've never been here before."
    cryo_vestibule.on_revisit = "You're back."
    galley.on_first_enter = "You've never been here before."
    galley.on_revisit = "You're back."
    crew_lockers.on_first_enter = "You've never been here before."
    crew_lockers.on_revisit = "You're back."
    crew_lockers.is_event_trigger = True
    crew_lockers.room_event = crew_lockers_event
    deck_4_mid_aft_passage.on_first_enter = "You've never been here before."
    deck_4_mid_aft_passage.on_revisit = "You're back."
    deck_4_mid_aft_passage.is_open = False
    deck_4_mid_aft_passage.locked_description = "The Blast Door resists every push; its frame is fused and bolted tight. Only raw, focused force could budge it"
    # Act 2
    deck_4_med_env_corridor.on_first_enter = "You've never been here before."
    deck_4_med_env_corridor.on_revisit = "You're back."
    deck_4_med_env_corridor.is_act_event_trigger = True
    deck_4_med_env_corridor.act_number = "2"
    deck_4_med_env_corridor.act_subtitle = "Beneath the Darkness"
    medical_labs.on_first_enter = "You've never been here before."
    medical_labs.on_revisit = "You're back."
    environmental_controls.on_first_enter = "You've never been here before."
    environmental_controls.on_revisit = "You're back."
    upper_aft_lobby.on_first_enter = "You've never been here before."
    upper_aft_lobby.on_revisit = "You're back."
    central_freight_bay.on_first_enter = "You've never been here before."
    central_freight_bay.on_revisit = "You're back."
    deck_5_aft_utility.on_first_enter = "You've never been here before."
    deck_5_aft_utility.on_revisit = "You're back."
    # Act 3
    cargo_staging_room.on_first_enter = "You've never been here before."
    cargo_staging_room.on_revisit = "You're back."
    cargo_staging_room.is_act_event_trigger = True
    cargo_staging_room.act_number = "3"
    cargo_staging_room.act_subtitle = "Arrival"
    


def initial_rooms_setup():
    connect_all_initial_rooms()
    set_rooms_defaults()

## Items

initial_items = {
    "backpack": Item(name="Backpack", keywords = ["backpack", "pack", "bag"],
        description="Brown utility backpack",
        on_look="It is a durable, brown canvas backpack, clearly built for field utility rather than comfort."),
    "radio": Item(name="Radio", keywords = ["radio"],
        description="Radio broken down",),
    "maintenance_jack": Item(name="Maintenance Jack", keywords = ["maintenance jack", "jack", "maintenancejack"],
        description="Medium sized maintenance tool for turning things",),
    "engys_keycard": Item(name="Engy's Keycard", keywords = ["keycard, card, key, engy"],
        description="High Engineer Enrique's keycard.",),
    "flashlight": Item(name="Flashlight", keywords = ["flashlight, light, flash"],
        description="Small non-industrial handheld flashlight with low cone of light.",),
    "welder": Item(name="Welder", keywords = ["welder"],
        description="Hand usable welder.",),
}

backpack = initial_items["backpack"]
radio = initial_items["radio"]
maintenance_jack = initial_items["maintenance_jack"]
engys_keycard = initial_items["engys_keycard"]
flashlight = initial_items["flashlight"]
welder = initial_items["welder"]


def initial_items_setup():
    # Act 1
    crew_lockers.items['backpack'] = backpack
    crew_lockers.items['maintenance_jack'] = maintenance_jack
    crew_lockers.items['radio'] = radio
    # Act 2
    medical_labs.items['engys_keycard'] = engys_keycard
    environmental_controls.items['flashlight'] = flashlight
    deck_5_aft_utility.items['welder'] = welder

# Interactables functions

def interacted_cryo_terminal():
    player.output="You interacted with the cryo terminal"

# Interactables data

initial_interactables = {
    "cryo_bay_terminal": Interactable(
        name="Cryo Bay Terminal",
        keywords=["terminal", "console", "terminal console", "cryo terminal"],
        description="Act 1 Broken down door, open with jack",
        on_look="The terminal console is dark, its screen glowing softly with amber readouts that pulse in quiet rhythm.",
        on_interact=interacted_cryo_terminal
    ),
}

cryo_bay_terminal = initial_interactables["cryo_bay_terminal"]

def initial_interactables_setup():
    cryo_bay.interactables['cryo_bay_terminal'] = cryo_bay_terminal


# use_targets functions
def mess_hall_blast_door_used():
    player.output = "Mess hall blast door used"
    deck_4_mid_aft_passage.is_open = True

# use_targets data

initial_use_targets = {
    "mess_hall_blast_door": UseTarget(name="Mess Hall Blast Door",
        keywords = ["door", "blast door", "blastdoor", "broken door", "broken down door"],
        description="Act 1 Broken down door, open with jack",
        on_look="You observe the heavy metallic edge of the Blast Door. The emergency hydraulic bolts are partially retracted, but the frame is visibly seized and fused. There are no electronic panels or keypads visible; the mechanism appears to be locked purely by immense mechanical pressure. This is a job for focused, brute force.",
        use_func=mess_hall_blast_door_used),
}

mess_hall_blast_door = initial_use_targets["mess_hall_blast_door"]

def initial_use_targets_setup():
    galley.use_targets['mess_hall_blast_door'] = mess_hall_blast_door

def initial_use_targets_dicts_setup():
    mess_hall_blast_door.usable_items['maintenance_jack'] = maintenance_jack

# Sceneries

sceneries = {}

def run_all_setups():
    initial_rooms_setup()
    initial_interactables_setup()
    initial_items_setup()
    initial_use_targets_setup()
    initial_use_targets_dicts_setup()

run_all_setups()