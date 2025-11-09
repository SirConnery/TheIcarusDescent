import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet

console = Console()

from game_data import initial_rooms

def draw_HUD():
    hud_text= f"""[bright cyan]ICARUS SYSTEMS[/bright cyan]
    [green]Status: Healthy[/green], [blue]Warmth: Cold[/blue], [magenta]Heartrate: Calm[/magenta], [yellow]Location: {cur_room.name}[/yellow]
    [white]Inventory: (empty)[/white]"""

    hud_panel = Panel(hud_text, title="STATUS", style="bright_cyan", border_style="cyan")
    console.print(hud_panel)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

## Game variables

game_is_running = True
cur_act = 1
last_action_output = ""

# Rich text conversion

def r_text(text, style="cyan", delay=0.00, ):
    if text:
        for char in text:
            if style:
                console.print(char, style=style, end="")
            else:
                console.print(char, end="")
            time.sleep(delay)
    else:
        r_text_error("Returned 'None'")

def r_text_error(text):
    r_text(text, style="red")

def r_text_debug(text):
    r_text(text, style="yellow")

# Actions

def move(direction):
    new_room = cur_room.get_exits(direction)
    if new_room:
        enter_room(new_room)
        r_text(cur_room.name)
    else:
        r_text_error("Unrocognized or invalid direction")

def enter_room(room_moved_to):
    global cur_room
    cur_room = room_moved_to
    room_enter_text = cur_room.get_entry_event()
    global last_action_output
    last_action_output = room_enter_text

def interact(keyword):
    r_text_debug("Interacted")
    for obj in cur_room.interactables.values():
        if keyword in obj.keywords:
            obj.on_interact()
            return

    r_text_error(f"No interactable {keyword} in this room.")

def survey():
    survey_text = cur_room.on_survey
    r_text(survey_text)

def look(keyword):
    r_text_debug("Looked")

    sources = [cur_room.interactables, cur_room.items, cur_room.sceneries]

    for source in sources:
        for obj in source.values():
            if keyword in obj.keywords:
                r_text(obj.on_look)
                return

    r_text_debug(f"No interesting {keyword} in this room.")

## Command Parser

def check_quit(input):
    if input in ["quit", "exit", "abort"]:
        r_text("Game has been quit. Your fate remains a mystery...")

def process_input(user_input):
    input = user_input.lower().strip().split()    
    
    filler_words = {"at", "on", "to", "in", "the", "an", "of", "with",
    "by", "for", "from", "about", "as", "into", "over", "under","around", "between", 
    "against", "during", "without", "through","within", "outside", "along"}
    
    filtered = []
    for word in input:
        if word not in filler_words:
            filtered.append(word)
    
    if not filtered:
        return None

    action = filtered[0]
    obj = ""
    obj_2 = ""
    if len(filtered) == 2:
        obj = filtered[1]
    if len(filtered) == 3:
        obj = filtered[2]
        obj_2 = filtered[3]

    match action:
            case "forward"|"backward"|"left"|"right"|"f"|"b"|"l"|"r"|"w"|"s"|"a"|"d":
                move(action)
            case "interact":
                interact(obj)
            case "survey":
                survey()
            case "look":
                look(obj)
            case "take":
                pass
            case "use":
                pass
            case "help":
                pass
            case "quit"|"exit"|"abort":
                pass
            case _:
                r_text_error("Unrecognized command.")
                return None

# Helpers

if cur_act == 1:
    cur_room = initial_rooms["CryoBay"]
    enter_room(initial_rooms["CryoBay"])

## Main logic

# while game_is_running:
#     command = console.input("[white]\n> [/white]").lower().strip()

#     clear_screen()
#     draw_HUD()

#     process_input(command)

#     if check_quit(command):
#         game_is_running = False

while game_is_running:
    command = console.input("[white]\n> [/white]").lower().strip()
    process_input(command)

    clear_screen()
    draw_HUD()

    r_text(last_action_output)

    if check_quit(command):
        game_is_running = False
