import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import pyfiglet

console = Console()

from game_data import initial_rooms, player
from game_classes import Game

game = Game()

def draw_HUD():
    inventory_names = (", ".join(sorted([item.name for item in player.inventory.values()]))
    if player.inventory
    else "(empty)")

    hud_text= f"""[bright cyan]ICARUS SYSTEMS[/bright cyan]
    [green]Status: {player.status}[/green], [blue]Warmth: {player.warmth}[/blue], [magenta]Heartrate: {player.heartrate}[/magenta], [yellow]Location: {player.cur_room.name}[/yellow]
    [white]Inventory: {inventory_names}[/white]
    [white]Commands:[/white] Move, Survey, Interact, Look, Take, Use, Help, Quit"""

    hud_panel = Panel(hud_text, title="STATUS", style="bright_cyan", border_style="cyan")
    console.print(hud_panel)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

## Rich text conversion

# All normal text

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

# Acts change title text

def r_text_act_change(act_number, style="bold white", font="slant", delay=0.8):
    ascii_text = pyfiglet.figlet_format(f"ACT {act_number}", font=font)
    styled_text = f"[{style}]{ascii_text}[/{style}]"
    panel = Panel(Align.center(styled_text, vertical="middle"), expand=False, border_style=style)

    console.print(panel)
    
    if delay > 0:
        time.sleep(delay)



# Other functions

def quit_game():
    game.running = False
    clear_screen()
    r_text("Game has been quit. Your fate remains a mystery...")

## Command Parser

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
                player.move(action)
            case "interact":
                player.interact(obj)
            case "survey":
                player.survey()
            case "look":
                player.look(obj)
            case "take":
                player.take(obj)
            case "use":
                player.use(obj,obj_2)
            case "help":
                player.help()
            case "quit":
                #handled in main loop
                pass
            case "debug_drop":
                player.drop(obj)
            case _:
                player.output_error = "Unrecognized command."
                return None


## Game intro

if game.cur_act == 1:
    player.output_act_title = "ACT 1"
    player.cur_room = initial_rooms["CryoBay"]
    player.enter_room(initial_rooms["CryoBay"])
    clear_screen()
    draw_HUD()
    r_text_act_change("1")
    r_text(player.output)
    player.output=""

# Main loop

while game.running:
    command = console.input("[white]\n> [/white]").lower().strip()
    process_input(command)

    clear_screen()
    draw_HUD()

    if player.output_debug:
        r_text(player.output_debug, style="yellow")

    if player.output_error:
        r_text(player.output_error, style="red")
    
    if player.output_help:
        r_text(player.output_help, style="white")

    if player.output_act_title:
        r_text_act_change(player.output_act_title)

    if player.output:
        r_text(player.output)

    player.output = ""
    player.output_debug = ""
    player.output_error = ""
    player.output_help = ""
    player.output_act_title = ""
    
    if command == "quit":
        quit_game()
