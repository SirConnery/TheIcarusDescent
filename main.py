from game_data import initial_rooms

game_is_running = True
cur_room = initial_rooms["CryoBay"]


# Actions

def move(direction):
    new_room = cur_room.get_exits(direction)
    if new_room:
        enter_room(new_room)
        print(cur_room.name)
    else:
        print("Unrocognized or invalid direction")

def enter_room(room_moved_to):
    global cur_room
    cur_room = room_moved_to
    room_enter_text = cur_room.get_entry_event()
    print(room_enter_text)

def interact(keyword):
    print("Interacted")
    for obj in cur_room.interactables.values():
        if keyword in obj.keywords:
            obj.on_interact()
            return

    print(f"No interactable '{keyword}' in this room.")



## Command Parser

def check_quit(input):
    if input in ["quit", "exit", "abort"]:
        print("Game has been quit. Your fate remains a mystery...")

def process_input(user_input):
    input = user_input.lower().strip().split()    
    
    filler_words = {"at", "on", "to", "in", "the", "a", "an", "of", "with",
    "by", "for", "from", "about", "as", "into", "over", "under","around", "between", 
    "against", "during", "without", "through","within", "outside", "along"}
    
    filtered = []
    for word in input:
        if word not in filler_words:
            filtered.append(word)
    
    if not filtered:
        return None

    action = filtered[0]
    object = ""
    object_2 = ""
    if len(filtered) == 2:
        object = filtered[1]
    if len(filtered) == 3:
        object = filtered[2]

    match action:
            case "forward"|"backward"|"left"|"right"|"f"|"b"|"l"|"r"|"w"|"s"|"a"|"d":
                move(action)
            case "interact":
                interact(object)
            case "survey":
                pass
            case "look":
                pass
            case "take":
                pass
            case "use":
                pass
            case "help":
                pass
            case "quit"|"exit"|"abort":
                pass
            case _:
                print("Unrecognized command.")
                return None

# Helpers


## Main logic

while game_is_running:
     command = input("\n> ").lower().strip()
     process_input(command)

     if check_quit(command):
        break
