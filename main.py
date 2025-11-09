import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet

console = Console()

from game_data import initial_rooms, game

def draw_HUD():
    hud_text= f"""[bright cyan]ICARUS SYSTEMS[/bright cyan]
    [green]Status: Healthy[/green], [blue]Warmth: Cold[/blue], [magenta]Heartrate: Calm[/magenta], [yellow]Location: {game.cur_room.name}[/yellow]
    [white]Inventory: (empty)[/white]
    [white]Commands:[/white] Move, Survey, Interact, Look, Take, Use, Help"""

    hud_panel = Panel(hud_text, title="STATUS", style="bright_cyan", border_style="cyan")
    console.print(hud_panel)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Rich text conversion

def r_text(text, style="cyan", delay=0.00):
    if text:
        for char in text:
            if style:
                console.print(char, style=style, end="")
            else:
                console.print(char, end="")
            time.sleep(delay)
    else:
        r_text("Returned 'None'", style="red")


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

    action = filtered[0] if filtered else ""
    obj = ""
    obj_2 = ""
    if len(filtered) == 2:
        obj = filtered[1]
        print(filtered)
        print(obj)
    if len(filtered) == 3:
        obj = filtered[2]
        obj_2 = filtered[3]

    match action:
            case "forward"|"backward"|"left"|"right"|"f"|"b"|"l"|"r"|"w"|"s"|"a"|"d":
                game.move(action)
            case "interact":
                game.interact(obj)
            case "survey":
                game.survey()
            case "look":
                game.look(obj)
            case "take":
                pass
            case "use":
                pass
            case "help":
                pass
            case "quit"|"exit"|"abort":
                pass
            case _:
                game.output_error = "Unrecognized command."
                return None

# Helpers


## Main logic

# while game_is_running:
#     command = console.input("[white]\n> [/white]").lower().strip()

#     clear_screen()
#     draw_HUD()

#     process_input(command)

#     if check_quit(command):
#         game_is_running = False


if game.cur_act == 1:
    game.cur_room = initial_rooms["CryoBay"]
    game.enter_room(initial_rooms["CryoBay"])
    clear_screen()
    draw_HUD()
    r_text(game.output)
    game.output=""


while game.running:
    command = console.input("[white]\n> [/white]").lower().strip()
    process_input(command)

    clear_screen()
    draw_HUD()

    if game.output:
        r_text(game.output)

    if game.output_debug:
        r_text(game.output_debug, style="yellow")

    if game.output_error:
        r_text(game.output_error, style="red")

    game.output = ""
    game.output_debug = ""
    game.output_error = ""

    if check_quit(command):
        game_is_running = False
