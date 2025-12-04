from js import document                 # type:ignore
from pyodide.ffi import create_proxy    # type:ignore
import asyncio
from main import game_intro, pyscript_gameplay_loop

# ----------------- Start Button -----------------
start_btn = document.getElementById("start-btn")

# Start game asynchronously
def start_game(event=None):
    asyncio.create_task(game_intro())

start_game_proxy = create_proxy(start_game)
start_btn.addEventListener("click", start_game_proxy)

# ----------------- Input Box / Submit Button -----------------
input_box = document.getElementById("user-input")
submit_btn = document.getElementById("submit-btn")

# Persistent proxy for submit button
submit_proxy = create_proxy(lambda event=None: pyscript_gameplay_loop())
submit_btn.addEventListener("click", submit_proxy)

# Persistent proxy for Enter key in input box
def enter_key_handler(event):
    if event.key == "Enter":
        pyscript_gameplay_loop()

enter_key_proxy = create_proxy(enter_key_handler)
input_box.addEventListener("keypress", enter_key_proxy)
