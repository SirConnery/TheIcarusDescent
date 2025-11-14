import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import pyfiglet

console = Console()

from game_data import rooms, player
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

def r_text(text, delay=0.00, style="cyan"):
    if text:
        for char in text:
            if style:
                console.print(char, style=style, end="")
            else:
                console.print(char, end="")
            time.sleep(delay)
    else:
        r_text("Returned 'None'", style="red")

# Acts title text

def r_text_act_change(act_number="", subtitle="", style="bold white", font="xsbookb",
                      subtitle_font="cyberlarge", subtitle_style="bold cyan",
                      delay=0.0, line_delay=0.0):
    ascii_text = pyfiglet.figlet_format(f"ACT {act_number}", font=font)
    
    panel = Panel(
        Align.center(f"[{style}]{ascii_text}[/{style}]", vertical="middle"),
        expand=False,
        border_style=style
    )
    console.print(Align.center(panel, vertical="middle"))
    
    if subtitle:
        subtitle_text = pyfiglet.figlet_format(subtitle, font=subtitle_font)
        for line in subtitle_text.splitlines():
            console.print(Align.center(f"[{subtitle_style}]{line}[/{subtitle_style}]"))
            time.sleep(line_delay)
    
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
        obj = filtered[1]
        obj_2 = filtered[2]

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


## Get directions and print

def get_directions():
    cur_room = player.cur_room

    if cur_room.forward:
        player.output_directions += f"\n[FORWARD] {cur_room.forward.name}"
    if cur_room.backward:
        player.output_directions += f"\n[BACKWARD] {cur_room.backward.name}"
    if cur_room.left:
        player.output_directions += f"\n[LEFT] {cur_room.left.name}"
    if cur_room.right:
        player.output_directions += f"\n[RIGHT] {cur_room.right.name}"

## Game intro

def game_start():
    player.cur_room = rooms["operations_distribution_crossover"]
    player.enter_room(rooms["operations_distribution_crossover"])
    get_directions()

    clear_screen()
    draw_HUD()
    
    r_text_act_change(player.output_act_number, player.output_act_subtitle)
    r_text(player.output)
    r_text(player.output_directions)

    player.output=""
    player.output_act_number=""
    player.output_act_subtitle=""
    player.output_directions = f"\n\n"

game_start()

# Main loop

while game.running:
    command = console.input("[white]\n> [/white]").lower().strip()
    process_input(command)
    get_directions()

    # clear_screen()
    draw_HUD()

    if player.output_act_number and player.output_act_subtitle:
         r_text_act_change(player.output_act_number, player.output_act_subtitle)

    outputs = [
    (player.output_debug, {"style": "yellow"}),
    (player.output_gain_item, {"style": "green"}),
    (player.output_lose_item, {"style": "red"}),
    (player.output_error, {"style": "red"}),
    (player.output_help, {"style": "white"}),
    (player.output, {}),
    (player.output_slow, {"delay": 0.05}),
    (player.output_fast, {"delay": 0.02}),
    (player.output_directions, {"delay": 0.00}),]

    for text, kwargs in outputs:
        if text:
            r_text(text, **kwargs)

    player.output = f""
    player.output_fast = f""
    player.ouput_slow = f""
    player.output_debug = f""
    player.output_error = f""
    player.output_help = f""
    player.output_act_number = f""
    player.output_act_subtitle = f""
    player.output_directions = f"\n\n"
    player.output_gain_item = f""
    player.output_lose_item = f""

    if command == "quit":
        quit_game()
