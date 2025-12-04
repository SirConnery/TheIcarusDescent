import sys
from js import document                 # type:ignore
from pyodide.ffi import create_proxy    # type:ignore
import asyncio
from main import game_intro, pyscript_gameplay_loop

# ----------------- Start Button -----------------
start_btn = document.getElementById("start-btn")

async def start_game(event=None):
    start_btn.style.display = "none"
    await game_intro()

start_game_proxy = create_proxy(start_game)
start_btn.addEventListener("click", start_game_proxy)

# ----------------- Input Box / Submit Button -----------------
input_box = document.getElementById("user-input")
submit_btn = document.getElementById("submit-btn")

# Async handler for submit button
async def handle_submit(event=None):
    await pyscript_gameplay_loop()

submit_proxy = create_proxy(handle_submit)
submit_btn.addEventListener("click", submit_proxy)

# Handler for Enter key in input box
def enter_key_handler(event):
    if event.key == "Enter":
        # Schedule the async function in the running event loop
        asyncio.create_task(pyscript_gameplay_loop())

enter_key_proxy = create_proxy(enter_key_handler)
input_box.addEventListener("keypress", enter_key_proxy)

sys.modules["pyscript_hooks"] = sys.modules[__name__]
