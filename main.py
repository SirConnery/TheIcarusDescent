from game_data import initial_rooms, initial_items, initial_interactables, sceneries

game_is_running = True
cur_room = initial_rooms["CryoBay"]


# Actions

def move(direction):
    new_room = cur_room.get_exits(direction)
    if new_room:
        enter_room(new_room)
    else:
        print("Unrocognized or invalid direction")

def interact(object):
    print("Interacted")
    if object in cur_room.interactables:
        print("object found")
        target = cur_room.interactables[object]
        target.on_interact


## Command Parser

def check_quit(input):
    if input in ["quit", "exit", "abort"]:
        print("Game has been quit. Your fate remains a mystery...")

def process_input(input):
    input = input.lower().strip().split()
    action = input[0]
    object = input[1]

    match action:
            case "forward"|"backward"|"left"|"right"|"f"|"b"|"l"|"r"|"w"|"s"|"a"|"d":
                move(input)
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

def enter_room(room_moved_to):
    global cur_room
    cur_room = room_moved_to
    room_enter_text = cur_room.get_entry_event()
    print(room_enter_text)

## Main logic

while game_is_running:
     command = input("\n> ").lower().strip()
     process_input(command)

     if check_quit(command):
        break

