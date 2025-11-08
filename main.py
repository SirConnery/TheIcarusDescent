from rooms_config import initial_rooms
rooms = initial_rooms

game_is_running = True
cur_room = rooms["CryoBay"]

print(cur_room.forward)

def parser():
    pass

def move(direction):
    pass

## Functions

def check_quit(cmd):
    if cmd in ["quit", "exit"]:
        print("Game has been quit. Your fate remains a mystery...")

## Main logic

# while True:
#      command = input("\n> ").lower().strip()
#      current_room.describe()

#      if check_quit(command):
#         break

# Example of retrieving the room object:
# print(room_list["CryoBay"].name)

def p_get_available_exits():
    pass