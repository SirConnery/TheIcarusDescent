from game_classes import Game, Player, NPC, Room, Item, Interactable, UseTarget, Scenery
from npc_data import engy, chef, tanaka, captain, arachnid
player = Player()
game = Game()

## Rooms

rooms = {
    "cryo_bay": Room(
        id="cryo_bay",
        name="Cryo Bay",
        debug_info="It is a room with cryo stuff.",
    ),
    "cryo_vestibule": Room(
        id="cryo_vestibule",
        name="Cryo Vestibule",
        debug_info="It is a vestibule connecting CryoBay, Mess Hall and Crew Lockers.",
    ),
    "galley": Room(
        id="galley",
        name="Galley",
        debug_info="A room with small kitchen and dinner table, some sofas",
    ),
    "crew_lockers": Room(
        id="crew_lockers",
        name="Crew Lockers",
        debug_info="A room with small kitchen and dinner table, some sofas",
    ),
    "cryo_midship_transfer_passageway": Room(
        id="cryo_midship_transfer_passageway",
        name="Cryo-Midship Transfer Passage",
        debug_info="A passage connecting Act 1 and Act 2",
    ),
    "deck_4_med_env_corridor": Room(
        id="deck_4_med_env_corridor",
        name="Deck 4 Med-Env Corridor",
        debug_info="Start of Act 2.",
    ),
    "medical_labs": Room(
        id="medical_labs",
        name="Medical Labs",
        debug_info="Medical laboratory where you find a keycard",
    ),
    "environmental_controls": Room(
        id="environmental_controls",
        name="Environmental Controls",
        debug_info="Needs passcode. Find flashlight.",
    ),
    "upper_aft_lobby": Room(
        id="upper_aft_lobby",
        name="Upper Aft Lobby",
        debug_info="Connecting room to cargo and utility.",
    ),
    "central_freight_bay": Room(
        id="central_freight_bay",
        name="Central Freight Bay",
        debug_info="Massive cargo bay.",
    ),
    "deck_5_aft_utility": Room(
        id="deck_5_aft_utility",
        name="Deck 5 Aft Utility",
        debug_info="Small utility room.",
    ),
    "cargo_staging_room": Room(
        id="cargo_staging_room",
        name="Cargo Staging Room",
        debug_info="Small room for cargo.",
    ),
    "deck_5_secure_pathway": Room(
        id="deck_5_secure_pathway",
        name="Deck 5 Secure Pathway",
        debug_info="2 person pathway.",
    ),
    "service_access_hatchway": Room(
        id="service_access_hatchway",
        name="Service Access Hatchway",
        debug_info="Act 3 filler room.",
    ),
    "msc_1": Room(
        id="msc_1",
        name="MSC1 Main Service Control 1",
        debug_info="MSC Room 1 divided by mirror.",
    ),
    "msc_2": Room(
        id="msc_2",
        name="MSC2 Main Service Control 2",
        debug_info="MSC Room 2 divided by mirror. Alien encounter here.",
    ),
    "msc_2_b_storage_drums": Room(
        id="msc_2_b_storage_drums",
        name="MSC2 Main Service Control 2 (behind power storage drums)",
        debug_info="MSC Room 2 behind power storage drums.",
    ),
    "msc_2_b_console_desk": Room(
        id="msc_2_b_console_desk",
        name="MSC2 Main Service Control 2 (under console desk)",
        debug_info="MSC Room 2 behind console desk.",
    ),
    "msc_2_b_power_conduit": Room(
        id="msc_2_b_power_conduit",
        name="MSC2 Main Service Control 2 (behind power conduit manifold)",
        debug_info="MSC Room 2 behind power conduit manifold.",
    ),
    "msc_service_tunnel": Room(
        id="msc_service_tunnel",
        name="MSC2 Maintenance Access Tunnel",
        debug_info="MSC2 ventilation shaft.",
    ),
    "service_control_junction_5f": Room(
        id="service_control_junction_5f",
        name="Service Control Junction 5 F",
        debug_info="The door before entering. Act 4.",
    ),
    "operations_distribution_crossover": Room(
        id="operations_distribution_crossover",
        name="Operations Distribution Crossover",
        debug_info="Act 4 starting corridor.",
    ),
    "operations_and_cargo_interlink": Room(
        id="operations_and_cargo_interlink",
        name="Operations and Cargo Interlink",
        debug_info="Act 4 corridor between cargo and bridge.",
    ),
    "cargo_bay_control_f": Room(
        id="cargo_bay_control_f",
        name="Cargo Bay Control F",
        debug_info="Act 4 cargo bay control overwatch room.",
    ),
    "external_ops_access_way": Room(
        id="external_ops_access_way",
        name="External Ops Access Way",
        debug_info="Act 4 corridor between cargo and bridge.",
    ),
    "eva_gear_lockers": Room(
        id="eva_gear_lockers",
        name="EVA Gear Lockers",
        debug_info="Act 4 eva gear locker.",
    ),
    "central_utility_spine_5_f": Room(
        id="central_utility_spine_5_f",
        name="Central Utility Spine 5 F",
        debug_info="Part of the middle ship spanning hallway.",
    ),
    "central_utility_spine_4_f": Room(
        id="central_utility_spine_4_f",
        name="Central Utility Spine 4 F",
        debug_info="This door is broken and the room cannot be accessed.",
    ),
    "central_utility_spine_6_f": Room(
        id="central_utility_spine_6_f",
        name="Central Utility Spine 6 F",
        debug_info="Part of the middle ship spanning hallway.",
    ),
    "deck_5_forward_muster_station": Room(
        id="deck_5_forward_muster_station",
        name="Deck 5 Forward Muster Station",
        debug_info="Large empty area meant for gathering and receiving urgent instructions.",
    ),
    "bridge": Room(
        id="bridge",
        name="Bridge",
        debug_info="Ship bridge.",
    ),
    "systems_data_crossover": Room(
        id="systems_data_crossover",
        name="Systems Data Crossover",
        debug_info="Corridor before Systems Data Access Corridor.",
    ),
    "systems_data_access_corridor": Room(
        id="systems_data_access_corridor",
        name="Systems Data Access Corridor",
        debug_info="Corridor before Server Array.",
    ),
    "data_server_array": Room(
        id="data_server_array",
        name="Data Server Array",
        debug_info="Ship network and system control data central.",
    ),
    "executive_access_aisle": Room(
        id="executive_access_aisle",
        name="Executive Access Aisle",
        debug_info="Ship network and system control data central.",
    ),
    "captains_quarters": Room(
        id="captains_quarters",
        name="Captain's Quarters",
        debug_info="Living place for the captain.",
    ),
    "command_transit_vestibule": Room(
        id="command_transit_vestibule",
        name="Command Transit Vestibule",
        debug_info="Stairway connecting to deck_5_forward_muster_station.",
    ),
    "vertical_service_shaft": Room(
        id="vertical_service_shaft",
        name="Vertical Access Hatch",
        debug_info="Access module from bridge to the rear of the ship.",
    ),
    "reactor_deck_service_hub": Room(
        id="reactor_deck_service_hub",
        name="Reactor Deck Service Hub",
        debug_info="Room before reactor room.",
    ),
    "auxiliary_reactor_control": Room(
        id="auxiliary_reactor_control",
        name="Auxiliary Reactor Control",
        debug_info="The reactor room.",
    ),
    "emergency_launch_compartment": Room(
        id="emergency_launch_compartment",
        name="Emergency Launch Compartment",
        debug_info="Small space next to reactor room.",
    ),
    "emergency_launch_access_corridor": Room(
        id="emergency_launch_compartment",
        name="Emergency Launch Access Corridor",
        debug_info="Corridor leading to lifeboats.",
    ),
    "emergency_vehicles_bay": Room(
        id="emergency_vehicles_bay",
        name="Emergency Vehicles Bay",
        debug_info="Final emergency exit before the end.",
    ),
    "tantalus_ark": Room(
        id="tantalus_ark",
        name="Emergency Vehicles Bay (inside The Tantalus Ark)",
        debug_info="Medium sized escape vessel Cutter Class.",
    ),
    "tantalus_ark_final": Room(
        id="tantalus_ark_final",
        name="Tantalus Ark",
        debug_info="Final room before game end.",
    ),
}

# Act 1
cryo_bay = rooms["cryo_bay"]
cryo_vestibule = rooms["cryo_vestibule"]
galley = rooms["galley"]
crew_lockers = rooms["crew_lockers"]
cryo_midship_transfer_passageway = rooms["cryo_midship_transfer_passageway"]
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
msc_service_tunnel = rooms["msc_service_tunnel"]
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
# Act 5
vertical_service_shaft = rooms["vertical_service_shaft"]
reactor_deck_service_hub = rooms["reactor_deck_service_hub"]
auxiliary_reactor_control = rooms["auxiliary_reactor_control"]
emergency_launch_compartment = rooms["emergency_launch_compartment"]
# Act 6
emergency_launch_access_corridor = rooms["emergency_launch_access_corridor"]
emergency_vehicles_bay = rooms["emergency_vehicles_bay"]
tantalus_ark = rooms["tantalus_ark"]
tantalus_ark_final = rooms["tantalus_ark_final"]

## Room custom events
# Act 1
def cryo_bay_intro():
    player.warmth = "Cold"
    player.warmth_color = "dodger_blue"
    player.output_slow = "\n\nYou awaken to silence… \n\nCold air brushes across your skin, prickling through the thin fabric of your long underwear and undershirt. As you sit up, a faint hiss of the cryochamber releasing the last of its frost escapes from beneath you. Soft, intermittent bleeps echo from the nearby computer panels, a quiet rhythm that pulses through the room. \n\nThe room around you glows faintly in shades of white and pale blue. Rows of cyan metallic cryochambers curve around a white central pillar, their surfaces lit by strips of neon light. The walls are padded with soft, white panels, and bulky computer screens are embedded between them, their glass dim and lifeless. \nEvery other chamber stands open and empty. \n\nMaybe the others awoke before you…"
def crew_lockers_event():
    player.take("backpack")
    player.take("radio")
    
    player.warmth = "Warm"
    player.warmth_color = "green"

    player.output += "This large room is dominated by rows of metal lockers and features two small shower stalls near the back wall. \n\nYou quickly locate your assigned locker. You pull on your utility uniform and pick up your brown canvas backpack, noting the partially broken emergency radio secured to the strap. You really should have fixed it before your shift ended. \n\nAfter putting on some clothes you start to feel warmer and more comfortable. \n\nNear the floor, you spot your trusty old Maintenance Jack, exactly where you left it."
# Act 2
def deck_4_med_env_corridor_room_event():
    cryo_midship_transfer_passageway.is_open = False
    cryo_midship_transfer_passageway.locked_description = "I should push forward, there is no reason to return now..."
    player.output_fast += "The air hums faintly, but the lights here are extremely dim, reduced to a weak, hazy glow. Ahead of you, the stairway leading up to Deck 5 is completely shrouded in blackness. \n\n"
    player.output_fast += "The door to the Medical Bay on your left shows a thin line of bright, steady light beneath its frame, suggesting power is holding in that section.\n"
    player.output_fast += "On your right, the door to Environmental Controls is secured by a panel featuring both a keycard swipe slot and a digital passcode reader. The heavy security lock is clearly functional."

def medical_labs_room_event():
    player.heartrate = "Elevated"
    player.heartrate_color = "orange3"

    player.output_normal += "The room is squeaky clean as you would expect from a medical room, dominated by two sterile white examination tables. The lights here are working perfectly, but the silence is profound.\n\n"
    player.output_normal += "You stop, breath seizing in your throat.\n"
    player.output_normal += "You see a body on the floor. It's Enrique. He is lying motionless on the floor near the exit. \n\nYou try to wake him up, but he is clearly not breathing and has likely been like this for a while.\n\n"
    player.output_normal += "A sharp, acrid scent of ozone and burnt wiring insulation assaults your nose, confirming the tragedy wasn't natural. You stand there a moment, processing the terrible reality, the first confirmed casualty."
    player.output_normal += "On the floor next to Enrique you notice a plastic card."
# Act 3
def cargo_staging_room_room_event():
    player.output_normal += "The door closes behind you. Suddenly the dim, failing red lights give way to stable, normal illumination.\n"
    player.output_normal += "The power and lighting seem to have stabilized.\n\n"
    player.output_normal += "You hear the heavy crash of metal hitting the deck, followed by a loud screech of stressed metal and a final, dull thud, coming from the next room.\n"

def deck_5_secure_pathway_room_event():
    player.output_normal += "The corridor here has some dim lighting again, it looks like some of the fluorescent ceiling strips have short-circuited and gone black.\n"
    player.output_normal += "In the distance, down the corridor, you see a shape that doesn't belong there... It's coming towards you.\n\n"
    player.output_normal += "You pull out your flashlight to see what it is.\n\n"
    player.output_normal += "Chef: Hey, girl.\n"
    player.output_normal += "You realize it's your old friend, Chef. A wave of relief goes through your chest.\n"
    player.output_normal += "Chef: Aren't you grease monkeys supposed to keep the lights on here? The power is all kinds of messed up. I think I fixed it for now but you better take a look at it, Nat.\n\n"
    player.output_normal += "Before answering you take a brief moment to look at Chef. He is a broad, muscular black man in a dark-gray utility jumpsuit with sleeves rolled up to his biceps.\n\n"
    player.output_normal += "Nat: Chef, Enrique is dead.\n"
    player.output_normal += "Chef: I know. I came through there. It's bad, Nat. This ain't just fuses.\n"
    player.output_normal += "Chef: You know how to work the power right Nat? Let's go to the Main Service Control and see what's up.\n"
    player.output_normal += "Nat: Sure. Lead the way Chef."

def service_access_hatchway_room_event():
    player.output_normal += "Chef: Hold up. What's that smell? Burnt metal and fried wiring. That from your deck, Nat?\n"
    player.output_normal += "Nat: Yeah. You know, that smell reminds me of your kitchen.\n"
    player.output_normal += "Chef: Yeah, yeah, roast my kitchen later. That smell's serious, or you just cooked another conduit?\n"
    player.output_normal += "Nat: Keep it moving, Chef."

def msc_1_room_event():
    player.warmth = "Hot"
    player.warmth_color = "orange3"

    player.output_normal += "The room has only dim lighting, you pull out your flashlight for better vision.\n"
    player.output_normal += "Exposed conduits and thick, heavy piping line the reinforced walls. Directly ahead, a single, reinforced window overlooks a mirrored control station at Main Service Control 2.\n"
    player.output_normal += "The air here is noticeably warm, but the relentless roar of ventilation fans makes it hard to even hear your own thoughts. \n\n"    
    player.output_normal += "Chef: CHECK OUT WHAT'S HAPPENING WITH THE SHIP, NAT!\n"
    player.output_normal += "Nat: THE POWER SYSTEMS ARE IN MSC 2! I'LL CHECK IT OUT!\n\n"
    player.output_normal += "Through the window you see Main Service Control 2."

def msc_2_room_event():
    player.heartrate = "High"
    player.heartrate = "Red"

    player.drop("flashlight")
    flashlight.can_take = False
    flashlight.locked_description = "Unable to take Flashlight. The flashlight has dropped into a maintenance drain out of your reach."

    player.output_fast +=  "The heavy access door slams shut behind you with a deafening hydraulic screech.\n"
    player.output_fast +=  "The shock of the impact throws you off balance. Your flashlight slips from your grip, skitters across the floor, and clatters down the maintenance drain near the wall, plunging the room into dim shadow.\n"
    player.output_fast +=  "Only a few emergency lamps flicker to life, bathing the industrial bay in a weak dim yellow light.\n"
    player.output_fast +=  "An emergency alarm starts blaring. You're not sure what's caused it.\n\n"
    player.output_fast +=  "Suddenly your radio crackles into life.\n\n"
    player.output_fast +=  "Chef (via radio, sounding clearly panicked): **WHAT IS THAT!? NAT, YOU NEED TO HIDE, QUICKLY! MEET ME AT THE BRIDGE!**\n\n"
    player.output_fast +=  "The broadcast ends instantly, leaving only static and the roar of the fans. You realize your broken radio can still receive broadcasts but not send them.\n"
    player.output_fast +=  "You hear a clicking sound that can be heard even above the noise of the ventilation. You look up and see something crawling in the vents.\n"
    player.output_fast +=  "You decide it's time to hide, and fast.\n\n"
    player.output_fast +=  "You quickly scan the room and see 3 potential hiding places:\n"
    player.output_fast +=  "— Behind the Power Conduit Manifold\n"
    player.output_fast +=  "— Under the Operator Console Deck\n"
    player.output_fast +=  "— Behind the stacked Heavy Industrial Drums"

def msc_2_room_default_hiding_event_end():
    player.output_fast += "\n\nThe clicking sound intensifies, growing from a rattle in the ducts to a deafening, metallic percussion. Suddenly, a colossal arachnid creature drops from the vent high above and lands with a heavy, floor-shaking impact in the center of the room.\n\n"
    player.output_fast += "You take a peek and finally see it clearly: Its main body is easily three meters long, and its spike-like legs stretch another two meters, allowing it to dominate the entire floor space. The creature is segmented and impossibly large.\n\n"
    player.output_fast += f"Near the floor behind you, you spot a loose inspection vent hatch. If you can carefully remove the heavy cover, you should gain access to the {msc_service_tunnel.name}."
    player.output_fast += "You hope the sound of the ventilation will mask your escape."

def msc_2_power_conduit_hiding_room_event():
    player.output_fast +=  "The Power Conduit Manifold is a dense, metallic structure where power lines converge. A narrow, dark pocket of shadow exists behind the thick bundles of cables near the floor. \n\nYou squeeze into the space.\n\n"
    msc_2_room_default_hiding_event_end()

def msc_2_b_storage_drums_hiding_room_event():
    player.output_fast += "A cluster of heavy industrial drums, labeled with faded biohazard symbols, stands near the reinforced wall. They are secured with thick polymer bands, leaving a narrow, dark crevice between them and the wall.\n\nYou squeeze into the space.\n\n"    
    msc_2_room_default_hiding_event_end()

def msc_2_b_console_desk_hiding_room_event():
    player.output_fast += "The heavy operator console is bolted to the floor. Beneath it, a cramped crawlspace is barely visible, filled with exposed wiring and discarded ties. It offers just enough shadow and clearance for you to squeeze out of sight."
    msc_2_room_default_hiding_event_end()

def msc_service_tunnel_room_event():
    msc_2.is_open = False
    msc_2.locked_description = "There is no reason to go back with that creature still roaming there..."
    player.output_fast += f"You carefully remove the vent cover and move through into the {msc_service_tunnel.name}. The passage is dark and smells sharply of ozone and old metal, but it is wide enough for you to traverse without crawling. You can still hear the clicking come through the metal, amplified by the confined space. Since you've been in these utility shafts before, you quickly orient yourself and start making your way forward towards the bridge."

def service_control_junction_5f_room_event():
    player.warmth = "Warm"
    player.warmth_color = "green"
    player.heartrate = "Calm"
    player.heartrate_color = "green"

    msc_service_tunnel.is_open = False
    msc_service_tunnel.locked_description = "There is no reason to go back with that creature still roaming there..."
    player.output_normal += f"You emerge from the dark access tunnel into the {service_control_junction_5f.name}. This wide, functional room is filled with utility access panels and large conduits. You recognize this as a critical nexus for power and communication lines.\n\n"
    player.output_normal += f"Your path forward is blocked by a heavy, structural blast door. The door's lock mechanism is completely fused shut, and the frame is covered in thick, hardened polymer sealant. The door resists all manual force; its seams appear to be structurally sealed with material that only intense, sustained heat could liquefy."

# Act 4
def act_4_start():
    operations_distribution_crossover.is_open = True
    service_control_junction_5f.is_open = False
    service_control_junction_5f.locked_description = "There is no reason to go back with that thing roaming there..."
    player.output_normal += "You are away from danger, for now. \n\nHere the air is cool and clean, and the lights are steady. \n\nThis small access point serves as a clean transition area between the the ship spine and cargo operations."

def meet_panicked_npc_executive_access_aisle():
    player.output_normal += f"\n\nThis narrow corridor is impeccably maintained and quiet, emphasizing its purpose as a high-security link. \nOn the right of the corridor the door to Captain's Quarters is visible."
    player.output_normal += "Ahead of you see someone coming out from the Captain's Quarters.\n"
    player.output_normal += "It's Tanaka! The ship's data systems analyst. He seems visibly terrified.\n\n"
    player.output_normal += "Tanaka: Aagh, he's dead, the captain's dead! We're all gonna die!!\n\n"
    player.output_normal += f"Before you know how to react Tanaka disappears through the door towards {systems_data_access_corridor.name}.\n\n"
    player.output_normal += "Nat: Tanaka! Wait!\n\n"

    systems_data_access_corridor.is_event_trigger = True
    systems_data_access_corridor.room_event = meet_panicked_npc_systems_data_access_corridor

def meet_panicked_npc_systems_data_access_corridor():
    systems_data_crossover.is_event_trigger = True
    systems_data_crossover.room_event = meet_panicked_npc_systems_data_systems_crossover
    player.output_fast += f"\n\nYou see Tanaka disappearing through the door toward {systems_data_crossover.name}.\n\n"
    player.output_normal += "Nat: Tanaka!\n\n"

def meet_panicked_npc_systems_data_systems_crossover():
    central_utility_spine_5_f.is_event_trigger = True
    central_utility_spine_5_f.room_event = meet_panicked_npc_central_utility_spine_5_f
    player.output_fast += f"\n\nYou see Tanaka disappearing through the door toward {central_utility_spine_5_f.name}.\n\n"
    player.output_normal += "Nat: Tanaka! Stop! I need to tell you something!\n\n"

def meet_panicked_npc_central_utility_spine_5_f():
    operations_distribution_crossover.is_event_trigger = True
    operations_distribution_crossover.room_event = meet_panicked_npc_operations_distribution_crossover
    player.output_fast += f"\n\nYou see Tanaka disappearing through the door toward {operations_distribution_crossover.name}.\n\n"
    player.output_normal += "Nat: Tanaka! Get a hold of yourself!"

def meet_panicked_npc_operations_distribution_crossover():
    operations_distribution_crossover.items["lockpick"] = lockpick
    service_control_junction_5f.is_open = False
    service_control_junction_5f.locked_description = "The blast door was triggered by the ship's central system and there is no way through to follow after Tanaka."
    operations_distribution_crossover.on_revisit = "The air remains cool and the lighting steady. You spot something glimmering on the floor."
    operations_distribution_crossover.on_survey = f"This corridor is narrow and reinforced, designed for limited crew transit between the central spine and the external operation staging areas. The walls are smooth, and the overhead utilities are secured and caged.\n\n The blast door has dropped on the door leading to {service_control_junction_5f.name}.\n Lying just beside the blast door, you spot a small, professional lockpick set glinting faintly. It must have fallen from Tanaka's belt.\n\n"

    player.output_fast += "\n\nIn his blind haste, the small chain securing Tanaka's gear snags violently on a damaged utility conduit jutting from the wall.\n"
    player.output_fast += "The force rips the tool free, and you hear it tumble loudly with a metallic clang onto the polished deck where it skitters across the floor.\n\n"    
    player.output_fast += "Tanaka! Stop! There's a monster in the ship!\n\n"
    player.output_fast += f"Tanaka keeps panicking and doesn't seem like he paid any attention to your shouts and bolts through the door toward {service_control_junction_5f.name}.\n\n"
    player.output_fast += f"Right then, the synthesized ship system voice blares: 'ICARUS SYSTEMS BREACH DETECTED. ISOLATING SECTOR 4F. CONTAINMENT PROTOCOL ACTIVATED.'\n"
    player.output_fast += f"The breach door on {service_control_junction_5f.name} slams shut with a deafening, final thud.\n\n"
    player.output_normal += "You stare at the door, exhausted.\n"
    player.output_normal += "The corridor is silent. You stare at something glittering on the floor.\n\n"
    player.output_slow += "You give yourself a moment to think...\n'He's gone. The system sealed the door right on him. Right now my job is getting the bridge operational.'"

def captains_quarters_room_event():
    player.heartrate = "Elevated"
    player.heartrate_color = "orange3"

    player.output_normal += "This room is a scene of violent, catastrophic disarray. Furniture is overturned and warped metal streaks across the far wall, where the Captain's body lies. It is immediately clear that he did not die from oxygen loss; the trauma is massive, consistent with being repeatedly pierced and torn by immense, sharp points.\n\nThe room's only untouched feature is the captain's personal command vault, a sturdy, dark gray safe bolted to the rear wall. Its electronic keypad access is completely covered by an emergency metallic blast plate, suggesting a high-level, automated lockdown."

# Act 5
def bridge_room_enter_event():
    player.heartrate = "Calm"
    player.heartrate_color = "green"

    chef.on_look =          "He's a broad, imposing Black man in a dark-gray, reinforced utility jumpsuit. The sleeves are rolled up to his biceps, showing a powerful build, and a thick leather belt is cinched tight. He holds a bulky, jury-rigged flamethrower. \nYou know without a doubt he will fight for both of you until the very end."
    player.output_normal =  "\n\nYou step onto the Bridge. The silence is immense, broken only by the cold hum of auxiliary power. The main command console is dark. Before you can even move, the entry door hisses shut.\n\n"
    player.output_normal += "Nat! \n\nYou spin around. The Chef stands framed in the access hatch, looking ready. He's gripping a bulky, jury-rigged flamethrower.\n\n"
    player.output_normal += "Chef: Look what I found, Nat. I got just enough fuel on this to go for some roast spider meat.\n"
    player.output_normal += "Nat: Chef! Thank God. The console is live. Can we get the lifeboats cycling?\n\n"
    player.output_normal += "The Chef types quickly on the emergency console. The screen flashes red.\n\n"
    player.output_normal += "Chef: Hold up, we got problems. This whole rig is officially cooked, Nat. The pressure regulators on the main airlocks are seized. We can't cycle the life pods from this luxury suite. We gotta go manual.\n"
    player.output_normal += f"Nat: Manual, yes. The {auxiliary_reactor_control.name} on Deck 2. It's the only place with the purge valves and manual lifeboat releases.\n"
    player.output_normal += "Chef: Good. We're not taking the main passage, it's a death trap. Let's use the service route. We'll hit the self-destruct while we're down there. That spider's travel plans are gonna blow up.\n"
    player.output_normal += "Chef: Follow me. Stick close. We're going down three decks, fast.\n\n" 
    player.output_normal += "Nat: Right. Blow the station. Open the pods. Let's move."

def vertical_service_shaft_room_event():
    player.warmth = "Cold"
    player.warmth_color = "dodger_blue"

    player.output_normal = "Chef: Hold up, Nat! This old thing ain't pretty, but it's fast. Remember what I told you: smooth is fast, and fast is life!\n"
    player.output_normal += "Nat: Relax, Chef. I know every weld on this deck better than you know your spice rack.\n"    
    player.output_normal += "Chef: Good. Because where we're going, if we ain't fixing it with muscle and metal, we ain't fixin' it. Keep your eyes peeled, girl. We are running out of time and luck, and baby, I ain't got much of either left!\n"    

def reactor_deck_service_hub_room_event():
    player.warmth = "Warm"
    player.warmth_color = "green"

    player.output_normal += "Chef: This is it, Nat. The Hub. Control Room is right through that door. This place gives me the creeps.\n"
    player.output_normal += "Nat: Hey, I basically live down here.\n"
    player.output_normal += "Chef: Oh right, you grease monkeys get all the fun.\n"
    player.output_normal += "Nat: It takes more than a greasy apron to fix an entire command network, Chef."

def auxiliary_reactor_control_room_event():
    player.heartrate = "Elevated"
    player.heartrate_color = "orange3"

    player.output_normal += "Chef: Hold up now... Did you hear that? The clicking.\n"
    player.output_normal += "Nat: Quick! Close the door! I'm hitting the manual meltdown sequence!\n"    
    player.output_normal += "Chef: Forget the purge! That thing got to the hydraulics, the main line is buckled! We can't get the lifeboats out!\n" 
    player.output_normal += "Nat: I see it. The hydraulic line running along the frame is severely buckled and pinched. That thing cut off all pressure to the feed!\n"
    player.output_normal += f"Nat: The final pressure valve is in the {emergency_launch_compartment.name}. I'm going there now to fix the pinch. You take over the terminal and prepare the purge sequence, Chef.\n"
    player.output_normal += "Chef: Get on it, Nat! I ain't gonna be spider food down here!\n"

def emergency_launch_compartment_room_event():
    player.output_normal += "You enter the room. The heavy duty blast door closes behind you. Inside the room is a small console for operating the lifeboats and above it you see the hydraulic fluid line running along the doorframe. It is completely warped and will need fixing by manual force. You will need some leverage for this one.\n\n" 
    player.output_normal += "You can see Chef through the window."
# Act 6
def emergency_launch_access_corridor_room_event():
    player.status =         "Injured (right ankle freeze-burn)"
    player.status_color =   "orange3"
    player.warmth =         "Freezing"
    player.warmth_color=    "blue"
    player.output_fast += "\n\nThis long, narrow passage is a scene of systemic breakdown. The power has mostly failed, and the only illumination comes from flickering, strobe-like emergency lights that cast the path in blinding flashes of red and black shadow.\n"
    player.output_fast += "The air is freezing, biting at your exposed skin and making your breath plume violently. Structural conduits have been torn from the ceiling, confirming this route is extremely unstable.\n\n"
    player.output_fast += "The main reactor alarm blares violently across the deck. A synthetic voice echoes through the ship: **EMERGENCY MELTDOWN SEQUENCE ACTIVE. T-MINUS THREE MINUTES.** \n\n"
    player.output_fast += "The freezing air hits you with the force of a hammer. You bite down on the pain, forcing yourself into a stumbling, desperate run, relying entirely on the left side of your body.\n"
    player.output_fast += "You need to keep moving."
def emergency_vehicles_bay_room_event():
    player.warmth = "Cold"
    player.warmth_color = "dodger_blue"

    player.output_fast   += "The alarm blares **EMERGENCY MELTDOWN SEQUENCE ACTIVE. T-MINUS TWO MINUTES, THIRTY SECONDS.**\n\n"
    player.output_normal += "The freezing run ends as you stumble your way into the Emergency Vehicles Bay. The room is expansive and, thankfully, the ambient temperature is several degrees warmer than the corridor.\n" 
    player.output_normal += "The emergency lighting here is stable, casting the entire area in a warm, steady glow, offering a brief reprieve from the chaos.\n\n"
    player.output_normal += "The Tantalus Ark Cutter Class sits secured in its launch cradle, looking entirely solid and ready. Its main access hatch is currently open.\n"
    player.output_normal += "You sigh a bit at the sight of the vessel.\n"
    player.output_normal += "You know initiating the magnetic rail launch sequence can be done purely from inside the craft.\n\n"
    player.output_normal += "You think to yourself: I made it. It's ready."

def tantalus_ark_room_event():
    player.output_fast += "The alarm blares **EMERGENCY MELTDOWN SEQUENCE ACTIVE. T-MINUS TWO MINUTES.**\n\n"
    player.output_normal += "You rush up the landing struts and run through the open hatch and hit the button besides the door closing the hatch behind you. The internal lighting flickers on, confirming the craft has power.\n\n"
    player.output_normal += "You are in the pilot cabin of The Tantalus Ark. The main diagnostic screen is green, confirming systems are functional. The controls are within easy reach.\n"
    player.output_normal += "The clock is ticking. You must initiate the launch sequence immediately on the console."

def tantalus_ark_cryobay_room_event():
    player.output_title = "The End"
    game.running = False

## Connect rooms

def connect_all_initial_rooms():
    # Act 1
    cryo_bay.forward = cryo_vestibule
    cryo_vestibule.left = galley
    cryo_vestibule.right = crew_lockers
    cryo_vestibule.backward = cryo_bay
    galley.forward = cryo_midship_transfer_passageway
    galley.right = cryo_vestibule
    crew_lockers.left = cryo_vestibule
    cryo_midship_transfer_passageway.forward = deck_4_med_env_corridor
    cryo_midship_transfer_passageway.backward = galley
    # Act 2
    deck_4_med_env_corridor.left = medical_labs
    deck_4_med_env_corridor.right = environmental_controls
    deck_4_med_env_corridor.forward = upper_aft_lobby
    deck_4_med_env_corridor.backward = cryo_midship_transfer_passageway
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
    msc_1.right = msc_2
    msc_2.right = msc_2_b_power_conduit
    msc_2.forward = msc_2_b_storage_drums
    msc_2.backward = msc_2_b_console_desk
    msc_service_tunnel.forward = service_control_junction_5f
    msc_service_tunnel.backward = msc_2
    service_control_junction_5f.forward = operations_distribution_crossover
    service_control_junction_5f.backward = msc_service_tunnel
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
    deck_5_forward_muster_station.right = command_transit_vestibule
    deck_5_forward_muster_station.forward = bridge
    deck_5_forward_muster_station.backward = central_utility_spine_6_f
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
    # Act 5
    bridge.right = vertical_service_shaft
    vertical_service_shaft.backward = reactor_deck_service_hub
    reactor_deck_service_hub.backward = auxiliary_reactor_control
    auxiliary_reactor_control.right = emergency_launch_compartment
    # Act 6
    emergency_launch_access_corridor.right = emergency_vehicles_bay
    emergency_vehicles_bay.right = tantalus_ark

def set_rooms_defaults():
    # Act 1
    cryo_bay.on_first_enter = "Act 1 - The Beginning"
    cryo_bay.on_revisit = "The cryochamber lies silent, bathed in pale blue light. A lone terminal hums near the door.."
    cryo_bay.on_survey = "You are in the Cryo Bay. The room is dominated by the curving rows of cyan metallic cryochambers arranged around the large white central pillar. Most of the units stand open and empty. \n\nNear the forward door, the Cryo Management Terminal is embedded in the wall, currently displaying a dull, static screen."
    cryo_bay.is_act_event_trigger = True
    cryo_bay.act_number = "1"
    cryo_bay.act_subtitle = "The Beginning"
    cryo_bay.is_event_trigger = True
    cryo_bay.room_event = cryo_bay_intro
    cryo_vestibule.on_first_enter = "The Cryo Vestibule is a short, sterile passage with padded white walls and heavy metallic door frames. The hum of auxiliary systems is steady and consistent. \n\nYou allow your mind to briefly drift:\n\n 'Orbiting SD-4's moon and shipping specialized goods for ICUS Corp... that's the mission. So much routine for such a long journey.'"
    cryo_vestibule.on_revisit = "You are back in the Cryo Vestibule. The passage remains sterile, and the systems continue to hum quietly."
    cryo_vestibule.on_survey = "The Cryo Vestibule is a small, empty passage serving as the air buffer between the Cryo Bay and the main deck area. There are no consoles or utilities here, only the structural doors leading to the Crew Lockers and the Mess Hall."
    galley.on_first_enter = "This small space is tidy but shows signs of regular use, dominated by heavy stainless steel counters and several polished wooden dining tables. It smells faintly of strong brewed coffee and cooking oil, reflecting recent activity. \n\nThe food preparation area is pristine, but there is no one here."
    galley.on_revisit = "You are back in the Galley. The space remains clean and quiet, smelling faintly of coffee."
    galley.on_survey = "This small space is tidy but shows signs of regular use, dominated by heavy stainless steel counters and several polished wooden dining tables. The area smells faintly of strong brewed coffee and cooking oil, reflecting recent activity. The food preparation area is pristine. \n\nThe door leading to the rest of the ship is stuck, maybe you should take a closer look at the door to find a way to open it."
    crew_lockers.on_first_enter = ""
    crew_lockers.on_revisit = "You are back in the Crew Lockers. The room is silent and empty. Your locker is still open, and the rest of the facility remains functional but empty. \n\nNear the floor, you spot your trusty old Maintenance Jack, exactly where you left it."
    crew_lockers.on_survey = "The room is large and empty, dominated by rows of metal lockers and two small shower stalls near the back wall. The facility is functional, immaculately clean, and the air is still slightly warm, suggesting it was used very recently.\n\nnNear the floor, you spot your trusty old Maintenance Jack, exactly where you left it."
    crew_lockers.is_event_trigger = True
    crew_lockers.room_event = crew_lockers_event
    cryo_midship_transfer_passageway.on_first_enter = "You are now in the Cryo-Midship Transfer Passage. This wide, functional corridor acts as the primary link between the hypothermic systems bay and the ship's main operational areas. The walls are lined with standard utility paneling, and the air hums with the steady rhythm of the ship's functional systems."
    cryo_midship_transfer_passageway.on_revisit = "This wide, functional corridor acts as the primary link between the hypothermic systems bay and the ship's main operational areas."
    cryo_midship_transfer_passageway.on_survey = "This wide, functional corridor acts as the primary link between the hypothermic systems bay and the ship's main operational areas. The walls are lined with standard utility paneling, and the air hums with the steady rhythm of the ship's functional systems."
    cryo_midship_transfer_passageway.is_open = False
    cryo_midship_transfer_passageway.locked_description = "The Blast Door resists every push; its frame is fused and bolted tight. Only raw, focused force could budge it"
    # Act 2
    deck_4_med_env_corridor.on_first_enter = "Act 2 - Beneath the Darkness \n\n"
    deck_4_med_env_corridor.on_revisit = f"The dim, hazy light persists, and the atmosphere feels cold and unnerving."
    deck_4_med_env_corridor.on_survey = f"The dim, hazy light persists, and the atmosphere feels cold and unnerving. \n\nThe stairway upstairs is bathed in darkness.\n\nThe keypad towards {environmental_controls.name} is awaiting input."
    deck_4_med_env_corridor.is_act_event_trigger = True
    deck_4_med_env_corridor.act_number = "2"
    deck_4_med_env_corridor.act_subtitle = "Beneath the Darkness"
    deck_4_med_env_corridor.is_event_trigger = True
    deck_4_med_env_corridor.room_event = deck_4_med_env_corridor_room_event
    medical_labs.on_first_enter = ""
    medical_labs.on_revisit = "You're back. Enrique is still lying on the floor motionless.\n\nThere is a plastic card on the floor."
    medical_labs.on_survey = "The space is cold and sterile, equipped with specialized emergency diagnostic machines. \n\nHigh Engineer Enrique's body is lying motionless on the deck. His eyes are open, wide with silent surprise. \n\nYou detect a sharp, acrid scent of ozone and burnt wiring insulation, confirming a severe electrical disaster occurred here. You think it's most likely the air was drained due to some faulty electronics.\n\n You allow yourself a moment of quiet reflection. You remember the crew always called him Engy.\nThough you two didn't know each other well, he seemed like the easy going type who wasn't a stickler for the rules. You remember hearing he had gotten into trouble with the Captain a couple of times...\n\nOn the floor next to Enrique you notice a plastic card."
    medical_labs.is_event_trigger = True
    medical_labs.room_event = medical_labs_room_event
    environmental_controls.on_first_enter = "It's a small, chilly chamber filled with intricate atmospheric monitoring equipment and sealed conduit access panels. The air is very dry. \nThe main consoles are dark, but your eyes are drawn to a faint glint on a central workbench."
    environmental_controls.on_revisit = "You enter the keycode and move in. The machines in the room make a continuous soft humming sound that is somehow soothing. \nThe space remains cold, functional.\n\nnSitting on the steel workbench you notice a a small, handheld flashlight."
    environmental_controls.on_survey = "The walls are covered in dense panels marked with fluid lines and thermal regulators. This room is clearly responsible for the ship's critical HVAC and air-scrubbing systems. All monitoring screens are currently dark, and a faint, high-pitched whine from the equipment indicates the systems are offline or struggling..\n\nSitting on the steel workbench you notice a a small, handheld flashlight."
    environmental_controls.is_open = False
    environmental_controls.locked_description = "The door to Environmental Controls remains sealed. The access panel glows faintly, waiting for a valid code. No amount of pressing or swiping seems to budge it."
    upper_aft_lobby.on_first_enter = "It's complete darkness... \n\nYou know the layout of the ship and  can make your way from room to room but you can see nothing."
    upper_aft_lobby.on_revisit = "You can see nothing in the darkness..."
    upper_aft_lobby.on_survey = "You can see nothing in the darkness..."
    central_freight_bay.on_first_enter = "The area is vast and oppressive, dominated by rows of massive, stacked freight containers. The main lights are offline, leaving the space illuminated only by dim emergency lamps.\n\nYour flashlight beam is weak but sufficient to cut through the gloom. The air systems hum steadily, confirming the environment is stable.\n\nYou decide the first priority must be the system failure that caused this darkness. You know the power bus distribution panels are located in the sections accessed via the right corridor."
    central_freight_bay.on_revisit = "The area remains vast, dark, and oppressive, illuminated by the dim emergency lamps. The air systems continue their steady hum."
    central_freight_bay.on_survey = "The vast, open space is dominated by rows of massive, stacked freight containers. The main lights are offline, leaving the area illuminated only by weak, intermittent emergency lamps. The air systems hum steadily, confirming the environment is stable\n\You know the power bus distribution panels are located in the sections accessed via the right corridor."
    central_freight_bay.is_open = False
    central_freight_bay.locked_description = "The door refuses to budge, but it's too dark to investigate why."
    deck_5_aft_utility.on_first_enter = "You can see nothing."
    deck_5_aft_utility.on_revisit = "You can see nothing in the darkness..."
    deck_5_aft_utility.on_survey = "You can see nothing in the darkness..."
    # Act 3
    cargo_staging_room.on_first_enter = "Act 3 - Arrival \n\n"
    cargo_staging_room.on_revisit = ""
    cargo_staging_room.on_survey = "This area is narrow and functional, designed for temporary holding and inspection of freight before it enters the main bay.\n\n The lights have turned back to normal."
    cargo_staging_room.is_event_trigger = True
    cargo_staging_room.room_event = cargo_staging_room_room_event
    cargo_staging_room.is_act_event_trigger = True
    cargo_staging_room.act_number = "3"
    cargo_staging_room.act_subtitle = "Arrival"
    deck_5_secure_pathway.on_first_enter = ""
    deck_5_secure_pathway.on_revisit = ""
    deck_5_secure_pathway.on_survey = "The space is largely dim, with several fluorescent ceiling strips short-circuited and gone black, leaving hazy pools of light only near the serviceable areas. The air is cold and quiet, confirming that systems on this deck are still struggling to maintain full power."
    deck_5_secure_pathway.is_event_trigger = True
    deck_5_secure_pathway.room_event = deck_5_secure_pathway_room_event
    service_access_hatchway.on_first_enter = ""
    service_access_hatchway.on_revisit = ""
    service_access_hatchway.on_survey = "This narrow, brightly lit passage is designed purely for utility transit and entry into secured areas. The walls are seamless and reinforced, with heavy metallic plates lining the floor."
    service_access_hatchway.is_event_trigger = True
    service_access_hatchway.room_event = service_access_hatchway_room_event
    msc_1.on_first_enter = ""
    msc_1.on_revisit = ""
    msc_1.on_survey = "The room is intensely hot, and the constant roar of ventilation fans is deafening. The lighting is dim, requiring you to use your flashlight to see clearly.\n\nThe walls are lined with exposed, thick conduits and heavy piping, confirming this area's role as a major utility junction. Ahead, a single, reinforced window overlooks MSC 2, a mirrored control station. The air is thick with the scent of hot metal."
    msc_1.is_event_trigger = True
    msc_1.room_event = msc_1_room_event
    msc_2.on_first_enter = ""
    msc_2.on_revisit = ""
    msc_2.on_survey = "This is no time for sight seeing! You quickly scan the room and see 3 potential hiding places:\n— BEHIND the Power Conduit Manifold\n— UNDER the Operator Console Deck\n— BEHIND the stacked Heavy Industrial Drums"
    msc_2.is_event_trigger = True
    msc_2.room_event = msc_2_room_event
    msc_2_b_storage_drums.on_first_enter = ""
    msc_2_b_storage_drums.on_revisit = ""
    msc_2_b_storage_drums.on_survey = f"You survey the room from your cover, your eyes darting low across the deck. The room is hot and loud, filled with the intense roar of ventilation fans. \n\nDim yellow emergency lighting casts long, eerie shadows that fluctuate with the failing power.\n\nThe colossal arachnid creature dominates the center of the floor. Its segmented body is approximately three meters long, and its spike-like legs stalk slowly over the deck plating. The rhythmic clicking of its limbs is now the loudest, most terrifying sound in the room.\n\nNear the floor behind you, you spot a loose inspection vent hatch. If you can carefully remove the heavy cover, you should gain access to the {msc_service_tunnel.name}."
    msc_2_b_storage_drums.is_event_trigger = True
    msc_2_b_storage_drums.room_event = msc_2_b_storage_drums_hiding_room_event
    msc_2_b_console_desk.on_first_enter = ""
    msc_2_b_console_desk.on_revisit = ""
    msc_2_b_console_desk.on_survey = msc_2_b_storage_drums.on_survey
    msc_2_b_console_desk.is_event_trigger = True
    msc_2_b_console_desk.room_event = msc_2_b_console_desk_hiding_room_event
    msc_2_b_power_conduit.on_first_enter = ""
    msc_2_b_power_conduit.on_revisit = ""
    msc_2_b_power_conduit.on_survey = msc_2_b_storage_drums.on_survey
    msc_2_b_power_conduit.is_event_trigger = True
    msc_2_b_power_conduit.room_event = msc_2_power_conduit_hiding_room_event
    msc_service_tunnel.on_first_enter = ""
    msc_service_tunnel.on_revisit = ""
    msc_service_tunnel.on_survey = "This wide conduit is pitch dark and smells sharply of ozone and old metal. The clicking of the creature's legs is amplified by the confined space, creating a terrifying percussive echo. The tunnel runs forward toward the ship's center."
    msc_service_tunnel.is_event_trigger = True
    msc_service_tunnel.room_event = msc_service_tunnel_room_event
    service_control_junction_5f.on_first_enter = ""
    service_control_junction_5f.on_revisit = ""
    service_control_junction_5f.on_survey = "This wide, functional room is filled with utility access panels and large conduits. You recognize this as a critical nexus for power and communication lines. \n\n The path to the next room is through a heavy structural blast door. The electronic lock mechanism appears on it appears to be fused shut and inaccessible"
    service_control_junction_5f.is_event_trigger = True
    service_control_junction_5f.room_event = service_control_junction_5f_room_event
    # Act 4
    operations_distribution_crossover.on_first_enter = "Act 4 - The Outer Decks. \n\n"
    operations_distribution_crossover.on_revisit = "The air remains cool and the lighting steady."
    operations_distribution_crossover.on_survey = "The air is cool and clean, and the lights are steady. The walls are lined with sealed maintenance panels, confirming its utility function."
    operations_distribution_crossover.is_open = False
    operations_distribution_crossover.locked_description = "The door won't budge..."
    operations_distribution_crossover.is_event_trigger = True
    operations_distribution_crossover.room_event = act_4_start
    operations_distribution_crossover.is_act_event_trigger = True
    operations_distribution_crossover.act_number = "4"
    operations_distribution_crossover.act_subtitle = "The Outer Decks"
    operations_and_cargo_interlink.on_first_enter = "This short, fortified corridor feels heavy and cold. The passage is dominated by three sealed doorways. To your left, a heavy security door has been completely destroyed, its metallic surface ripped and curled as if melted by immense, unnatural force. Right next to it, the door leading to Cargo Bay Control F remains intact but locked. Forward, a door leads to the External Ops Access Way. \n\nA small, specialized diagnostic console is mounted beside the Cargo Bay Control door, indicating the access system has failed and requires a unique technical bypass."
    operations_and_cargo_interlink.on_revisit = "You're back. The destroyed door remains untouched, and the Cargo Bay Control door is still sealed. The diagnostic console next to it is awaiting initiation."
    operations_and_cargo_interlink.on_survey = "This short, fortified corridor feels heavy and cold. The passage is dominated by three sealed doorways. \n\nTo your left, a heavy security door has been completely destroyed, its metallic surface ripped and curled as if melted by immense, unnatural force. Right next to it, the Cargo Bay Control F remains intact but locked.\n\nA small, specialized diagnostic console is mounted beside the Cargo Bay door, indicating the access system has failed and requires a unique technical bypass. \n\nForward, a door leads to the External Ops Access Way"
    cargo_bay_control_f.on_first_enter = "The room is wide and brightly lit. A massive window dominates the forward wall, offering a sweeping view of the vast, silent Cargo Bay below. Below the window, several control consoles are completely dark and inert.\n\nA heavy, cyan panel marked 'POWER BUS DISTRIBUTION PANEL' is bolted to the far right wall."
    cargo_bay_control_f.on_revisit = "room remains brightly lit and quiet, dominated by the massive window overlooking the Cargo Bay.\n\nThe Power Bus Distribution Panel remains accessible on the far right wall."
    cargo_bay_control_f.on_survey = "This wide, spacious office room is dedicated to overseeing logistics, with several control consoles currently dark and inert below the window. The lighting is bright and stable.\n\nThe forward wall is dominated by a massive, unreinforced window offering a sweeping view of the Cargo Bay. The bay below is a vast, expansive space, illuminated by stable industrial lamps. It is completely silent.\n\nA heavy, cyan panel marked 'POWER BUS DISTRIBUTION PANEL' is bolted to the far right wall."
    cargo_bay_control_f.is_open = False
    cargo_bay_control_f.locked_description = "The door doesn't budge. The console next to the door is awaiting input."
    external_ops_access_way.on_first_enter = "This short, narrow passage is well-lit and purely functional, serving as a clean link between the main spine and gearing up on EVA equipment."
    external_ops_access_way.on_revisit = "This short, functional corridor is brightly lit and quiet."
    external_ops_access_way.on_survey = "This narrow passage is well-lit and serves as a simple transport link. The walls are lined with standard utility paneling."
    eva_gear_lockers.on_first_enter = "It is a narrow staging bay lined with helmet racks and storage units. Secured to the wall is a dark, electronic locker, and through its clear panel, you can clearly see the SART (Systems Repair and Analysis Tool) unit locked inside..\n\nThere is what appears to be a screwdriver on the floor."
    eva_gear_lockers.on_revisit = "The room's equipment racks are mostly empty, and the SART locker remains a central point of interest. There is a screwdriver on the floor."
    eva_gear_lockers.on_survey = "The room is quiet and unnervingly cold. It is dedicated to storing external mission gear, though most racks are now empty. A specialized maintenance board stands next to a tool chest, and you see a small, precision screwdriver set attached to it.\n\nSecured prominently on the wall is a dark, electronic locker with the SART (Systems Analysis and Repair Tool) unit clearly visible behind its sealed high security glass panel. Normally you would open it by using your attached token id on your radio. The locker is centrally connected to the data servers that controls id data."
    central_utility_spine_5_f.on_first_enter = "This is the ship's main structural artery: a wide, brightly lit corridor designed for heavy traffic and equipment transfer. \n\nThe high ceiling is laced with exposed conduits and thick utility bundles, confirming its role as the central nervous system of Deck 5."
    central_utility_spine_5_f.on_revisit = "The wide corridor is brightly lit and quiet, dominated by the constant hum of utility bundles overhead."
    central_utility_spine_5_f.on_survey = "This wide, brightly lit artery runs the length of the ship's forward section. The floor is clearly marked with personnel and equipment transit lanes. The exposed conduits overhead are massive, confirming the importance of this route."
    central_utility_spine_4_f.on_first_enter = ""
    central_utility_spine_4_f.on_revisit = ""
    central_utility_spine_4_f.on_survey = ""
    central_utility_spine_4_f.is_open = False
    central_utility_spine_4_f.locked_description = "This heavy access door is severely damaged. The metallic surface is battered and buckled, and the automated locking mechanism has been ripped from its housing. The door frame is twisted, ensuring the passage is permanently sealed by physical force. "
    central_utility_spine_6_f.on_first_enter = "This wide corridor is impeccably clean and brightly lit, maintaining a much higher standard than the aft sections. The utility conduits are almost entirely sealed behind polished access panels. This corridor is designed for rapid personnel transit to the command area."
    central_utility_spine_6_f.on_revisit = "The wide corridor is brightly lit and quiet, maintaining a professional atmosphere."
    central_utility_spine_6_f.on_survey = "This wide corridor is impeccably clean and brightly lit, maintaining a high standard that reflects its purpose as the final approach to the command structure. The utility conduits are almost entirely sealed behind polished access panels, suggesting a focus on both security and rapid personnel transit. \n\nThe air hums with the steady sound of functional, high-priority systems."
    deck_5_forward_muster_station.on_first_enter = "This is an immense, brightly lit chamber, serving as the final staging area before the Bridge.\n\nThe security terminal for the bridge door is operational but showing some errors."
    deck_5_forward_muster_station.on_revisit = "The large chamber remains brightly lit and quiet.\n\nThe security terminal for the bridge door is operational but showing some errors."
    deck_5_forward_muster_station.on_survey = "This is a wide chamber designed for rapid personnel assembly, easily large enough to hold dozens of people. The space is mostly empty, furnished only with a few heavy, bolted-down benches near the walls. The lighting is bright and functional. This is the final staging area where bridge crew receive urgent instructions.\n\nThe security terminal for the bridge door is operational but showing some errors.\n\nThe only sound is a low, erratic hum from the failing auxiliary power conduits beneath the deck."
    systems_data_crossover.on_first_enter = "This is a narrow corridor running perpendicular to the Central Utility Spine, functioning as a major access link. The air is noticeably warm due to the waste heat bleeding through the reinforced server bay walls"
    systems_data_crossover.on_revisit = "The air remains noticeably warm, and the passage functions as a quick link between the main spine and the server bay."
    systems_data_crossover.on_survey = "This narrow corridor runs perpendicular to the ship's main axis, feeling noticeably warm due to the waste heat bleeding through the reinforced server bay walls. The walls are lined with thick data conduits."
    systems_data_access_corridor.on_first_enter = "This narrow passage is lined with high-capacity data conduits, and the air feels noticeably warm and electrically charged due to the nearby servers. It seems the console that would let access the Data Server Array is fried. The door seems fine mechanically though."
    systems_data_access_corridor.on_revisit = "The passage remains slightly warm and electrically charged, lined with silent data conduits. The Data Server Array door remains sealed.."
    systems_data_access_corridor.on_survey = "This narrow passage is lined with high-capacity data conduits, and the air feels noticeably warm and electrically charged due to the adjacent server bay.\n\nThe electronic access console to the Data Server Array is completely fried: the panel is melted and blackened, emitting a faint smell of burnt ozone.\n\nThe massive blast door leading to the Command Server Array is sealed shut. The door itself cannot be opened electronically, and the emergency mechanical lock beside it is seized.\nIf you could somehow manipulate the door's internal lock tumblers you might get the door open."
    data_server_array.on_first_enter = "The room is loud and cold, dominated by the relentless hum of the primary cooling systems. Though the ceiling is low, dozens of silent, black server racks stretch across the wide room, many displaying flickering red diagnostic lights. The central ICARUS Systems Terminal stands alone in the center, waiting for input.\n\n"
    data_server_array.on_revisit = "The room is loud, cold, and wide. The central ICARUS terminal remains active.."
    data_server_array.on_survey = "The room is loud and cold, dominated by the relentless hum of the primary cooling systems. Though the ceiling is low, dozens of silent, black server racks stretch across the wide room, many displaying flickering red diagnostic lights. The central ICARUS Systems Terminal stands alone in the center, waiting for input.\n\nAround the terminal are lots of scattered papers and sticky notes."
    data_server_array.is_open = False
    data_server_array.locked_description = "The door is locked as the electronic console that would let you in is completely fried.\n\nThe door's mechanical emergency lock looks fine though."
    executive_access_aisle.on_first_enter = ""
    executive_access_aisle.on_revisit = "The corridor remains quiet and impeccably maintained, serving its role as a high-security link."
    executive_access_aisle.on_survey = "This narrow corridor is impeccably maintained and quiet, emphasizing its purpose as a high-security link. The walls are smooth, sealed, and feature no exposed utilities."
    executive_access_aisle.is_event_trigger = True
    executive_access_aisle.room_event = meet_panicked_npc_executive_access_aisle
    captains_quarters.on_first_enter = ""
    captains_quarters.on_revisit = "The scene remains one of violent disarray. The captain's personal command vault is still sealed shut on the rear wall."
    captains_quarters.on_survey = "The room is a scene of utter destruction, with overturned furniture and warped metallic streaks across the far wall, confirming the immense force used by the organism. The Captain's body lies motionless on the deck.\n\nThe captain's personal command vault, a sturdy dark gray safe, remains bolted to the rear wall. Its standard electronic keypad access has been completely covered by an emergency metallic blast plate. The plate is held firmly in place by four heavy, visible structural welds."
    captains_quarters.is_event_trigger = True
    captains_quarters.room_event = captains_quarters_room_event
    command_transit_vestibule.on_first_enter = "This small, quiet entry chamber is dedicated entirely to moving personnel to the command structure. A short flight of stairs leads up to the Muster Station, and a heavy, sealed door leads to the Executive Access Isle."
    command_transit_vestibule.on_revisit = "The small chamber remains quiet, serving as the high-priority connection point."
    command_transit_vestibule.on_survey = "This small, hexagonal entry chamber is quiet and functional. The walls are seamless and reinforced."
    # Act 5
    bridge.on_first_enter = "Act 5 - Final Protocol"
    bridge.on_revisit = ""
    bridge.is_act_event_trigger = True
    bridge.act_number = "5"
    bridge.act_subtitle = "Final Protocol"
    bridge.is_event_trigger = True
    bridge.room_event = bridge_room_enter_event
    bridge.on_survey = "This is the nerve center of the Tantalus Horizon and the ship's primary command center, built around a crescent of control stations facing a massive forward viewport. The lights are stable and bright, the central main command console is showing multiple errors.\n\nOther consoles line the walls, displaying diagnostic readouts."
    bridge.is_open = False
    bridge.locked_description = "Next to the bridge door the Bridge Security Terminal screen glows amber. It confirms the access system is blocked critical hardware and security errors."
    vertical_service_shaft.on_survey = "This is a narrow, heavily armored maintenance chute that bypasses the intermediate decks, providing a direct, high-speed descent. Exposed conduit bundles and thick cable runs line the walls, disappearing into the darkness below.\n\nYou feel the immediate drop in air pressure and temperature, confirming you are leaving the main ship systems far behind. This is not a passage meant for crew comfort, but for rapid transit to the lower systems."    
    vertical_service_shaft.is_event_trigger = True
    vertical_service_shaft.room_event = vertical_service_shaft_room_event
    reactor_deck_service_hub.on_survey = "This small, heavily shielded room serves as the final buffer zone for the reactor core systems. The air here is noticeably warmer, and the walls are crisscrossed with thick, industrial piping and high-voltage conduits.\n\nStraight ahead, the reinforced door to the Auxiliary Reactor Control Room is visible. The door's lock mechanism is tied to the adjacent hydraulic systems, and you can clearly see the thick hydraulic fluid line running along the doorframe."
    reactor_deck_service_hub.is_event_trigger = True
    reactor_deck_service_hub.room_event = reactor_deck_service_hub_room_event
    auxiliary_reactor_control.on_survey = "This is a large, specialized control deck, approximately twenty meters long and ten meters wide. The air is warm and heavy. A massive, shielded reactor housing dominates the far end of the room. Exposed conduits and thick, heavy piping snake across the high walls.\n\nA single, heavy reinforced window is set into the wall on your left, looking directly into the Emergency Launch Compartment.\n\nIn the center of the room, a console with the Manual Nitrogen Purge Valve stands ready. Beside it, the ICARUS Reactor Terminal is active."
    auxiliary_reactor_control.is_event_trigger = True
    auxiliary_reactor_control.room_event = auxiliary_reactor_control_room_event
    emergency_launch_compartment.on_survey = "This small, heavily insulated room is designed purely for escape coordination. The console for operating the lifeboats sits prominently against the wall.\n\nYou can see the Chef clearly through the reinforced window, standing near the purge valve in the Auxiliary Reactor Control Room.\n\nRunning along the top of the internal access doorframe is the main hydraulic fluid line. You notice the line is severely warped and buckled—it will need some kind of leverage to manually fix the pinch before the launch system receives full pressure."
    emergency_launch_compartment.is_event_trigger = True
    emergency_launch_compartment.room_event = emergency_launch_compartment_room_event
    #Act 6
    emergency_launch_access_corridor.on_survey = "The air is bitterly freezing, and the air systems are failing. Illumination is fractured and chaotic. Bright red rotating alarm lights sweep the corridor in blinding flashes, interspersed with rapid yellow strobes from the failing emergency lamps. Exposed structural conduits are torn from the ceiling, confirming the extreme instability of the route."
    emergency_launch_access_corridor.on_first_enter = "Act 6 - The Exodus"
    emergency_launch_access_corridor.is_event_trigger = True
    emergency_launch_access_corridor.room_event = emergency_launch_access_corridor_room_event
    emergency_launch_access_corridor.is_act_event_trigger = True
    emergency_launch_access_corridor.act_number = 6
    emergency_launch_access_corridor.act_subtitle = "The Exodus"
    emergency_vehicles_bay.on_survey = "The expansive room is dominated by the vast, open structural framework of the launch cradle, which secures the Tantalus Ark in its firing position. The stable, warm lighting here is a sharp contrast to the corridor outside.\n\nThe Cutter Class vessel itself is intact and ready. At the far end of the bay, the massive external airlock door is currently sealed, but its hydraulic system shows a green light, confirming it is ready to cycle once the launch sequence is initiated. Your only objective remaining is to board the Ark and launch the craft."
    emergency_vehicles_bay.is_event_trigger = True
    emergency_vehicles_bay.room_event = emergency_vehicles_bay_room_event
    tantalus_ark.on_survey = "The cabin is compact and highly functional, built for two primary occupants. The hull plating surrounding the viewport is thick and heavily reinforced, offering reassurance against the dangers outside.\n\nThe main pilot console wraps around the command seat, featuring heavy physical toggles, analog gauges, and thick, matte-screen displays set behind reinforced glass. There are no delicate holographics here—just reliable, tactile controls. Strapped to the wall behind the seats is a sealed emergency provisions unit.\n\nThe main diagnostic screen glows green, confirming all systems are functional and ready for launch."
    tantalus_ark.is_event_trigger = True
    tantalus_ark.room_event = tantalus_ark_room_event
    tantalus_ark_final.on_survey = "You are asleep safely inside the Cryo unit..."

def setup_rooms():
    connect_all_initial_rooms()
    set_rooms_defaults()

## Items

# Item pickup events

def maintenance_jack_picked_up():
    crew_lockers.on_revisit = "You are back in the Crew Lockers. The room is silent and empty. Your locker is still open, and the rest of the facility remains functional but empty."
    crew_lockers.on_survey = "The room is large and empty, dominated by rows of metal lockers and two small shower stalls near the back wall. The facility is functional, immaculately clean, and the air is still slightly warm, suggesting it was used very recently."

def flashlight_picked_up():
    player.heartrate = "Calm"
    player.heartrate_color = "green"
    welder.can_take=True
    welder.on_look="It is a heavy, industrial-grade plasma torch used for emergency hull breaches and structural repair.\n It features a thick, reinforced handle and a large external coolant tank.\n It feels weighty and powerful, capable of cutting through the thickest metal found on the Tantalus Horizon."
    
    environmental_controls.on_revisit = "You enter the keycode and move in. The machines in the room make a continuous soft humming sound that is somehow soothing. \nThe space remains cold, functional."
    environmental_controls.on_survey = "The walls are covered in dense panels marked with fluid lines and thermal regulators. This room is clearly responsible for the ship's critical HVAC and air-scrubbing systems. All monitoring screens are currently dark, and a faint, high-pitched whine from the equipment indicates the systems are offline or struggling.."
    central_freight_bay_bulk_door.on_look ="The central freight bay door sits sealed and unyielding. \nA narrow panel clings to its side, warped and jammed, its edges surprisingly thin against the massive door. \n\nInside, you can just make out a tangle of rods and mechanisms. There must be some way to override the locks, if you can reach them. \n\nWhatever caused the door to fail, it won't budge without a careful approach."
    central_freight_bay.locked_description="The door refuses to budge. Its surface is cold and unyielding, and the panel to the side is jammed tight. Whatever shut it down, it won't open by hand."
    upper_aft_lobby.on_first_enter = "Your flashlight beam cuts through the gloom, revealing a wide, heavily paneled space. The silence here is profound, broken only by the faint hum of high-voltage systems behind the walls."
    upper_aft_lobby.on_revisit = "Your flashlight beam cuts through the gloom, revealing a wide, heavily paneled space. The silence here is profound, broken only by the faint hum of high-voltage systems behind the walls."
    upper_aft_lobby.on_survey = "You sweep your flashlight beam across the lobby. This wide, silent space functions as a waiting area, sparsely furnished with a few wide, bolted-down benches. The silence is broken only by the faint, high-pitched whine of dormant electronics behind the utility panels.\n\n"
    deck_5_aft_utility.on_first_enter = "It's a small, functional space dedicated to storing maintenance equipment, with heavy cabinets bolted to the walls. \nYour portable welder is sitting exactly where you left it on the central metallic shelf.\n\nYou briefly hear some strange clicking voice likely echoing from the vents above, but then it passes."
    deck_5_aft_utility.on_revisit = "The cabinets are closed, and the room is quiet.\nYour portable welder is sitting exactly where you left it on the central metallic shelf."
    deck_5_aft_utility.on_survey = "It's a small, reinforced space for specialized repair equipment. Heavy cabinets line the walls, and a secure floor hatch indicates access to the lower conduits. A central metallic shelf dominates the room, which currently holds only a few spare filters and coiled cables.\n\nYour portable welder is sitting exactly where you left it on the central metallic shelf."

def welder_picked_up():
    deck_5_aft_utility.on_revisit = "The cabinets are closed, and the room is quiet."
    deck_5_aft_utility.on_survey = "It's a small, reinforced space for specialized repair equipment. Heavy cabinets line the walls, and a secure floor hatch indicates access to the lower conduits. A central metallic shelf dominates the room, which currently holds only a few spare filters and coiled cables."

def engys_keycard_picked_up():
    medical_labs.on_revisit = "You're back. Enrique is still lying on the floor motionless."
    medical_labs.on_survey = "The space is cold and sterile, equipped with specialized emergency diagnostic machines. \n\nHigh Engineer Enrique's body is lying motionless on the deck. His eyes are open, wide with silent surprise. \n\nYou detect a sharp, acrid scent of ozone and burnt wiring insulation, confirming a severe electrical disaster occurred here. You think it's most likely the air was drained due to some faulty electronics.\n\n You allow yourself a moment of quiet reflection. You remember the crew always called him Engy.\nThough you two didn't know each other well, he seemed like the easy going type who wasn't a stickler for the rules. You remember hearing he had gotten into trouble with the Captain a couple of times..."

def screwdriver_picked_up():
    eva_gear_lockers.on_revisit = "The room's equipment racks are mostly empty, and the SART locker remains a central point of interest."
    eva_gear_lockers.on_survey = "The room is quiet and unnervingly cold. It is dedicated to storing external mission gear, though most racks are now empty. \n\nSecured prominently on the wall is a dark, electronic locker with the SART (Systems Analysis and Repair Tool) unit clearly visible."

def lockpick_picked_up():
    operations_distribution_crossover.on_revisit = "The air remains cool and the lighting steady."
    operations_distribution_crossover.on_survey = f"This corridor is narrow and reinforced, designed for limited crew transit between the central spine and the external operation staging areas. The walls are smooth, and the overhead utilities are secured and caged."

def sart_picked_up():
    sart.on_look="It is the System Analysis and Repair Tool. Can be used for diagnostics, using and repairing consoles."


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
        debug_info="Radio broken down",
        on_look="This is an industrial-grade handheld radio, secured to the strap of your backpack. The casing is cracked and scorched, suggesting it survived a severe electrical shock. The unit is broken and seems incapable of transmitting anything."
    ),

    "maintenance_jack": Item(
        id="maintenance_jack",
        name="Jack",
        keywords=["maintenance jack", "maintenance", "jack", "maintenancejack"],
        is_item_pickup_event_trigger= True,
        item_picked_up_event=maintenance_jack_picked_up,
        debug_info="Medium sized maintenance tool for turning things",
        on_look="The maintenace jack is designed to be carried for field maintenance, capable of applying immense, focused leverage to pry apart seized components."
    ),

    "engys_keycard": Item(
        id="engys_keycard",
        name="Keycard",
        keywords=["keycard", "card", "key", "engy"],
        debug_info="High Engineer Enrique's keycard.",
        on_look="The keycard reads: High Engineer Enrique 4277",
        is_item_pickup_event_trigger=True,
        item_picked_up_event=engys_keycard_picked_up
    ),

    "flashlight": Item(
        id="flashlight",
        name="Flashlight",
        keywords=["flashlight", "light", "flash"],
        debug_info="Handheld flashlight.",
        on_look="Small non-industrial handheld flashlight with low cone of light. It offers only limited illumination, but it looks functional and is better than nothing. ",
        is_item_pickup_event_trigger=True,
        item_picked_up_event=flashlight_picked_up
    ),

    "welder": Item(
        id="welder",
        name="Welder",
        keywords=["welder", "portable"],
        on_look="If there is a welder here, you can't see where it is.",
        debug_info="Hand usable welder.",
        can_take=False,
        locked_description="If there is a welder here, you can't see where it is.",
        is_item_pickup_event_trigger=True,
        item_picked_up_event=welder_picked_up
    ),

    "lockpick": Item(
        id="lockpick",
        name="Lockpick",
        keywords=["lockpick", "key", "pick", "lock"],
        debug_info="Dropped lockpick by Tanaka. Opens Server Array.",
        on_look="It is a Specialized Lockpick Set, secured in a compact, polymer case. It's not designed for standard key locks, but for precision manipulation of complex lock tumblers and override mechanisms. This is exactly the kind of tool needed to bypass the high-security locks found on the Tantalus Horizon.",
        is_item_pickup_event_trigger=True,
        item_picked_up_event=lockpick_picked_up
    ),

    "screwdriver": Item(
        id="screwdriver",
        name="Screwdriver",
        keywords=["screwdriver", "screw", "driver"],
        debug_info="Screwdriver on the floor of EVA room.",
        on_look="The standard issue tool for disassembling small electronics and fine mechanical parts, like sealed access panels or delicate system boards.",
        is_item_pickup_event_trigger=True,
        item_picked_up_event=screwdriver_picked_up
    ),
    "sart": Item(
        id="sart",
        name="SART",
        keywords=["sart", "system", "systems" , "analysis", "repair", "tool"],
        debug_info="System Analysis and Repair Tool.",
        on_look="It is the System Analysis and Repair Tool. Can be used for diagnostics, using and repairing consoles.",
        can_take=False,
        locked_description="It is locked behind a bulletproof glass panel with token identifier next to it.",
        is_item_pickup_event_trigger=True,
        item_picked_up_event=sart_picked_up
    ),
    "bridge_access_cypher": Item(
        id="bridge_access_cypher",
        name="Cypher",
        keywords=["cypher", "bridge", "access", "access cypher", "bridge access cypher"],
        debug_info="Captain's quarters vault you find this.",
        on_look="This is the Bridge Access Cypher, a small, black ceramic token with crystalline edges. It holds the cryptographic key necessary to bypass the ship's primary electronic security."
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

def setup_items():
    # Act 1
    crew_lockers.items["backpack"] = backpack
    crew_lockers.items["maintenance_jack"] = maintenance_jack
    crew_lockers.items["radio"] = radio
    # Act 2
    medical_labs.items["engys_keycard"] = engys_keycard
    environmental_controls.items["flashlight"] = flashlight
    deck_5_aft_utility.items["welder"] = welder
    # Act 3

    # Act 4
    eva_gear_lockers.items["screwdriver"] = screwdriver
    eva_gear_lockers.items["sart"] = sart

# Interactables functions

def interacted_cryo_terminal():
    player.output +="You know this terminal is just for displaying status reports. You access the terminal's core diagnostics. The screen stabilizes, displaying the ship's operational manifest:\n\n"
    player.output +="ICARUS SYSTEMS STATUS REPORT VESSEL: The Tantalus Horizon.\n"
    player.output +="OPERATIONS: All local systems operational.\n"
    player.output +="POWER DISTRIBUTION REPORT: Multiple minor power fluctuations detected in Midship Sections D4 and D5."

def interacted_msc_2_vent_cover():
    player.enter_room(msc_service_tunnel)

def interacted_icarus_systems_terminal():
    print("--------------------------------------------------")
    print(">>> ICARUS SYSTEMS V6.1.4: PRIMARY ACCESS CONSOLE <<<")
    print("--------------------------------------------------")
    print("INIT: Power Bus Tie [STATUS: NOMINAL]")
    print("INIT: Command Data Link [STATUS: ONLINE]")
    print("DIAG: Reactor Core Telemetry . . . . . . . . . . [PASS]")
    print("DIAG: Life Support HVAC . . . . . . . . . . . . [PASS]")
    print("CHECK: Airlock Regulator Lockouts . . . . . . . [WARNING]")
    print("CHECK: External Communications Module. . . . . . [FAILURE]")
    print("SYSTEMS: Access protocol engaged. Awaiting input.")
    print("--------------------------------------------------")
    login = input("Please enter login")
    password = input("Please enter password")
    if login == "admin" and password == "1234":
        eva_lockers_sars_locker.on_look = "The lockers are open and you can take the SART equipment."
        eva_lockers_sars_locker.use_func = eva_lockers_sars_locker_radio_used_after_server_use
        sart.can_take = True
        sart.on_look = "The lock is open and the sart can be taken."
        
        player.output += "You gain root access to the terminal. It seems like Tanaka was less concerned with breaches and more concerned with remembering the code before their coffee wore off.\n\n"
        player.output += "Using your credentials, you manually overload the transmission array and inject a high-power, one-time authorization token directed specifically at the EVA Prep Room.\n"
        player.output += "The terminal flashes a final confirmation: TOKEN INJECTED. TARGET LOCK OVERRIDDEN.\n"
        player.output += "You log out of the terminal."
    else:
        player.output_error = "Incorrect login or password."

def interacted_tantalus_ark_console():
    if tantalus_ark_console.amount_interacted_with == 0:
        tantalus_ark.on_survey = "The structural frame of the vessel is shuddering constantly, and the airlock hydraulics are screaming as the outer hatch fails to seal.\n\nThe creature's immense, scarred form is pressed directly against the viewport, completely filling your forward view. Its spiked legs are visibly anchored to the launch rail structure, creating an insurmountable physical obstruction.\n\nYou have no time to go outside to deal with the problem, it's time to try initiating the launch sequence again."
        
        player.output_fast   += "The alarm blares **EMERGENCY MELTDOWN SEQUENCE ACTIVE. T-MINUS ONE MINUTE, THIRTY SECONDS.**\n\n"
        player.output_normal += "You slam your hand down on the activation switch. The cabin lights surge, and the heavy launch cradle retracts with a deafening hydraulic screech.\n"
        player.output_normal += "The Tantalus Ark shudders violently and begins to slide forward on the magnetic rails. The outer airlock hatch starts to cycle open.\n\n"
        player.output_normal += "Just as you feel the magnetic acceleration kick in, the vessel is struck by an impossibly heavy, metallic impact. A colossal, scarred figure slams against the pilot viewport.\n"
        player.output_normal += "The launch sequence immediately aborts. The creature has anchored its immense, spiked legs deep into the magnetic launch rail structure, locking the Ark in place.\n"
        player.output_normal += "The launch cradle screams under the external pressure, and your console flashes: **'LAUNCH RAIL OBSTRUCTION.'** \n\n"
        player.output_normal += "You hope starting the launch sequence again will work."
    elif tantalus_ark_console.amount_interacted_with == 1:
        tantalus_ark.on_survey = "The violent impact and subsequent pin of the creature caused the vessel to shudder, but the structural integrity is holding. The airlock hydraulics have successfully completed their cycle, readying the final launch stage.\n\nThe main diagnostic screen now glows with a steady GREEN light, confirming: OBSTRUCTION CLEARED.\nThe viewport offers a devastating view of the launch bay: the Chef's industrial lifter is stalled and crushed against the structural rail, pinning the colossal arachnid creature. Both are motionless.\n\nYour focus locks on the countdown: The main control panel flashes T-MINUS THIRTY SECONDS, demanding immediate action. The silence is now the heaviest danger."

        player.output_fast   += "The alarm blares **EMERGENCY MELTDOWN SEQUENCE ACTIVE. T-MINUS ONE MINUTE.**\n\n"
        player.output_fast   += "The main control panel screams: 'LAUNCH ABORTED. EXTERNAL OBSTRUCTION.'\n" 
        player.output_normal += "Suddenly, the silence is annihilated by the sound of heavy machinery being violently accelerated. A large, dark shape hurtles across the launch bay floor.\n"
        player.output_normal += "It's the Chef! He is driving an industrial maintenance lifter, a heavy, low-profile vehicle, directly toward the massive arachnid.\n"
        player.output_normal += "Chef (shouting, voice distorted by the radio): One small step for man, one giant squish for spiderkind!\n"
        player.output_normal += "The impact is colossal. The creature shrieks as it's violently thrown against the far wall. The industrial lifter stalls, pinned between the creature and the rail.\n"
        player.output_normal += "The ship's computer flashes green: **'OBSTRUCTION CLEARED. LAUNCH SEQUENCE RESUMED.'**\n"
        player.output_normal += "Your control panel flashes: **T-MINUS THIRTY SECONDS.** \n\n"
        player.output_normal += "You don't have time to rescue Chef. You have one last chance to initiate the launch sequence.\n"
    elif tantalus_ark_console.amount_interacted_with == 2:
        player.enter_room(tantalus_ark_final)

        player.output_fast += "You slam your hand onto the activation switch. The Ark's console immediately blazes with green light, confirming the sequence.\n\n"
        player.output_fast += "**'LAUNCH INTEGRITY 100%.'**\n\n"
        player.output_fast += "The vessel roars to life, and the cabin lights lock down to safety red.\n"
        player.output_fast += "The internal hatch seals with a heavy thud, separating you from the launching bay and the creature's hideous form.\n\n"
        player.output_fast += "Through the viewport, you see the Chef, pinned by the industrial lifter, look back at your vessel. He raises a hand in a final salute as the massive external airlock begins its cycle, sealing the entire launch bay.\n"
        player.output_normal += "Chef (through the radio, his voice sounding strained): Sorry, eight-legs, this ship already has a countdown, and you're out of time.\n\n"
        player.output_normal += "[SYSTEMS: EXTERNAL SEAL CONFIRMED. IGNITING LAUNCH ACCELERATORS!]\n\n"
        player.output_normal += "The Tantalus Ark punches forward, ripping free of the dying station. You watch through the viewport as the hull of the Tantalus Horizon shudders one final, agonizing time.\n"
        player.output_normal += "The central reactor core goes critical in a silent, blinding flash of white energy. The immense ship collapses into itself, consumed by the meltdown and the void.\n"
        
        player.output_slow += "You are alone, but alive.\n\n"
        player.output_slow += "You turn on the emergency beacon and enter the containment cryo unit within The Tantalus Ark.\n\n"
        player.output_slow += "Your signal is all you have now. Because in the vastness of space, no one can hear you scream...\n\n\n"
        
        player.output_slow += "THE END."

        
# Interactables data

initial_interactables = {
    "cryo_bay_diagnostics_terminal": Interactable(
        id="cryo_bay_diagnostics_terminal",
        name="Cryo Bay Diagnostics Terminal",
        keywords=["terminal", "console", "terminal console","diagnostics", "diagnostic", "keyboard"],
        debug_info="Act 1 Broken down door, open with jack",
        on_look="The Cryo Bay Diagnostics Terminal is an embedded panel displaying a faint, steady green light. This unit is active and waiting for a system query.",
        on_interact_func=interacted_cryo_terminal
    ),
     "msc_2_vent_cover": Interactable(
        id="msc_2_vent_cover",
        name="MSC2 Vent Cover",
        keywords = ["inspection","vent", "hatch", "cover", "frame", "duct", "ventilation","hole", "shaft", "escape", "grate", "grille"],
        debug_info="Vent cover that needs to be removed for escape.",
        on_look="You focus on the vent near the floor. It's a standard-sized service access hatch, secured by a heavy metal grille. The frame looks severely warped, and the screws are loose and jutting out due to the structural shock. You realize the cover isn't properly seated; you could likely pry the heavy grille free with effort.",
        on_interact_func=interacted_msc_2_vent_cover,
    ),
    "icarus_systems_terminal": Interactable(
        id="icarus_systems_terminal",
        name="ICARUS Systems Terminal",
        keywords = ["terminal", "console", "icarus", "systems", "data", "note", "notes", "sticky", "sticky notes", "paper", "papers"],
        debug_info="Main systems terminal inside Data Server Array.",
        on_look="The ICARUS Systems Terminal is a heavy-duty, reinforced console built directly into the floor. Its primary interface is fully active, displaying a sequence of high-level network protocols demanding authentication. \n\nYou note the massive auxiliary power connection required to run it, hinting at its high signal output capability. \n\nRight next to the interface, a faded yellow sticky note is secured to the console, bearing the text: admin 1234.",
        on_interact_func=interacted_icarus_systems_terminal,
    ),
    "tantalus_ark_console": Interactable(
        id="tantalus_ark_console",
        name="Tantalus Ark Cockpit Console",
        keywords=["terminal", "console", "terminal console", "cockpit", "systems", "ignite", "initiate", "pilot", "launch", "sequence"],
        debug_info="Last location and last interactable.",
        on_look="The main pilot console wraps around the command seat, featuring heavy physical toggles, analog gauges, and thick, matte-screen displays set behind reinforced glass.",
        on_interact_func=interacted_tantalus_ark_console,
    ),
}

cryo_bay_diagnostics_terminal = initial_interactables["cryo_bay_diagnostics_terminal"]
icarus_systems_terminal = initial_interactables["icarus_systems_terminal"]
tantalus_ark_console = initial_interactables["tantalus_ark_console"]
msc_2_vent_cover = initial_interactables["msc_2_vent_cover"]

def setup_interactables():
    cryo_bay.interactables["cryo_bay_diagnostics_terminal"] = cryo_bay_diagnostics_terminal
    msc_2_b_storage_drums.interactables["msc_2_vent_cover"] = msc_2_vent_cover
    msc_2_b_power_conduit.interactables["msc_2_vent_cover"] = msc_2_vent_cover
    msc_2_b_console_desk.interactables["msc_2_vent_cover"] = msc_2_vent_cover
    data_server_array.interactables["icarus_systems_terminal"] = icarus_systems_terminal
    tantalus_ark.interactables["tantalus_ark_console"] = tantalus_ark_console


## use_targets functions

# Act 1
def mess_hall_blast_door_used():
    player.output = f"You position the {maintenance_jack.name} against the fused door frame and apply the hydraulics. The metal groans loudly under the increasing pressure. With a final, explosive CRACK of stressed metal, the seized frame bends outward, and the locking mechanism snags free. \n\nThe door pops open, giving you passage forward."
    galley.on_survey = "This small space is tidy but shows signs of regular use, dominated by heavy stainless steel counters and several polished wooden dining tables. The area smells faintly of strong brewed coffee and cooking oil, reflecting recent activity. The food preparation area is pristine."

    cryo_midship_transfer_passageway.is_open = True
# Act 2
def central_freight_bay_blast_door_used():
    player.output = "Freight bay blast door used"
    central_freight_bay.is_open = True

    player.output += "The Welder hisses, and the thin metal of the access panel shrieks under the intense heat before falling away in a cascade of molten slag. You quickly aim the torch at the exposed locking mechanism's primary circuit and fuse the seizure point.\n\n"
    player.output += "With a heavy, mechanical groan, the final mechanism disengages and the lock gives."

def env_controls_access_panel_use_keypad():
    passcode = input("Keycard detected. Please enter passcode")
    if passcode == "4277":
        player.output="Code verified. Access granted."
        environmental_controls.is_open = True
    else:
        player.output_error="Code invalid. Access denied."
# Act 3
def service_control_junction_5f_door_used():
    service_control_junction_5f_door.on_look = "You examine the heavy, structural blast door. A rough, smoking hole has been cut through the access panel, bypassing the fused original lock. The door's mechanism is now fully restored and functional."
    operations_distribution_crossover.is_open = True
    service_control_junction_5f.on_survey = "This wide, functional room is filled with utility access panels and large conduits. You recognize this as a critical nexus for power and communication lines. \n\n The path to the next room is through a heavy structural blast door."
    player.output += "\nThe Welder screams, and the access panel metal shrieks under the intense heat before melting away. You quickly cut a precise hole, exposing the tangled internal wiring and manual release mechanism of the door lock. The door should open now."
# Act 4
def operations_and_cargo_interlink_console_used():
    player.output += f"The door next to the console clicks and the lock to {cargo_bay_control_f.name} is open."
    cargo_bay_control_f.is_open = True
    operations_and_cargo_interlink.on_revisit = ""
    operations_and_cargo_interlink.on_survey = "The door is open. There is not much of interest here."

def cargo_bay_control_f_power_bus_used():
    player.heartrate = "Elevated"
    player.heartrate_color = "orange3"

    game.act_4_bridge_powered = True
    cargo_bay_control_f.is_open = False
    player.output_fast += "You finish forcing the lever, and the power bus hums back to life. Just then, you glance out the massive control room window into the Cargo Bay. You spot Tanaka, still in his technician uniform, moving erratically across the deck below. He seems completely lost and disoriented. \n\nA sudden impossibly large shadow stretches across the cargo bay floor, falling from the high ceiling where no shadows should exist. You look up and see the colossal arachnoid creature dropping like a silent anchor, instantly closing the distance to the floor. The terrifying clicking sound begins, sharp and deafening, echoing up from the vast bay. \n\nInstinct takes over and you duck low behind the inert consoles, shielding your eyes. You don't see the impact, but the clicking quickly gives way to a sickening, muffled crunch and a brief, strangled cry that is abruptly cut short. When the silence returns, it is heavy and absolute. You know Tanaka didn't make it..."
    cargo_bay_control_f.on_first_enter = "You duck on the floor to not be seen through the large window. This is no time to look around, the arachnid creature might still be there in the cargo bay."
    cargo_bay_control_f.on_revisit = "You duck on the floor to not be seen through the large window. This is no time to look around, the arachnid creature might still be there in the cargo bay."
    cargo_bay_control_f.on_survey = "You are ducking on the floor to not be seen through the large window. This is no time to look around, the arachnid creature might still be there in the cargo bay."
    bridge_errors_check()

def eva_lockers_sars_locker_radio_used_before_server_use():
    player.output += "You try to wave your radio's embedded ID token on the locker's sensor. The lock mechanism gives a faint, dead click. \n"
    player.output += "The radio's ID token usually works to open this locker, but the broken radio is unable to communicate the necessary security handshake. \n"
    player.output += "The locker is centrally connected to the data servers that control ID and access data."

def eva_lockers_sars_locker_radio_used_after_server_use():
    player.output += "The locker is already open."

def personal_command_vault_welder_used():
    player.output += "You pull the Welder away as the metal cools. Your hand is shaking from the heat of the torch, and the air smells like ozone. The protective blast plate clangs heavily onto the floor, revealing the electronic lock mechanism.\n\nThe inner access panel is seized shut and secured by four tiny, specialized security screws."
    player.cur_room.remove_use_target(personal_command_vault_before_weld)
    player.cur_room.add_use_target(personal_command_vault_after_weld)

def personal_comand_vault_screwdriver_used():
    player.output += "You manage to carefully remove the four specialized screws with the tip of the tool. The seized access panel pops open, revealing the battery housing and the main solenoid. You quickly bypass the jam, and the lock mechanism whirs back to life with a satisfying click.\n\nInside the small compartment, resting on a velvet cushion, is a small, black ceramic token. You recognize it instantly: the Bridge Access Cypher."
    player.cur_room.remove_use_target(personal_command_vault_after_weld)
    player.cur_room.add_scenery(personal_command_vault_complete)
    player.cur_room.add_item(bridge_access_cypher)
    player.take("cypher")

def data_array_door_lockpick_used():
    data_server_array.is_open = True
    player.output += "You hear a click and the door opens."

def bridge_door_console_cypher_used():
    player.output = "AUTHORIZATION SUCCESSFUL. \n\nOne of the errors disappeared."
    game.act_4_bridge_authorized = True
    bridge_errors_check()

def bridge_errors_check():
    if game.act_4_bridge_powered:
        bridge_security_terminal.on_look = "It is a thin, reinforced diagnostic panel built into the wall beside the Bridge's main hatch. The screen is active but glows with a frustrated amber caution light. A scrolling list of diagnostic errors is displayed, blocking access: \n\nERROR 02: SECURITY CLEARANCE REQUIRED \n\nYou realize this terminal doesn't open the door, but diagnoses why the door won't open. Beneath the display, a secure interface socket is visible, designed to accept a high-level cryptographic cypher for verification."
    if game.act_4_bridge_authorized:
        bridge_security_terminal.on_look = "It is a thin, reinforced diagnostic panel built into the wall beside the Bridge's main hatch. The screen is active but glows with a frustrated amber caution light. A scrolling list of diagnostic errors is displayed, blocking access: \n\nERROR 01: POWER BUS DISRUPTION \n\nYou realize this terminal doesn't open the door, but diagnoses why the door won't open. Beneath the display, a secure interface socket is visible, designed to accept a high-level cryptographic cypher for verification."
    if game.act_4_bridge_powered and game.act_4_bridge_authorized:
        bridge.is_open = True
        bridge_security_terminal.on_look = "The Bridge Security Terminal now glows with a steady, functional green light. The screen displays a single, static message: ACCESS GRANTED. ALL SYSTEMS NOMINAL. The Cypher slot remains empty, indicating your task here is complete."
        if player.cur_room.id == deck_5_forward_muster_station.id:
            player.output = "The amber caution light on the terminal flashes green, and the diagnostic errors vanish. The ICARUS SYSTEMS screen flashes ACCESS GRANTED - MANUAL OVERRIDE DEACTIVATED"
        
        deck_5_forward_muster_station.on_revisit = "The large chamber remains brightly lit and quiet.\n\nThe security terminal for the bridge door is operational."
        deck_5_forward_muster_station.on_survey = "This is a wide chamber designed for rapid personnel assembly, easily large enough to hold dozens of people. The space is mostly empty, furnished only with a few heavy, bolted-down benches near the walls. The lighting is bright and functional. This is the final staging area where bridge crew receive urgent instructions.\n\nThe security terminal for the bridge door is operational."


# Act 5
def emergency_launch_compartment_hydraulic_pipe_used():
    player.heartrate = "High"
    player.heartrate_color = "red"

    emergency_launch_compartment.backward = emergency_launch_access_corridor
    emergency_launch_compartment.on_survey = "The confined space is filled with the sharp, sterile scent of ozone and cryogenics, and the air is intensely cold due to the radiation from the neighboring room.\n\nThe small console for the lifeboats is flashing GREEN and shows the running countdown: T-MINUS 03:30 AND COUNTING.\n\nThe reinforced window overlooking the Auxiliary Reactor Control Room is completely obscured by a thick, swirling white cloud of liquid nitrogen fog, confirming the Chef successfully initiated the purge.\n\n"

    player.output_normal += "You manage to straighten the warped pipe. You can hear softly the fluid flowing inside it.\n"
    player.output_normal += "You hear crackling on your radio.\n\n"
    player.output_normal += "Chef: Good one Nat! I'm starting the meltdown sequence.\n\n"
    player.output_normal += "Before the Chef even finishes speaking, the terrifying, rhythmic clicking begins right outside the door.\n"
    player.output_normal += "Suddenly, the colossal arachnid creature appears outside of the Auxiliary Reactor Control Room door, its segmented legs scrambling for purchase on the frame.\n"    
    player.output_normal += "The Chef sees the giant arachnid pierce a corrosive acid pipe above the door. The door instantly begins to melt.\n\n"
    player.output_normal += "Chef: Aww hell naww!\n\n"
    player.output_normal += "The spider quickly ducks below the door and enters the room.\n\n"
    player.output_normal += "Chef: Get back, you ugly**! This ain't my first barbecue!\n\n"
    player.output_normal += "Chef readies his flamethrower and blasts the arachnid with intense flame.\n"
    player.output_normal += "The creature takes a few hesitant steps back, as if startled by the heat. Then, it calmly walks straight through the flame and slams the Chef into the wall next to the terminal.\n"
    player.output_normal += "The immense spider turns its attention to you, looking through the thick glass of your compartment window.\n\n"
    player.output_normal += "**Reactor Alarm blares: SEQUENCE READY.**\n\n"
    player.output_normal += "Chef (whispering over the radio, barely alive): Nat... This dinner is served cold.\n\n"
    player.output_normal += "Chef presses the final purge button. Through the glass you see a torrent of white, freezing gas and liquid nitrogen instantly filling the Reactor Room.\n\n"

    player.output_normal += "Suddenly a nearby pressure relief valve from the pipe you just fixed fails, rupturing with a deafening hiss. A blast of white cryogenic vapor hits your right leg.\n"
    player.output_normal += "Your ankle joint locks instantly, sending a searing stab of hypothermic pain up your leg. You stumble back with a high pitched whail.\n"
    player.output_normal   += "The burn is severe, you can barely put any weight on your right leg without feeling immense pain.\n\n" 
    player.output_normal += "You realize you can't help your friend...\n\n"

    player.output_normal += "The main reactor alarm blares violently. A synthetic voice screams: **FOUR MINUTES UNTIL CORE MELTDOWN.**\n"
    player.output_normal += "You take a bit of time and use the console to activate the lifeboat system. The console confirms the locks are disengaged.\n\n"
    player.output_normal += "The main reactor alarm blares again. A synthetic voice screams: **EMERGENCY MELTDOWN SEQUENCE ACTIVE. T-MINUS THREE MINUTES, THIRTY SECONDS.**\n"

    player.output_normal += "It's time to move."

# use_targets data

initial_use_targets = {
    "galley_blast_door": UseTarget(
        id="galley_blast_door",
        name="Mess Hall Blast Door",
        keywords = ["door", "blast", "blast door", "blastdoor", "broken door", "broken down door"],
        debug_info="Act 1 Broken down door, open with jack",
        on_look="You observe the heavy metallic edge of the Blast Door. The emergency hydraulic bolts are partially retracted, but the frame is visibly seized and fused. There are no electronic panels or keypads visible; the mechanism appears to be locked purely by immense mechanical pressure. This is a job for focused, brute force.",
        use_func=mess_hall_blast_door_used),
    "env_controls_access_panel": UseTarget(
        id="env_controls_access_panel",
        name="Environmental Control Access Panel",
        keywords = ["access panel", "panel", "door", "keypad", "keypanel", "console", "terminal", "security", "keylogger"],
        debug_info="Act 2 keypad to Environmental Controls.",
        on_look="A compact keypad and card swipe terminal connected to the ship's security network. Its small green display sits blank, awaiting input.",
        use_func=env_controls_access_panel_use_keypad),
    "central_freight_bay_bulk_door": UseTarget(
        id="central_freight_bay_bulk_door",
        name="Central Freight Bay Bulk Door",
        keywords = ["door", "blast door", "blastdoor", "broken door", "broken down door"],
        debug_info="Act 2 Broken down door, open with welder",
        on_look="It's too dark to see anything.",
        use_func=central_freight_bay_blast_door_used),
    "service_control_junction_5f_door": UseTarget(
        id="service_control_junction_5f_door",
        name="Heavy Door",
        keywords = ["door", "blastdoor", "bulk", "electronic", "lock", "frame", "handle", "blast", "structural", "heavy"],
        debug_info="Heavy door that needs welder to make a hole to get through.",
        on_look="You examine the heavy, structural blast door. The frame is sound, but the entire electronic lock and manual override are completely fused shut and inaccessible. The metal is thick, making the door impenetrable by force. \n\nYou realize the only way to bypass the mechanism and gain entry is to cut a small, precise hole through the adjacent access panel large enough to reach the manual controls inside.",
        use_func=service_control_junction_5f_door_used,),
    "logistics_door_console": UseTarget(
        id="logistics_door_console",
        name="Logistics Access Console",
        keywords = ["console", "terminal", "panel", "logistics", "logistics console", "diagnostic", "diagnostics", "diagnostic console", "door"],
        debug_info="Console that needs SART to be used on it.",
        on_look="It is a small, specialized terminal mounted beside the door. It has an exposed electronic interface port but no keypad or manual override. It is waiting for a high-level diagnostic tool to handshake with the security lock and initiate access.",
        use_func=operations_and_cargo_interlink_console_used),
    "power_bus_distribution_panel": UseTarget(
        id="power_bus_distribution_panel",
        name="Power Bus Distribution Panel",
        keywords = ["power","bus", "distribution", "panel", "closet", "cabinet"],
        debug_info="Act 4 power bus unit inside cargo_bay_control_f. Use maintenance jack.",
        on_look="It is a heavy, gray metallic cabinet bolted to the wall, humming loudly with suppressed voltage. The automated controls are dark, but the manual override lever is visible behind a reinforced safety grate. This bus controls the dedicated line feeding the Command Deck and Bridge systems. The lever is clearly seized solid due to immense pressure and heat and will not budge by hand. The only way to restore power is by applying extreme, focused leverage.",
        use_func=cargo_bay_control_f_power_bus_used,),
    "eva_lockers_sars_locker": UseTarget(
        id="eva_lockers_sars_locker",
        name="EVA SART Locker",
        keywords = ["door", "locker", "lockers"],
        debug_info="Act 3 locker that holds SART item. Purely visual. On radio used, just a text prompt.",
        on_look="This locker holds multiple SART tools. Usually you would activate it with your radio but the radio transmitter is broken.\n\nThe locker is centrally connected to the data servers that controls id data.",
        use_func=eva_lockers_sars_locker_radio_used_before_server_use),
    "personal_command_vault_before_weld": UseTarget(
        id="personal_command_vault_before_weld",
        name="Personal Command Vault",
        keywords = ["vault", "personal", "personal vault", "safe", "command"],
        debug_info="Act 4 captains safe",
        on_look="The Personal Command Vault is a sturdy, dark gray safe bolted to the rear wall. The unit itself appears undamaged. The standard electronic keypad access has been completely covered by an emergency metallic blast plate, suggesting a high-level, automated lockdown. This plate is held firmly in place by four heavy, visible structural welds and cannot be removed without cutting the seals.",
        use_func=personal_command_vault_welder_used),
    "personal_command_vault_after_weld": UseTarget(
        id="personal_command_vault_after_weld",
        name="Personal Command Vault",
        keywords = ["vault", "personal", "personal vault", "safe", "command"],
        debug_info="Act 4 captains safe",
        on_look="The Personal Command Vault is now partially open. The protective blast plate lies on the floor beside it, exposing the inner electronic lock mechanism.\n\nThe mechanism's small access panel is seized shut and secured by four tiny, specialized security screws.\n\nTo get inside, you'll need to find a way past that last, delicate barrier.",
        use_func=personal_comand_vault_screwdriver_used),
    "data_array_door": UseTarget(
        id="data_array_door",
        name="Data Array Door",
        keywords = ["door", "data", "array", "systems", "lock"],
        debug_info="Data Server Array room broken down door. Use lockpick to open.",
        on_look="The destruction of the console has rendered the primary lock useless. The emergency mechanical lock tumblers are visible in a small recess next to the frame. They are jammed and cannot be operated by hand, but the exposed key housing is small and complex, indicating it was designed for fine, precision manipulation.",
        use_func=data_array_door_lockpick_used),
    "bridge_security_terminal": UseTarget(
        id="bridge_security_terminal",
        name="Bridge Security Terminal",
        keywords = ["door", "bridge", "security", "terminal", "console"],
        debug_info="Bridge security terminal before door. Use cypher here and power it up from cargo room.",
        on_look="It is a thin, reinforced diagnostic panel built into the wall beside the Bridge's main hatch. The screen is active but glows with a frustrated amber caution light. A scrolling list of diagnostic errors is displayed, blocking access: \n\nERROR 01: POWER BUS DISRUPTION\nERROR 02: SECURITY CLEARANCE REQUIRED \n\nYou realize this terminal doesn't open the door, but diagnoses why the door won't open. Beneath the display, a secure interface socket is visible, designed to accept a high-level cryptographic cypher for verification.",
        use_func=bridge_door_console_cypher_used),
    "hydraulic_pipe": UseTarget(
        id="hydraulic_pipe",
        name="Hydraulic Pipe",
        keywords = ["door", "pipe", "pipes", "vent", "line", "hydraulic"],
        debug_info="Act 5 hydraulic pipe next to reactor room.",
        on_look="The thick hydraulic fluid line running along the doorframe is severely buckled and pinched, completely cutting off fluid pressure to the reactor room. You're going to need some kind of leverage to manually fix this.",
        use_func=emergency_launch_compartment_hydraulic_pipe_used),
}

galley_blast_door = initial_use_targets["galley_blast_door"]
env_controls_access_panel = initial_use_targets["env_controls_access_panel"]
central_freight_bay_bulk_door = initial_use_targets["central_freight_bay_bulk_door"]
service_control_junction_5f_door = initial_use_targets["service_control_junction_5f_door"]
logistics_door_console = initial_use_targets["logistics_door_console"]
power_bus_distribution_panel = initial_use_targets["power_bus_distribution_panel"]
eva_lockers_sars_locker = initial_use_targets["eva_lockers_sars_locker"]
personal_command_vault_before_weld = initial_use_targets["personal_command_vault_before_weld"]
personal_command_vault_after_weld = initial_use_targets["personal_command_vault_after_weld"]
data_array_door = initial_use_targets["data_array_door"]
bridge_security_terminal = initial_use_targets["bridge_security_terminal"]
hydraulic_pipe = initial_use_targets["hydraulic_pipe"]

def setup_use_targets():
    galley.use_targets["galley_blast_door"] = galley_blast_door
    deck_4_med_env_corridor.use_targets["env_controls_access_panel"] = env_controls_access_panel
    upper_aft_lobby.use_targets["central_freight_bay_bulk_door"] = central_freight_bay_bulk_door
    service_control_junction_5f.use_targets["service_control_junction_5f_door"] = service_control_junction_5f_door
    operations_and_cargo_interlink.use_targets["logistics_door_console"] = logistics_door_console
    cargo_bay_control_f.use_targets["power_bus_distribution_panel"] = power_bus_distribution_panel
    eva_gear_lockers.use_targets["eva_lockers_sars_locker"] = eva_lockers_sars_locker
    deck_5_forward_muster_station.use_targets["bridge_security_terminal"] = bridge_security_terminal
    systems_data_access_corridor.use_targets["data_array_door"] = data_array_door
    captains_quarters.use_targets["personal_command_vault_before_weld"] = personal_command_vault_before_weld
    emergency_launch_compartment.use_targets["hydraulic_pipe"] = hydraulic_pipe
    

def setup_use_targets_usable_items():
    galley_blast_door.usable_items["maintenance_jack"] = maintenance_jack
    env_controls_access_panel.usable_items["engys_keycard"] = engys_keycard
    central_freight_bay_bulk_door.usable_items["welder"] = welder
    service_control_junction_5f_door.usable_items["welder"] = welder
    logistics_door_console.usable_items["sart"] = sart
    power_bus_distribution_panel.usable_items["maintenance_jack"] = maintenance_jack
    eva_lockers_sars_locker.usable_items["radio"] = radio
    bridge_security_terminal.usable_items["bridge_access_cypher"] = bridge_access_cypher
    personal_command_vault_before_weld.usable_items["welder"] = welder
    personal_command_vault_after_weld.usable_items["screwdriver"] = screwdriver
    data_array_door.usable_items["lockpick"] = lockpick
    hydraulic_pipe.usable_items["maintenance_jack"] = maintenance_jack

# Sceneries

sceneries = {
    "s_cryo_bay_pillar": Scenery(
        id = "s_cryo_bay_pillar",
        name = "Pillar",
        keywords = ["pillar", "central"],
        debug_info = "Scenery for cryo bay",
        on_look = "The central pillar is a wide, reinforced core housing major utility conduits. Its surface is clad in smooth, white, matte plating that feels cold and damp to the touch. You can detect a very faint, low-frequency hum emanating from its interior."
        ),
    "s_cryo_bay_hypersleep_unit": Scenery(
        id = "s_cryo_bay_hypersleep_unit",
        name = "Hypersleep Unit",
        keywords = ["cryo", "bay", "cryobay", "cryochamber", "cryochambers", "sleep", "cryogenic", "hyper"],
        debug_info = "Scenery for cryo bay",
        on_look = f"You look at your Hypersleep Unit, a single metallic pod still humming with residual energy. The thick glass lid is raised and frosted with condensation, a sign of the rapid thaw-cycle. Its interior is lined with nutrient tubing and monitoring sensors. You notice a slight scorch mark near the main power conduit. A possible cause for the system failure that woke you."
        ),
    "personal_command_vault_complete": Scenery(
        id="personal_command_vault_complete",
        name="Personal Command Vault",
        keywords = ["vault", "personal", "personal vault", "safe", "command"],
        debug_info="Act 4 captains safe.",
        on_look="The Personal Command Vault now stands open. The electronic lock is bypassed, and the small inner compartment is empty."
        )
}

s_cryo_bay_pillar = sceneries["s_cryo_bay_pillar"]
s_cryo_bay_hypersleep_unit = sceneries["s_cryo_bay_hypersleep_unit"]
personal_command_vault_complete = sceneries["personal_command_vault_complete"]

def setup_sceneries():
    cryo_bay.sceneries["s_cryo_bay_pillar"] = s_cryo_bay_pillar
    cryo_bay.sceneries["s_cryo_bay_hypersleep_unit"] = s_cryo_bay_hypersleep_unit

# NPCS
def setup_npcs():
    medical_labs.npcs["engy"] = engy
    
    deck_5_secure_pathway.npcs["chef"] = chef
    service_access_hatchway.npcs["chef"] = chef
    msc_1.npcs["chef"] = chef
    vertical_service_shaft.npcs["chef"] = chef
    reactor_deck_service_hub.npcs["chef"] = chef
    auxiliary_reactor_control.npcs["chef"] = chef

    captains_quarters.npcs["captain"] = captain

    msc_2_b_console_desk.npcs["arachnid"] = arachnid
    msc_2_b_storage_drums.npcs["arachnid"] = arachnid
    msc_2_b_power_conduit.npcs["arachnid"] = arachnid

## Run all necessary setups

def run_all_setups():
    setup_rooms()
    setup_interactables()
    setup_items()
    setup_use_targets()
    setup_use_targets_usable_items()
    setup_sceneries()
    setup_npcs()

run_all_setups()


# Debug stuff

def add_debug_inventory():
    player.inventory["backpack"] = backpack
    player.inventory["radio"] = radio
    player.inventory["flashlight"] = flashlight
    player.inventory["maintenance_jack"] = maintenance_jack
    player.inventory["welder"] = welder
    # player.inventory["screwdriver"] = screwdriver
    # player.inventory["lockpick"] = lockpick
    # player.inventory["sart"] = sart
    # player.inventory["bridge_access_cypher"] = bridge_access_cypher

add_debug_inventory()