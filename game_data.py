from game_classes import Player, NPC, Room, Item, Interactable, UseTarget, Scenery
from npc_data import engy, chef, tanaka, arachnid
player = Player()


## Rooms

rooms = {
    "cryo_bay": Room(name="Cryo Bay", 
        debug_info="It is a room with cryo stuff.",),
    "cryo_vestibule": Room(name="Cryo Vestibule",
        debug_info="It is a vestibule connecting CryoBay, Mess Hall and Crew Lockers.",),
    "galley": Room(name="Galley",
        debug_info="A room with small kitchen and dinner table, some sofas",),
    "crew_lockers": Room(name="Crew Lockers",
        debug_info="A room with small kitchen and dinner table, some sofas",),
    "deck_4_mid_aft_passage": Room(name="Deck 4 Mid-Aft Passage",
        debug_info="A passage connecting Act 1 and Act 2"),
    "deck_4_med_env_corridor": Room(name="Deck 4 Med-Env Corridor",
        debug_info="Start of Act 2."),
    "medical_labs": Room(name="Medical Labs",
        debug_info="Medical laboratory where you find a keycard"),
    "environmental_controls": Room(name="Environmental Controls",
        debug_info="Needs passcode. Find flashlight."),
    "upper_aft_lobby": Room(name="Upper Aft Lobby",
        debug_info="Connecting room to cargo and utility."),
    "central_freight_bay": Room(name="Central Freight Bay",
        debug_info="Massive cargo bay."),
    "deck_5_aft_utility": Room(name="Deck 5 Aft Utility",
        debug_info="Small utility room."),
    "cargo_staging_room": Room(name="Cargo Staging Room",
        debug_info="Small room for cargo."),
    "deck_5_secure_pathway": Room(name="Deck 5 Secure Pathway",
        debug_info="2 person pathway."),
    "service_access_hatchway": Room(name="Service Access Hatchway",
        debug_info="Act 3 filler room."),
    "msc_1": Room(name="MSC1 Main Service Control 1",
        debug_info="MSC Room 1 divided by mirror."),
    "msc_2": Room(name="MSC2 Main Service Control 2",
        debug_info="MSC Room 2 divided by mirror. Alien encounter here."),
    "msc_2_b_storage_drums": Room(name="MSC2 Main Service Control 2 (behind power storage drums)",
        debug_info="MSC Room 2 behind power storage drums."),
    "msc_2_b_console_desk": Room(name="MSC2 Main Service Control 2 (behind console desk)",
        debug_info="MSC Room 2 behind console desk."),
    "msc_2_b_power_conduit": Room(name="MSC2 Main Service Control 2 (behind power conduit manifold)",
        debug_info="MSC Room 2 behind power conduit manifold."),
    "msc_vent": Room(name="MSC2 Ventilation Shaft",
        debug_info="MSC2 ventilation shaft."),
    "service_control_junction_5f": Room(name="Service Control Junction 5 F",
        debug_info="The door before entering. Act 4."),
    "operations_distribution_crossover": Room(name="Operations Distribution Crossover",
        debug_info="Act 4 starting corridor."),
    "operations_and_cargo_interlink": Room(name="Operations and Cargo Interlink",
        debug_info="Act 4 corridor between cargo and bridge."),
    "cargo_bay_control_f": Room(name="Cargo Bay Control F",
        debug_info="Act 4 cargo bay control overwatch room."),
    "external_ops_access_way": Room(name="External Ops Access Way",
        debug_info="Act 4 corridor between cargo and bridge."),
    "eva_gear_lockers": Room(name="EVA Gear Lockers",
        debug_info="Act 4 eva gear locker."),
    "central_utility_spine_5_f": Room(name="Central Utility Spine 5 F",
        debug_info="Part of the middle ship spanning hallway."),
    "central_utility_spine_4_f": Room(name="Central Utility Spine 4 F",
        debug_info="This door is broken and the room cannot be accessed."),
    "central_utility_spine_6_f": Room(name="Central Utility Spine 6 F",
        debug_info="Part of the middle ship spanning hallway."),
    "deck_5_forward_muster_station": Room(name="Deck 5 Forward Muster Station",
        debug_info="Large empty area meant for gathering and receiving urgent instructions."),
    "bridge": Room(name="Bridge",
        debug_info="Ship bridge."),
    "systems_data_crossover": Room(name="Systems Data Crossover",
        debug_info="Corridor before Systems Data Access Corridor."),
    "systems_data_access_corridor": Room(name="Systems Data Access Corridor",
        debug_info="Corridor before Server Array."),
    "data_server_array": Room(name="Data Server Array",
        debug_info="Ship network and system control data central."),
    "executive_access_aisle": Room(name="Executive Access Aisle.",
        debug_info="Ship network and system control data central."),
    "captains_quarters": Room(name="Captain's Quarters.",
        debug_info="Living place for the captain."),
    "command_transit_vestibule": Room(name="Command Transit Vestibule",
        debug_info="Stairway connecting to deck_5_forward_muster_station."),
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
central_utility_spine_4_f = rooms["central_utility_spine_4_f"]
deck_5_forward_muster_station = rooms["deck_5_forward_muster_station"]
bridge = rooms["bridge"]
systems_data_crossover = rooms["systems_data_crossover"]
systems_data_access_corridor = rooms["systems_data_access_corridor"]
data_server_array = rooms["data_server_array"]
executive_access_aisle = rooms["executive_access_aisle"]
captains_quarters = rooms["captains_quarters"]
command_transit_vestibule = rooms["command_transit_vestibule"]


## Room custom events

# Act 1
def crew_lockers_event():
    player.take("backpack")
    player.take("radio")

# Act 4
def act_4_lock_starting_door():
    service_control_junction_5f.is_open = False
    service_control_junction_5f.locked_description = "There is no reason to go back with that thing roaming there..."

def meet_panicked_npc_executive_access_aisle():
    player.output_fast += f"Tanaka runs toward {systems_data_access_corridor.name}."
    systems_data_access_corridor.is_event_trigger = True
    systems_data_access_corridor.room_event = meet_panicked_npc_systems_data_access_corridor

def meet_panicked_npc_systems_data_access_corridor():
    systems_data_crossover.is_event_trigger = True
    systems_data_crossover.room_event = meet_panicked_npc_systems_data_systems_crossover
    player.output_fast += f"Tanaka runs toward {systems_data_crossover.name}."

def meet_panicked_npc_systems_data_systems_crossover():
    central_utility_spine_5_f.is_event_trigger = True
    central_utility_spine_5_f.room_event = meet_panicked_npc_central_utility_spine_5_f
    player.output_fast += f"Tanaka runs toward {central_utility_spine_5_f.name}."

def meet_panicked_npc_central_utility_spine_5_f():
    operations_distribution_crossover.is_event_trigger = True
    operations_distribution_crossover.room_event = meet_panicked_npc_operations_distribution_crossover
    player.output_fast += f"Tanaka runs toward {operations_distribution_crossover.name}."

def meet_panicked_npc_operations_distribution_crossover():
    operations_distribution_crossover.items["lockpick"] = lockpick
    operations_distribution_crossover.on_survey = "This corridor is narrow and reinforced, designed for limited crew transit between the central spine and the external operation staging areas. The walls are smooth, and the overhead utilities are secured and caged.\n\n Lying just beside the rough, circular hole you previously cut into the access door, you spot a small, professional Lockpick Set glinting faintly. It must have fallen from Tanaka's belt in his haste to squeeze through the opening."
    player.output += "Tanaka don't go!"
    player.output_fast += f"\n\nTanaka runs toward operations distribution crossover."
    operations_distribution_crossover.items["lockpick"] = lockpick



## Connect rooms

def connect_all_initial_rooms():
    # Act 1
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
    operations_distribution_crossover.right = central_utility_spine_5_f
    operations_distribution_crossover.backward = service_control_junction_5f
    operations_and_cargo_interlink.left = cargo_bay_control_f
    cargo_bay_control_f.right = operations_and_cargo_interlink
    operations_and_cargo_interlink.right = operations_distribution_crossover
    operations_and_cargo_interlink.forward = external_ops_access_way
    external_ops_access_way.forward = eva_gear_lockers
    external_ops_access_way.right = central_utility_spine_6_f
    external_ops_access_way.backward = operations_and_cargo_interlink
    eva_gear_lockers.backward = external_ops_access_way
    central_utility_spine_5_f.left = operations_distribution_crossover
    central_utility_spine_5_f.right = systems_data_crossover
    central_utility_spine_5_f.forward = central_utility_spine_6_f
    central_utility_spine_5_f.backward = central_utility_spine_4_f
    central_utility_spine_6_f.left = external_ops_access_way
    central_utility_spine_6_f.forward = deck_5_forward_muster_station
    central_utility_spine_6_f.backward = central_utility_spine_5_f
    deck_5_forward_muster_station.left = external_ops_access_way
    deck_5_forward_muster_station.right = command_transit_vestibule
    deck_5_forward_muster_station.forward = bridge
    deck_5_forward_muster_station.backward = central_utility_spine_6_f
    bridge.backward = deck_5_forward_muster_station
    systems_data_crossover.left = central_utility_spine_5_f
    systems_data_crossover.forward = systems_data_access_corridor
    systems_data_access_corridor.right = data_server_array
    systems_data_access_corridor.forward = executive_access_aisle
    systems_data_access_corridor.backward = systems_data_crossover
    data_server_array.left = systems_data_access_corridor
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
    cryo_vestibule.on_survey = "You survey the room."
    galley.on_first_enter = "You've never been here before."
    galley.on_revisit = "You're back."
    galley.on_survey = "You survey the room."
    crew_lockers.on_first_enter = "You've never been here before."
    crew_lockers.on_revisit = "You're back."
    crew_lockers.on_survey = "You survey the room."
    crew_lockers.is_event_trigger = True
    crew_lockers.room_event = crew_lockers_event
    deck_4_mid_aft_passage.on_first_enter = "You've never been here before."
    deck_4_mid_aft_passage.on_revisit = "You're back."
    deck_4_mid_aft_passage.on_survey = "You survey the room."
    deck_4_mid_aft_passage.is_open = False
    deck_4_mid_aft_passage.locked_description = "The Blast Door resists every push; its frame is fused and bolted tight. Only raw, focused force could budge it"
    # Act 2
    deck_4_med_env_corridor.on_first_enter = "You've never been here before."
    deck_4_med_env_corridor.on_revisit = "You're back."
    deck_4_med_env_corridor.on_survey = "You survey the room."
    deck_4_med_env_corridor.is_act_event_trigger = True
    deck_4_med_env_corridor.act_number = "2"
    deck_4_med_env_corridor.act_subtitle = "Beneath the Darkness"
    medical_labs.on_first_enter = "You've never been here before."
    medical_labs.on_revisit = "You're back."
    medical_labs.on_survey = "You survey the room."
    environmental_controls.on_first_enter = "You've never been here before."
    environmental_controls.on_revisit = "You enter the keycode and move in. The machines in the room make a continuous soft humming sound that is somehow soothing."
    environmental_controls.on_survey = "You survey the room."
    environmental_controls.is_open = False
    environmental_controls.locked_description = "The door to Environmental Controls remains sealed. The access panel glows faintly, waiting for a valid code. No amount of pressing or swiping seems to budge it."
    upper_aft_lobby.on_first_enter = "You've never been here before."
    upper_aft_lobby.on_revisit = "You're back."
    upper_aft_lobby.on_survey = "You survey the room."
    central_freight_bay.on_first_enter = "You've never been here before."
    central_freight_bay.on_revisit = "You're back."
    central_freight_bay.on_survey = "You survey the room."
    central_freight_bay.is_open = False
    central_freight_bay.locked_description = "The door refuses to budge. Its surface is cold and unyielding, and the panel to the side is jammed tight. Whatever shut it down, it won’t open by hand. You’ll need another way in"
    deck_5_aft_utility.on_first_enter = "You've never been here before."
    deck_5_aft_utility.on_revisit = "You're back."
    deck_5_aft_utility.on_survey = "You survey the room."
    # Act 3
    cargo_staging_room.on_first_enter = "The door closes behind you and suddenly the power comes on."
    cargo_staging_room.on_revisit = "You're back."
    cargo_staging_room.on_survey = "You survey the room."
    cargo_staging_room.is_act_event_trigger = True
    cargo_staging_room.act_number = "3"
    cargo_staging_room.act_subtitle = "Arrival"
    deck_5_secure_pathway.on_first_enter = "You've never been here before."
    deck_5_secure_pathway.on_revisit = "You're back."
    deck_5_secure_pathway.on_survey = "You survey the room."
    service_access_hatchway.on_first_enter = "You've never been here before."
    service_access_hatchway.on_revisit = "You're back."
    service_access_hatchway.on_survey = "You survey the room."
    msc_1.on_first_enter = "You've never been here before."
    msc_1.on_revisit = "You're back."
    msc_1.on_survey = "You survey the room."
    msc_2.on_first_enter = f"The heavy operator console is bolted to the floor. Beneath it, a cramped crawlspace is barely visible, filled with exposed wiring and discarded ties. It offers just enough shadow and clearance for you to squeeze out of sight.\n\nThe Power Conduit Manifold is a dense, metallic structure where power lines converge. A narrow, dark pocket of shadow exists behind the thick bundles of cables near the floor. You could squeeze into the space.\n\n A cluster of heavy industrial drums, labeled with faded biohazard symbols, stands near the reinforced wall. They are secured with thick polymer bands, leaving a narrow, dark crevice between them and the wall."
    msc_2.on_revisit = "You're back."
    msc_2.on_survey = "You survey the room."
    msc_2_b_storage_drums.on_first_enter = "You've never been here before."
    msc_2_b_storage_drums.on_revisit = "You're back."
    msc_2_b_storage_drums.on_survey = "You survey the room."
    msc_2_b_console_desk.on_first_enter = "You've never been here before."
    msc_2_b_console_desk.on_revisit = "You're back."
    msc_2_b_console_desk.on_survey = "You survey the room."
    msc_2_b_power_conduit.on_first_enter = "You've never been here before."
    msc_2_b_power_conduit.on_revisit = "You're back."
    msc_2_b_power_conduit.on_survey = "You survey the room."
    msc_vent.on_first_enter = "You've never been here before."
    msc_vent.on_revisit = "You're back."
    msc_vent.on_survey = "You survey the room."
    service_control_junction_5f.on_first_enter = "You've never been here before."
    service_control_junction_5f.on_revisit = "You're back."
    service_control_junction_5f.on_survey = "You survey the room."
    # Act 4
    operations_distribution_crossover.on_first_enter = "You've never been here before."
    operations_distribution_crossover.on_revisit = "You're back."
    operations_distribution_crossover.on_survey = "You survey the room."
    operations_distribution_crossover.is_event_trigger = True
    operations_distribution_crossover.room_event = act_4_lock_starting_door
    operations_distribution_crossover.is_act_event_trigger = True
    operations_distribution_crossover.act_number = "4"
    operations_distribution_crossover.act_subtitle = "The Outer Decks"
    operations_and_cargo_interlink.on_first_enter = "This short, fortified corridor feels heavy and cold. The passage is dominated by three sealed doorways. To your left, a heavy security door has been completely destroyed, its metallic surface ripped and curled as if melted by immense, unnatural force. Right next to it, the door leading to Cargo Bay Control F remains intact but locked. Forward, a door leads to the External Ops Access Way. \n\nA small, specialized diagnostic console is mounted beside the Cargo Bay Control door, indicating the access system has failed and requires a unique technical bypass."
    operations_and_cargo_interlink.on_revisit = "You're back. The destroyed door remains untouched, and the Cargo Bay Control door is still sealed. The diagnostic console next to it is awaiting initiation."
    operations_and_cargo_interlink.on_survey = "This short, fortified corridor feels heavy and cold. The passage is dominated by three sealed doorways. \n\nTo your left, a heavy security door has been completely destroyed, its metallic surface ripped and curled as if melted by immense, unnatural force. Right next to it, the Cargo Bay Control F remains intact but locked.\n\n A small, specialized diagnostic console is mounted beside the Cargo Bay door, indicating the access system has failed and requires a unique technical bypass. \n\nForward, a door leads to the External Ops Access Way"
    cargo_bay_control_f.on_first_enter = ""
    cargo_bay_control_f.on_revisit = "You're back."
    cargo_bay_control_f.on_survey = "You survey the room."
    cargo_bay_control_f.is_open = False
    cargo_bay_control_f.locked_description = "The door doesn't budge. The console next to the door is awaiting input."
    external_ops_access_way.on_first_enter = "You've never been here before."
    external_ops_access_way.on_revisit = "You're back."
    external_ops_access_way.on_survey = "You survey the room."
    eva_gear_lockers.on_first_enter = "It is a narrow staging bay lined with helmet racks and storage units. Secured to the wall is a dark, electronic locker, and through its clear panel, you can clearly see the SART (Systems Repair and Analysis Tool) unit locked inside..\n\nThere is what appears to be a screwdriver on the floor."
    eva_gear_lockers.on_revisit = "The room's equipment racks are mostly empty, and the SART locker remains a central point of interest. There is a screwdriver on the floor."
    eva_gear_lockers.on_survey = "The room is quiet and unnervingly cold. It is dedicated to storing external mission gear, though most racks are now empty. A specialized maintenance board stands next to a tool chest, and you see a small, precision screwdriver set attached to it.\n\nSecured prominently on the wall is a dark, electronic locker with the SART (Systems Analysis and Repair Tool) unit clearly visible behind its sealed high security glass panel. Normally you would open it by using your attached token id on your radio. The locker is centrally connected to the data servers that controls id data."
    central_utility_spine_5_f.on_first_enter = "You've never been here before."
    central_utility_spine_5_f.on_revisit = "You're back."
    central_utility_spine_5_f.on_survey = "You survey the room."
    central_utility_spine_4_f.on_first_enter = "You've never been here before."
    central_utility_spine_4_f.on_revisit = "You're back."
    central_utility_spine_4_f.on_survey = "You survey the room."
    central_utility_spine_4_f.is_open = False
    central_utility_spine_4_f.locked_description = "This heavy access door is severely damaged. The metallic surface is battered and buckled, and the automated locking mechanism has been ripped from its housing. The door frame is twisted, ensuring the passage is permanently sealed by physical force. "
    central_utility_spine_6_f.on_first_enter = "You've never been here before."
    central_utility_spine_6_f.on_revisit = "You're back."
    central_utility_spine_6_f.on_survey = "You survey the room."
    deck_5_forward_muster_station.on_first_enter = "You've never been here before."
    deck_5_forward_muster_station.on_revisit = "You're back."
    deck_5_forward_muster_station.on_survey = "You survey the room."
    bridge.on_first_enter = "You've never been here before."
    bridge.on_revisit = "You're back."
    bridge.on_survey = "You survey the room."
    systems_data_crossover.on_first_enter = "You've never been here before."
    systems_data_crossover.on_revisit = "You're back."
    systems_data_crossover.on_survey = "You survey the room."
    systems_data_access_corridor.on_first_enter = "This narrow passage is lined with high-capacity data conduits, and the air feels cold and electrically charged. It seems the console that would let access the Data Server Array is fried. You have to get in somehow..."
    systems_data_access_corridor.on_revisit = "You are back. The Data Server Array door remains sealed.."
    systems_data_access_corridor.on_survey = "This narrow passage is lined with high-capacity data conduits, and the air feels cold and electrically charged. The electronic access console is completely fried: the panel is melted and blackened, emitting a faint smell of burnt ozone. The massive blast door is sealed shut, and the emergency mechanical lock beside it is seized. The door cannot be opened electronically. You will need a delicate tool to bypass the final internal lock tumblers."
    data_server_array.on_first_enter = "The room is loud and cold, dominated by the relentless hum of the primary cooling systems. Though the ceiling is low, dozens of silent, black server racks stretch across the wide room, many displaying flickering red diagnostic lights. The central ICARUS Systems Terminal stands alone in the center, waiting for input."
    data_server_array.on_revisit = "The room is loud, cold, and wide. The central ICARUS terminal remains active.."
    data_server_array.on_survey = "The room is loud and cold, dominated by the relentless hum of the primary cooling systems. Though the ceiling is low, dozens of silent, black server racks stretch across the wide room, many displaying flickering red diagnostic lights. The central ICARUS Systems Terminal stands alone in the center, waiting for input."
    data_server_array.is_open = False
    data_server_array.locked_description = "The door is locked as the electronic console that would let you in is completely fried.\n\nThe door's mechanical emergency lock looks fine though."
    executive_access_aisle.on_first_enter = "You've never been here before."
    executive_access_aisle.on_revisit = "You're back."
    executive_access_aisle.on_survey = "You survey the room."
    executive_access_aisle.is_event_trigger = True
    executive_access_aisle.room_event = meet_panicked_npc_executive_access_aisle
    captains_quarters.on_first_enter = "You've never been here before."
    captains_quarters.on_revisit = "You're back."
    captains_quarters.on_survey = "You survey the room."
    command_transit_vestibule.on_first_enter = "You've never been here before."
    command_transit_vestibule.on_revisit = "You're back."
    command_transit_vestibule.on_survey = "You survey the room."


def initial_rooms_setup():
    connect_all_initial_rooms()
    set_rooms_defaults()

## Items

initial_items = {
        "backpack": Item(
        id="backpack",
        name="Backpack",
        keywords=["backpack", "pack", "bag"],
        debug_info="Brown utility backpack",
        on_look="It is a durable, brown canvas backpack, clearly built for field utility rather than comfort."
    ),

    "radio": Item(
        id="radio",
        name="Radio",
        keywords=["radio"],
        debug_info="Radio broken down"
    ),

    "maintenance_jack": Item(
        id="maintenance_jack",
        name="Maintenance Jack",
        keywords=["maintenance jack", "jack", "maintenancejack"],
        debug_info="Medium sized maintenance tool for turning things"
    ),

    "engys_keycard": Item(
        id="engys_keycard",
        name="High Engineer Enrique's keycard.",
        keywords=["keycard", "card", "key", "engy"],
        debug_info="High Engineer Enrique's keycard."
    ),

    "flashlight": Item(
        id="flashlight",
        name="Flashlight",
        keywords=["flashlight", "light", "flash"],
        debug_info="Small non-industrial handheld flashlight with low cone of light."
    ),

    "welder": Item(
        id="welder",
        name="Welder",
        keywords=["welder"],
        debug_info="Hand usable welder."
    ),

    "lockpick": Item(
        id="lockpick",
        name="Lockpick",
        keywords=["lockpick", "key", "pick", "lock"],
        debug_info="Dropped lockpick by Tanaka. Opens Server Array."
    ),

    "screwdriver": Item(
        id="screwdriver",
        name="Screwdriver",
        keywords=["screwdriver", "screw", "driver"],
        debug_info="Screwdriver on the floor of EVA room."
    ),
    "sart": Item(
        id="sart",
        name="(SART) System Analysis and Repair Tool",
        keywords=["sart", "system", "analysis", "repair", "tool"],
        debug_info="System Analysis and Repair Tool.",
        on_look="It is the System Analysis and Repair Tool. Can be used for diagnostics, using and repairing consoles.",
        can_take=False,
        locked_description="It is locked behind a bulletproof glass panel with token identifier next to it."
    ),
    "bridge_access_cypher": Item(
        id="bridge_access_cypher",
        name="Access Cypher",
        keywords=["cypher", "bridge", "access", "access cypher", "bridge access cypher"],
        debug_info="Captain's quarters vault you find this."
    ),
}


backpack = initial_items["backpack"]
radio = initial_items["radio"]
maintenance_jack = initial_items["maintenance_jack"]
engys_keycard = initial_items["engys_keycard"]
flashlight = initial_items["flashlight"]
welder = initial_items["welder"]
lockpick = initial_items["lockpick"]
screwdriver = initial_items["screwdriver"]
sart = initial_items["sart"]
bridge_access_cypher = initial_items["bridge_access_cypher"]

def initial_items_setup():
    # Act 1
    crew_lockers.items["backpack"] = backpack
    crew_lockers.items["maintenance_jack"] = maintenance_jack
    crew_lockers.items["radio"] = radio
    # Act 2
    medical_labs.items["engys_keycard"] = engys_keycard
    environmental_controls.items["flashlight"] = flashlight
    deck_5_aft_utility.items["welder"] = welder
    # Act 4
    eva_gear_lockers.items["screwdriver"] = screwdriver
    eva_gear_lockers.items["sart"] = sart

# Interactables functions

def interacted_cryo_terminal():
    player.output="You interacted with the cryo terminal"

def interacted_icarus_systems_terminal():
    sart.can_take = True
    sart.on_look = "The lock is open and the sart can be taken."
    player.output += "EVA Lockers SART lock opened."

# Interactables data

initial_interactables = {
    "cryo_bay_terminal": Interactable(
        id="cryo_bay_terminal",
        name="Cryo Bay Terminal",
        keywords=["terminal", "console", "terminal console", "cryo terminal"],
        debug_info="Act 1 Broken down door, open with jack",
        on_look="The terminal console is dark, its screen glowing softly with amber readouts that pulse in quiet rhythm.",
        on_interact_func=interacted_cryo_terminal
    ),
    "icarus_systems_terminal": Interactable(
        id="icarus_systems_terminal",
        name="ICARUS Systems Terminal",
        keywords = ["terminal", "console", "icarus", "systems", "data", "note"],
        debug_info="Main systems terminal inside Data Server Array.",
        on_look="The ICARUS Systems Terminal is a heavy-duty, reinforced console built directly into the floor. Its primary interface is fully active, displaying a sequence of high-level network protocols demanding authentication. \n\nYou note the massive auxiliary power connection required to run it, hinting at its high signal output capability. \n\nRight next to the interface, a faded yellow sticky note is secured to the console, bearing the text: Admin 1234.",
        on_interact_func=interacted_icarus_systems_terminal,
    ),

}

cryo_bay_terminal = initial_interactables["cryo_bay_terminal"]
icarus_systems_terminal = initial_interactables["icarus_systems_terminal"]

def initial_interactables_setup():
    cryo_bay.interactables["cryo_bay_terminal"] = cryo_bay_terminal
    data_server_array.interactables["icarus_systems_terminal"] = icarus_systems_terminal

## use_targets functions

# Act 1
def mess_hall_blast_door_used():
    player.output = "Mess hall blast door used"
    deck_4_mid_aft_passage.is_open = True
# Act 2
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

# Act 4
def operations_and_cargo_interlink_console_used():
    player.output += f"The door next to the console clicks and the lock to {cargo_bay_control_f.name} is open."
    cargo_bay_control_f.is_open = True

def cargo_bay_control_f_power_bus_used():
    player.output_fast += "You finish forcing the lever, and the power bus hums back to life. Just then, you glance out the massive control room window into the Cargo Bay. You spot Tanaka, still in his technician uniform, moving erratically across the deck below. He seems completely lost and erratic. \n\nA sudden impossibly large shadow stretches across the cargo bay floor, falling from the high ceiling where no shadows should exist. You look up and see the colossal arachnoid creature dropping like a silent anchor, instantly closing the distance to the floor. The terrifying clicking sound begins, sharp and deafening, echoing up from the vast bay. \n\nInstinct takes over and you duck low behind the inert consoles, shielding your eyes. You don't see the impact, but the clicking quickly gives way to a sickening, muffled crunch and a brief, strangled cry that is abruptly cut short. When the silence returns, it is heavy and absolute. You know Tanaka didn't make it..."
    bridge.is_open = True
    cargo_bay_control_f.on_enter = "You duck on the floor to not be seen through the large window. This is no time to look around, the arachnid creature might still be there in the cargo bay."
    cargo_bay_control_f.on_revisit = "You duck on the floor to not be seen through the large window. This is no time to look around, the arachnid creature might still be there in the cargo bay."
    cargo_bay_control_f.on_survey = "You are ducking on the floor to not be seen through the large window. This is no time to look around, the arachnid creature might still be there in the cargo bay."

def personal_command_vault_welder_used():
    player.output += "You welded the thing open."
    player.cur_room.remove_use_target(personal_command_vault_before_weld)
    player.cur_room.add_use_target(personal_command_vault_after_weld)

def personal_comand_vault_screwdriver_used():
    player.output += "You used the screwdriver to open it."
    player.cur_room.add_item(bridge_access_cypher)
    player.take("cypher")

def data_array_door_lockpick_used():
    data_server_array.is_open = True
    player.output += "You hear a click and the door opens."

# use_targets data

initial_use_targets = {
    "mess_hall_blast_door": UseTarget(
        id="mess_hall_blast_door",
        name="Mess Hall Blast Door",
        keywords = ["door", "blast door", "blastdoor", "broken door", "broken down door"],
        debug_info="Act 1 Broken down door, open with jack",
        on_look="You observe the heavy metallic edge of the Blast Door. The emergency hydraulic bolts are partially retracted, but the frame is visibly seized and fused. There are no electronic panels or keypads visible; the mechanism appears to be locked purely by immense mechanical pressure. This is a job for focused, brute force.",
        use_func=mess_hall_blast_door_used),
    "env_controls_access_panel": UseTarget(
        id="env_controls_access_panel",
        name="Environmental Control Access Panel",
        keywords = ["access panel", "panel", "keypad", "keypanel", "console", "terminal", "security", "keylogger"],
        debug_info="Act 2 keypad to Environmental Controls.",
        on_look="A compact keypad and card swipe terminal connected to the ship’s security network. Its small green display sits blank, awaiting input.",
        use_func=env_controls_access_panel_use_keypad),
    "central_freight_bay_bulk_door": UseTarget(
        id="central_freight_bay_bulk_door",
        name="Central Freight Bay Bulk Door",
        keywords = ["door", "blast door", "blastdoor", "broken door", "broken down door"],
        debug_info="Act 2 Broken down door, open with welder",
        on_look="The central freight bay door sits sealed and unyielding. \nA narrow panel clings to its side, warped and jammed, its edges surprisingly thin against the massive door. \n\nInside, you can just make out a tangle of rods and mechanisms. There must be some way to override the locks, if you can reach them. \n\nWhatever caused the door to fail, it won’t budge without a careful approach.",
        use_func=central_freight_bay_blast_door_used),
    "logistics_door_console": UseTarget(
        id="logistics_door_console",
        name="Logistics Access Console",
        keywords = ["console", "terminal", "logistics", "logistics console", "diagnostic", "diagnostics", "diagnostic console"],
        debug_info="Console that needs SART to be used on it.",
        on_look="It is a small, specialized terminal mounted beside the door. It has an exposed electronic interface port but no keypad or manual override. The screen is dark, confirming the system has failed and requires a high-level diagnostic tool to handshake with the security lock and initiate access.",
        use_func=operations_and_cargo_interlink_console_used),
    "power_bus_distribution_panel": UseTarget(
        id="power_bus_distribution_panel",
        name="Power Bus Distribution Panel",
        keywords = ["power","bus", "distribution", "panel", "closet"],
        debug_info="Act 4 power bus unit inside cargo_bay_control_f. Use maintenance jack.",
        on_look="It is a heavy, gray metallic cabinet bolted to the wall, humming loudly with suppressed voltage. The automated controls are dark, but the manual override lever is visible behind a reinforced safety grate. This bus controls the dedicated line feeding the Command Deck and Bridge systems. The lever is clearly seized solid due to immense pressure and heat and will not budge by hand. The only way to restore power is by applying extreme, focused leverage.",
        use_func=cargo_bay_control_f_power_bus_used,),
    "personal_command_vault_before_weld": UseTarget(
        id="personal_command_vault_before_weld",
        name="Personal Command Vault",
        keywords = ["vault", "personal", "personal vault", "safe", "command"],
        debug_info="Act 2 Broken down door, open with welder",
        on_look="The Personal Command Vault is a sturdy, dark gray safe bolted to the rear wall. The unit itself appears undamaged. The standard electronic keypad access has been completely covered by an emergency metallic blast plate, suggesting a high-level, automated lockdown. This plate is held firmly in place by four heavy, visible structural welds and cannot be removed without cutting the seals.",
        use_func=personal_command_vault_welder_used),
    "personal_command_vault_after_weld": UseTarget(
        id="personal_command_vault_after_weld",
        name="Personal Command Vault",
        keywords = ["vault", "personal", "personal vault", "safe", "command"],
        debug_info="Act 2 Broken down door, open with welder",
        on_look="The Personal Command Vault is now partially open. The protective blast plate lies on the floor beside it, exposing the inner electronic lock mechanism.\n\nThe mechanism's small access panel is seized shut and secured by four tiny, specialized security screws.\n\nTo get inside, you'll need to find a way past that last, delicate barrier.",
        use_func=personal_comand_vault_screwdriver_used),
    "data_array_door": UseTarget(
        id="data_array_door",
        name="Data Array Door",
        keywords = ["door", "data", "array", "systems", "lock"],
        debug_info="Data Server Array room broken down door. Use lockpick to open.",
        on_look="The destruction of the console has rendered the primary lock useless. The emergency mechanical lock tumblers are visible in a small recess next to the frame. They are jammed and cannot be operated by hand, but the exposed key housing is small and complex, indicating it was designed for fine, precision manipulation.",
        use_func=data_array_door_lockpick_used),
}

mess_hall_blast_door = initial_use_targets["mess_hall_blast_door"]
env_controls_access_panel = initial_use_targets["env_controls_access_panel"]
central_freight_bay_bulk_door = initial_use_targets["central_freight_bay_bulk_door"]
logistics_door_console = initial_use_targets["logistics_door_console"]
power_bus_distribution_panel = initial_use_targets["power_bus_distribution_panel"]
personal_command_vault_before_weld = initial_use_targets["personal_command_vault_before_weld"]
personal_command_vault_after_weld = initial_use_targets["personal_command_vault_after_weld"]
data_array_door = initial_use_targets["data_array_door"]

def initial_use_targets_setup():
    galley.use_targets["mess_hall_blast_door"] = mess_hall_blast_door
    deck_4_med_env_corridor.use_targets["env_controls_access_panel"] = env_controls_access_panel
    upper_aft_lobby.use_targets["central_freight_bay_bulk_door"] = central_freight_bay_bulk_door
    captains_quarters.use_targets["personal_command_vault_before_weld"] = personal_command_vault_before_weld
    systems_data_access_corridor.use_targets["data_array_door"] = data_array_door
    operations_and_cargo_interlink.use_targets["logistics_door_console"] = logistics_door_console
    cargo_bay_control_f.use_targets["power_bus_distribution_panel"] = power_bus_distribution_panel

def setup_use_targets_usable_items():
    mess_hall_blast_door.usable_items["maintenance_jack"] = maintenance_jack
    env_controls_access_panel.usable_items["engys_keycard"] = engys_keycard
    central_freight_bay_bulk_door.usable_items["welder"] = welder
    logistics_door_console.usable_items["sart"] = sart
    power_bus_distribution_panel.usable_items["maintenance_jack"] = maintenance_jack
    personal_command_vault_before_weld.usable_items["welder"] = welder
    personal_command_vault_after_weld.usable_items["screwdriver"] = screwdriver
    data_array_door.usable_items["lockpick"] = lockpick

# Sceneries

sceneries = {}

# NPCS
def setup_npcs():
    medical_labs.npcs["engy"] = engy
    deck_5_secure_pathway.npcs["chef"] = chef

# Arachnid
def setup_arachnid():
    pass

## Run all necessary setups

def run_all_setups():
    initial_rooms_setup()
    initial_interactables_setup()
    initial_items_setup()
    initial_use_targets_setup()
    setup_use_targets_usable_items()
    setup_npcs()

run_all_setups()


def debug_stuff():
    player.inventory["maintenance_jack"] = maintenance_jack
    player.inventory["welder"] = welder
    player.inventory["screwdriver"] = screwdriver
    player.inventory["lockpick"] = lockpick
    player.inventory["sart"] = sart
debug_stuff()