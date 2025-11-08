from game_data import initial_rooms
rooms = initial_rooms

game_is_running = True
cur_room = rooms["CryoBay"]

def move(direction):
    new_room = cur_room.get_exits(direction)
    if new_room:
        enter_room(new_room)
    else:
        print("Unrocognized or invalid direction")

def enter_room(room_moved_to):
    global cur_room
    cur_room = room_moved_to
    room_enter_text = cur_room.get_entry_event()
    print(room_enter_text)


## Functions

def check_quit(input):
    if input in ["quit", "exit", "abort"]:
        print("Game has been quit. Your fate remains a mystery...")

def process_input(input):
    input = input.lower()
    match input:
            case "forward"|"backward"|"left"|"right"|"f"|"b"|"l"|"r"|"w"|"s"|"a"|"d":
                move(input)
            case "interact":
                pass
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

## Main logic

while game_is_running:
     command = input("\n> ").lower().strip()
     process_input(command)

     if check_quit(command):
        break