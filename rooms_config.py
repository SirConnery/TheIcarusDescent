from game_classes import Room 

initial_rooms = {
    "CryoBay": Room(
        name = "Cryo Bay",
        description = "It is a room with cryo stuff.",
        on_enter = "You have entered the Cryobay",
        forward = None,
        backward = None,
        left = None,
        right = None
    )

}