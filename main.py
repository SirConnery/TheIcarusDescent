import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import pyfiglet

from game_data import rooms, player, game

console = Console()

def draw_HUD():
    inventory_names = (", ".join(sorted([item.name for item in player.inventory.values()]))
    if player.inventory
    else "(empty)")

    hud_text= f"""[bright cyan]ICARUS SYSTEMS[/bright cyan]
    [grey82]Name:[/grey82][bright cyan]{player.name}[/bright cyan]
    [grey82]Status:[/grey82][{player.status_color}] {player.status}[/{player.status_color}], [grey82]Warmth:[/grey82] [{player.warmth_color}]{player.warmth}[/{player.warmth_color}], [grey82]Heartrate:[/grey82] [{player.heartrate_color}]{player.heartrate}[/{player.heartrate_color}], [grey82]Location:[/grey82] [yellow]{player.cur_room.name}[/yellow]
    [grey82]Inventory:[/grey82][light_steel_blue] {inventory_names}[/light_steel_blue]
    [grey82]Commands:[/grey82] Move, Survey, Interact, Look, Take, Use, Help, Quit"""

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

# Acts title text  (Chatgpt used to make this)

def r_text_act_change(
    act_number="",
    subtitle="",
    act_text="ACT",
    show_panel=True,
    style="bold white",
    font="xsbookb",
    subtitle_font="cyberlarge",
    subtitle_style="bold cyan",
    delay=0.0,
    line_delay=0.0,
    return_only=False,
):
    clear_screen()

    panel = None
    if show_panel and act_text:
        ascii_text = pyfiglet.figlet_format(f"{act_text} {act_number}", font=font)
        panel = Panel(
            Align.center(f"[{style}]{ascii_text}[/{style}]", vertical="middle"),
            expand=False,
            border_style=style
        )

    subtitle_render = None
    if subtitle:
        subtitle_text = pyfiglet.figlet_format(subtitle, font=subtitle_font)
        subtitle_render = [
            f"[{subtitle_style}]{line}[/{subtitle_style}]"
            for line in subtitle_text.splitlines()
        ]

    if return_only:
        return panel, subtitle_render

    if panel:
        console.print(Align.center(panel, vertical="middle"))

    if subtitle_render:
        for line in subtitle_render:
            console.print(Align.center(line))
            time.sleep(line_delay)

    if delay > 0:
        time.sleep(delay)

    time.sleep(2.0)
    clear_screen()
    draw_HUD()



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

def display_player_act_outputs():
    if player.output_act_number and player.output_act_subtitle:
        r_text_act_change(player.output_act_number, player.output_act_subtitle)

def display_player_outputs():
    # Does not display act text
    outputs = [
    (player.output_debug, {"style": "yellow"}),
    (player.output_gain_item, {"style": "green"}),
    (player.output_lose_item, {"style": "red"}),
    (player.output_error, {"style": "red"}),
    (player.output_help, {"style": "white"}),
    (player.output, {}),
    (player.output_fast, {"delay": 0.02}),
    (player.output_normal, {"delay": 0.04}),
    (player.output_slow, {"delay": 0.045}),
    (player.output_directions, {"delay": 0.00}),]

    for text, kwargs in outputs:
        if text:
            r_text(text, **kwargs)

def clear_player_outputs():
    player.output = f""
    player.output_fast = f""
    player.output_normal = f""
    player.output_slow = f""
    player.output_debug = f""
    player.output_error = f""
    player.output_help = f""
    player.output_act_number = f""
    player.output_act_subtitle = f""
    player.output_directions = f"\n\n"
    player.output_gain_item = f""
    player.output_lose_item = f""

## Game intro

def game_start():
    player.enter_room(rooms["cryo_bay"])
    get_directions()
    
    r_text_act_change(show_panel=False, subtitle="Icarus Descent", subtitle_font="big")
    
    clear_screen()
    draw_HUD()

    display_player_act_outputs()
    display_player_outputs()
    clear_player_outputs()


# Main loop
game_start()
while game.running:

    command = console.input("[white]\n> [/white]").lower().strip()
    if command == "quit":
        clear_screen()
        r_text("Game has been quit. Your fate remains a mystery...")
        break
    
    process_input(command)
    get_directions()

    clear_screen()
    draw_HUD()

    display_player_act_outputs()
    display_player_outputs()
    clear_player_outputs()