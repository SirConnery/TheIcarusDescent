from game_classes import NPC, Arachnid

npcs ={
    "engy":NPC(
    id="engy",
    name="Engy",
    debug_info="Deceased High Engineer Enrique.",
    on_look="The body is that of High Engineer Enrique, also known as Engy. He is a thin man in a white utility suit, slumped against the locker. Though you and Engy didn't know each other well, you vaguely recall his reputation for being a easygoing and quick with a joke who occasionally got into trouble with the Captain.",
    keywords=["body", "engy", "deceased", "dead"]),
    "chef":NPC(
    id="chef",
    name="Chef",
    debug_info="Main chef, black. Nat's great friend.",
    keywords=["chef"],
    on_look="You see the Chef. He's a broad, imposing black man in a dark-gray, reinforced utility jumpsuit. The sleeves are rolled up to his biceps, showing a powerful build, and a thick leather belt is cinched tight, carrying no excess gear. A faint feeling of relief washes over you at the sight of your friend, prepared and ready."),
    "tanaka":NPC(
    id="tanaka",
    name="Tanaka",
    debug_info="Japanese Data Systems Analyst")}

arachnids = {
    "arachnid":Arachnid(
    id="arachnid",
    name="Arachnid Creature",
    debug_info="The alien arachnid.",
    keywords=["arachnid","creature", "arachnid creature", "alien", "spider"],
    on_look="You stare at the creature, a horrific vision of overwhelming scale. Its body is roughly three meters long, and its spike-like legs each stretching two meters, give it a terrifying, elevated presence. It is covered in a glistening, chitinous exoskeleton. \n\nThough massive, the legs are composed of dozens of tight, compact segments, allowing for unnerving angles of movement. This jointed structure suggests the creature could compress its bulk or contort itself into surprisingly small accessways, despite its immense size. \n\nIt moves with a deep, rhythmic clicking sound that consumes all surrounding noise.",)
}

engy = npcs["engy"]
chef = npcs["chef"]
tanaka = npcs["tanaka"]

arachnid = arachnids["arachnid"]