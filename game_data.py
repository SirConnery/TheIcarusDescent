from game_classes import Player, Room, Item, Interactable, UseTarget, Scenery

player = Player()

## Rooms

rooms = {
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
        description="Small room for cargo."),
    "deck_5_secure_pathway": Room(name="Deck 5 Secure Pathway",
        description="2 person pathway."),
    "service_access_hatchway": Room(name="Service Access Hatchway",
        description="Act 3 filler room."),
    "msc_1": Room(name="MSC1 Main Service Control 1",
        description="MSC Room 1 divided by mirror."),
    "msc_2": Room(name="MSC2 Main Service Control 2",
        description="MSC Room 2 divided by mirror. Alien encounter here."),
    "msc_2_b_storage_drums": Room(name="MSC2 Main Service Control 2 (behind power storage drums)",
        description="MSC Room 2 behind power storage drums."),
    "msc_2_b_console_desk": Room(name="MSC2 Main Service Control 2 (behind console desk)",
        description="MSC Room 2 behind console desk."),
    "msc_2_b_power_conduit": Room(name="MSC2 Main Service Control 2 (behind power conduit manifold)",
        description="MSC Room 2 behind power conduit manifold."),
    "msc_vent": Room(name="MSC2 Ventilation Shaft",
        description="MSC2 ventilation shaft."),
    "service_control_junction_5f": Room(name="Service Control Junction 5 F",
        description="The door before entering. Act 4."),
    "operations_distribution_crossover": Room(name="Operations Distribution Crossover",
        description="Act 4 starting corridor."),
    "operations_and_cargo_interlink": Room(name="Operations and Cargo Interlink",
        description="Act 4 corridor between cargo and bridge."),
    "cargo_bay_control_f": Room(name="Cargo Bay Control F",
        description="Act 4 cargo bay control overwatch room."),
    "external_ops_access_way": Room(name="External Ops Access Way",
        description="Act 4 corridor between cargo and bridge."),
    "eva_gear_lockers": Room(name="EVA Gear Lockers",
        description="Act 4 eva gear locker."),
    "central_utility_spine_5_f": Room(name="Central Utility Spine 5 F",
        description="Part of the middle ship spanning hallway."),
    "central_utility_spine_6_f": Room(name="Central Utility Spine 6 F",
        description="Part of the middle ship spanning hallway."),
    "deck_5_forward_muster_station": Room(name="Deck 5 Forward Muster Station",
        description="Large empty area meant for gathering and receiving urgent instructions."),
    "bridge": Room(name="Bridge",
        description="Ship bridge."),
    "systems_data_access_corridor": Room(name="Systems Data Access Corridor",
        description="Corridor before Server Array."),''
    "command_server_array": Room(name="Command Server Array",
        description="Ship network and system control data central."),
    "executive_access_aisle": Room(name="Executive Access Aisle.",
        description="Ship network and system control data central."),
    "captains_quarters": Room(name="Captain's Quarters.",
        description="Living place for the captain."),
    "command_transit_vestibule": Room(name="Command Transit Vestibule",
        description="Stairway connecting to deck_5_forward_muster_station."),

}

# Act 1
cryo_bay = rooms["cryo_bay"]
cryo_vestibule = rooms["cryo_vestibule"]
galley = rooms["galley"]
crew_lockers = rooms["crew_lockers"]
deck_4_mid_aft_passage = rooms["deck_4_mid_aft_passage"]
# Act 2
deck_4_med_env_corridor = rooms["deck_4_med_env_corridor"]
medical_labs = rooms["medical_labs"]
environmental_controls = rooms["environmental_controls"]
upper_aft_lobby = rooms["upper_aft_lobby"]
central_freight_bay = rooms["central_freight_bay"]
deck_5_aft_utility = rooms["deck_5_aft_utility"]
# Act 3
cargo_staging_room = rooms["cargo_staging_room"]
deck_5_secure_pathway = rooms["deck_5_secure_pathway"]
service_access_hatchway = rooms["service_access_hatchway"]
msc_1 = rooms["msc_1"]
msc_2 = rooms["msc_2"]
msc_2_b_storage_drums = rooms["msc_2_b_storage_drums"]
msc_2_b_console_desk = rooms["msc_2_b_console_desk"]
msc_2_b_power_conduit = rooms["msc_2_b_power_conduit"]
msc_vent = rooms["msc_vent"]
service_control_junction_5f = rooms["service_control_junction_5f"]
# Act 4
operations_distribution_crossover = rooms["operations_distribution_crossover"]
operations_and_cargo_interlink = rooms["operations_and_cargo_interlink"]
cargo_bay_control_f = rooms["cargo_bay_control_f"]
external_ops_access_way = rooms["external_ops_access_way"]
eva_gear_lockers = rooms["eva_gear_lockers"]
central_utility_spine_5_f = rooms["central_utility_spine_5_f"]
central_utility_spine_6_f = rooms["central_utility_spine_6_f"]
deck_5_forward_muster_station = rooms["deck_5_forward_muster_station"]
bridge = rooms["bridge"]
systems_data_access_corridor = rooms["systems_data_access_corridor"]
command_server_array = rooms["command_server_array"]
executive_access_aisle = rooms["executive_access_aisle"]
captains_quarters = rooms["captains_quarters"]
command_transit_vestibule = rooms["command_transit_vestibule"]


## Room custom events

#Act 1
def crew_lockers_event():
    player.take("backpack")
    player.take("radio")

#Act 4
def act_4_lock_starting_door():
    service_control_junction_5f.is_open = False
    service_control_junction_5f.locked_description = "There is no reason to go back with that thing roaming there..."


## Connect rooms

def connect_all_initial_rooms():
    #Act 1
    cryo_bay.forward = cryo_vestibule
    cryo_vestibule.left = galley
    cryo_vestibule.right = crew_lockers
    cryo_vestibule.backward = cryo_bay
    galley.forward = deck_4_mid_aft_passage
    galley.right = cryo_vestibule
    crew_lockers.left = cryo_vestibule
    deck_4_mid_aft_passage.forward = deck_4_med_env_corridor
    deck_4_mid_aft_passage.backward = galley
    # Act 2
    deck_4_med_env_corridor.forward = upper_aft_lobby
    deck_4_med_env_corridor.left = medical_labs
    deck_4_med_env_corridor.right = environmental_controls
    medical_labs.right = deck_4_med_env_corridor
    environmental_controls.left = deck_4_med_env_corridor
    upper_aft_lobby.left = central_freight_bay
    upper_aft_lobby.right = deck_5_aft_utility
    upper_aft_lobby.backward = deck_4_med_env_corridor
    central_freight_bay.right = cargo_staging_room
    central_freight_bay.backward = upper_aft_lobby
    deck_5_aft_utility.backward = upper_aft_lobby
    # Act 3
    cargo_staging_room.right = deck_5_secure_pathway
    deck_5_secure_pathway.forward = service_access_hatchway
    service_access_hatchway.right = msc_1
    msc_1.forward = msc_2
    msc_2.left = msc_2_b_storage_drums
    msc_2.right = msc_2_b_console_desk
    msc_2.forward = msc_2_b_power_conduit
    msc_2_b_storage_drums.backward = msc_vent
    msc_2_b_console_desk.backward = msc_vent
    msc_2_b_power_conduit.backward = msc_vent
    msc_vent.forward = service_control_junction_5f
    service_control_junction_5f.forward = operations_distribution_crossover
    # Act 4
    operations_distribution_crossover.left = operations_and_cargo_interlink
    operations_distribution_crossover.right = systems_data_access_corridor
    operations_distribution_crossover.forward = central_utility_spine_5_f
    operations_distribution_crossover.backward = service_control_junction_5f
    operations_and_cargo_interlink.left = cargo_bay_control_f
    cargo_bay_control_f.right = operations_and_cargo_interlink
    operations_and_cargo_interlink.forward = external_ops_access_way
    operations_and_cargo_interlink.backward = operations_distribution_crossover
    external_ops_access_way.forward = eva_gear_lockers
    external_ops_access_way.right = central_utility_spine_6_f
    external_ops_access_way.backward = operations_and_cargo_interlink
    eva_gear_lockers.backward = external_ops_access_way
    central_utility_spine_5_f.forward = central_utility_spine_6_f
    central_utility_spine_5_f.backward = operations_distribution_crossover
    central_utility_spine_6_f.forward = deck_5_forward_muster_station
    central_utility_spine_6_f.backward = operations_distribution_crossover
    deck_5_forward_muster_station.left = external_ops_access_way
    deck_5_forward_muster_station.right = command_transit_vestibule
    deck_5_forward_muster_station.forward = bridge
    deck_5_forward_muster_station.backward = central_utility_spine_6_f
    bridge.backward = deck_5_forward_muster_station
    systems_data_access_corridor.left = operations_distribution_crossover
    systems_data_access_corridor.right = command_server_array
    systems_data_access_corridor.forward = executive_access_aisle
    command_server_array.left = systems_data_access_corridor
    executive_access_aisle.right = captains_quarters
    executive_access_aisle.forward = command_transit_vestibule 
    executive_access_aisle.backward = systems_data_access_corridor
    captains_quarters.left = executive_access_aisle
    command_transit_vestibule.left = deck_5_forward_muster_station
    command_transit_vestibule.backward = executive_access_aisle



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
    environmental_controls.on_revisit = "You enter the keycode and move in. The machines in the room make a continuous soft humming sound that is somehow soothing."
    environmental_controls.is_open = False
    environmental_controls.locked_description = "The door to Environmental Controls remains sealed. The access panel glows faintly, waiting for a valid code. No amount of pressing or swiping seems to budge it."
    upper_aft_lobby.on_first_enter = "You've never been here before."
    upper_aft_lobby.on_revisit = "You're back."
    central_freight_bay.on_first_enter = "You've never been here before."
    central_freight_bay.on_revisit = "You're back."
    central_freight_bay.is_open = False
    central_freight_bay.locked_description = "The door refuses to budge. Its surface is cold and unyielding, and the panel to the side is jammed tight. Whatever shut it down, it won’t open by hand. You’ll need another way in"
    deck_5_aft_utility.on_first_enter = "You've never been here before."
    deck_5_aft_utility.on_revisit = "You're back."
    # Act 3
    cargo_staging_room.on_first_enter = "The door closes behind you and suddenly the power comes on."
    cargo_staging_room.on_revisit = "You're back."
    cargo_staging_room.is_act_event_trigger = True
    cargo_staging_room.act_number = "3"
    cargo_staging_room.act_subtitle = "Arrival"
    deck_5_secure_pathway.on_first_enter = "You've never been here before."
    deck_5_secure_pathway.on_revisit = "You're back."
    service_access_hatchway.on_first_enter = "You've never been here before."
    service_access_hatchway.on_revisit = "You're back."
    msc_1.on_first_enter = "You've never been here before."
    msc_1.on_revisit = "You're back."
    msc_2.on_first_enter = f"The heavy operator console is bolted to the floor. Beneath it, a cramped crawlspace is barely visible, filled with exposed wiring and discarded ties. It offers just enough shadow and clearance for you to squeeze out of sight.\n\nThe Power Conduit Manifold is a dense, metallic structure where power lines converge. A narrow, dark pocket of shadow exists behind the thick bundles of cables near the floor. You could squeeze into the space.\n\n A cluster of heavy industrial drums, labeled with faded biohazard symbols, stands near the reinforced wall. They are secured with thick polymer bands, leaving a narrow, dark crevice between them and the wall."
    msc_2.on_revisit = "You're back."
    msc_2_b_storage_drums.on_first_enter = "You've never been here before."
    msc_2_b_storage_drums.on_revisit = "You're back."
    msc_2_b_console_desk.on_first_enter = "You've never been here before."
    msc_2_b_console_desk.on_revisit = "You're back."
    msc_2_b_power_conduit.on_first_enter = "You've never been here before."
    msc_2_b_power_conduit.on_revisit = "You're back."
    msc_vent.on_first_enter = "You've never been here before."
    msc_vent.on_revisit = "You're back."
    service_control_junction_5f.on_first_enter = "You've never been here before."
    service_control_junction_5f.on_revisit = "You're back."
    # Act 4
    operations_distribution_crossover.on_first_enter = "You've never been here before."
    operations_distribution_crossover.on_revisit = "You're back."
    operations_distribution_crossover.is_event_trigger = True
    operations_distribution_crossover.room_event = act_4_lock_starting_door
    operations_distribution_crossover.is_act_event_trigger = True
    operations_distribution_crossover.act_number = "4"
    operations_distribution_crossover.act_subtitle = "The Outer Decks"
    operations_and_cargo_interlink.on_first_enter = "You've never been here before."
    operations_and_cargo_interlink.on_revisit = "You're back."
    cargo_bay_control_f.on_first_enter = "You've never been here before."
    cargo_bay_control_f.on_revisit = "You're back."
    external_ops_access_way.on_first_enter = "You've never been here before."
    external_ops_access_way.on_revisit = "You're back."
    eva_gear_lockers.on_first_enter = "You've never been here before."
    eva_gear_lockers.on_revisit = "You're back."
    central_utility_spine_5_f.on_first_enter = "You've never been here before."
    central_utility_spine_5_f.on_revisit = "You're back."
    central_utility_spine_6_f.on_first_enter = "You've never been here before."
    central_utility_spine_6_f.on_revisit = "You're back."
    deck_5_forward_muster_station.on_first_enter = "You've never been here before."
    deck_5_forward_muster_station.on_revisit = "You're back."
    bridge.on_first_enter = "You've never been here before."
    bridge.on_revisit = "You're back."
    systems_data_access_corridor.on_first_enter = "You've never been here before."
    systems_data_access_corridor.on_revisit = "You're back."
    command_server_array.on_first_enter = "You've never been here before."
    command_server_array.on_revisit = "You're back."
    executive_access_aisle.on_first_enter = "You've never been here before."
    executive_access_aisle.on_revisit = "You're back."
    captains_quarters.on_first_enter = "You've never been here before."
    captains_quarters.on_revisit = "You're back."
    command_transit_vestibule.on_first_enter = "You've never been here before."
    command_transit_vestibule.on_revisit = "You're back."


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
    "engys_keycard": Item(name="Engy's Keycard", keywords = ["keycard", "card", "key", "engy"],
        description="High Engineer Enrique's keycard.",),
    "flashlight": Item(name="Flashlight", keywords = ["flashlight", "light", "flash"],
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
    crew_lockers.items["backpack"] = backpack
    crew_lockers.items["maintenance_jack"] = maintenance_jack
    crew_lockers.items["radio"] = radio
    # Act 2
    medical_labs.items["engys_keycard"] = engys_keycard
    environmental_controls.items["flashlight"] = flashlight
    deck_5_aft_utility.items["welder"] = welder

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
    cryo_bay.interactables["cryo_bay_terminal"] = cryo_bay_terminal


## use_targets functions

def mess_hall_blast_door_used():
    player.output = "Mess hall blast door used"
    deck_4_mid_aft_passage.is_open = True
def central_freight_bay_blast_door_used():
    player.output = "Freight bay blast door used"
    central_freight_bay.is_open = True
def env_controls_access_panel_use_keypad():
    passcode = input("Keycard detected. Please enter passcode")
    if passcode == "4277":
        player.output="Code verified. Access granted."
        environmental_controls.is_open = True
    else:
        player.output_error="Code invalid. Access denied."

# use_targets data

initial_use_targets = {
    "mess_hall_blast_door": UseTarget(name="Mess Hall Blast Door",
        keywords = ["door", "blast door", "blastdoor", "broken door", "broken down door"],
        description="Act 1 Broken down door, open with jack",
        on_look="You observe the heavy metallic edge of the Blast Door. The emergency hydraulic bolts are partially retracted, but the frame is visibly seized and fused. There are no electronic panels or keypads visible; the mechanism appears to be locked purely by immense mechanical pressure. This is a job for focused, brute force.",
        use_func=mess_hall_blast_door_used),
    "env_controls_access_panel": UseTarget(name="Environmental Control Access Panel",
        keywords = ["access panel", "panel", "keypad", "keypanel", "console", "terminal", "security", "keylogger"],
        description="Act 2 keypad to Environmental Controls.",
        on_look="A compact keypad and card swipe terminal connected to the ship’s security network. Its small green display sits blank, awaiting input.",
        use_func=env_controls_access_panel_use_keypad),
    "central_freight_bay_bulk_door": UseTarget(name="Central Freight Bay Bulk Door",
        keywords = ["door", "blast door", "blastdoor", "broken door", "broken down door"],
        description="Act 2 Broken down door, open with welder",
        on_look="The central freight bay door sits sealed and unyielding. \nA narrow panel clings to its side, warped and jammed, its edges surprisingly thin against the massive door. \n\nInside, you can just make out a tangle of rods and mechanisms. There must be some way to override the locks, if you can reach them. \n\nWhatever caused the door to fail, it won’t budge without a careful approach.",
        use_func=central_freight_bay_blast_door_used),
}

mess_hall_blast_door = initial_use_targets["mess_hall_blast_door"]
env_controls_access_panel = initial_use_targets["env_controls_access_panel"]
central_freight_bay_bulk_door = initial_use_targets["central_freight_bay_bulk_door"]

def initial_use_targets_setup():
    galley.use_targets["mess_hall_blast_door"] = mess_hall_blast_door
    deck_4_med_env_corridor.use_targets["env_controls_access_panel"] = env_controls_access_panel
    upper_aft_lobby.use_targets["central_freight_bay_bulk_door"] = central_freight_bay_bulk_door

def setup_usable_items():
    mess_hall_blast_door.usable_items["maintenance_jack"] = maintenance_jack
    env_controls_access_panel.usable_items["engys_keycard"] = engys_keycard
    central_freight_bay_bulk_door.usable_items["welder"] = welder

# Sceneries

sceneries = {}

## Run all necessary setups

def run_all_setups():
    initial_rooms_setup()
    initial_interactables_setup()
    initial_items_setup()
    initial_use_targets_setup()
    setup_usable_items()

run_all_setups()