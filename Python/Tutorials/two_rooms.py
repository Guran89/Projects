DESC = "desc"
SOUTH = "south"
NORTH = "north"
EAST = "east"
WEST = "west"

SCREEN_WIDTH = 60

worldRooms = {
    "Living Room": {
        DESC: """A broken TV in the corner, a dirty mat, and a sofa that you really shouldn't sit in if you care about your clothes.
Great place. You can see three doors, one to the north, one to the east and one to the west.""",
        NORTH: "Kitchen",
        EAST: "Bathroom",
        WEST: "Bedroom"},
    "Kitchen": {
        DESC: "The kitchen is a mess. There are dirty dishes all over the place.\nIf you look to the south, "
              "you see the door to the living room.",
        SOUTH: "Living Room"},
    "Bathroom": {
        DESC: "The lamp is flickering, the toilet seat is broken and the mirror is covered in dust.",
        WEST: "Living Room"},
    "Bedroom": {
        DESC: "The bed is a mess, sheets lie all over the floor. You flick the light switch, but nothing happens.\nThe only way out is to the east, back to the kitchen",
        EAST: "Living Room"}
    }

location = "Living Room"
showFullExits = True

import cmd, textwrap, time

def gameStart():
    print("Welcome to this demo!")
    print("==========")
    print("Loading...")
    print("==========")
    time.sleep(2)
    print("""\nWelcome!\nAt this time you cannot do very much. You can walk round in the different rooms and... yeah... That's pretty much it.
I'm working on adding items to interact with. Until then - Hope you'll enjoy!""")
    print("\nPress <ENTER> to start game")
    input()
    time.sleep(1)
    print("You find yourself standing in what seems to be a living room, all by yourself.\nYou can't seem to remember how you got here, nor do you know where you are.")
    print("\nPress <ENTER> to continue.")
    input()
    time.sleep(1)
    
def displayLocation(loc):
    print("=" * len(loc) + "====")
    print("| " + loc + " |")
    print("=" * len(loc) + "====")
    time.sleep(1)
    print("\n".join(textwrap.wrap(worldRooms[loc][DESC], SCREEN_WIDTH)))
    
    #Print exits
    exits = []
    for direction in (NORTH, SOUTH, EAST, WEST):
        if direction in worldRooms[loc].keys():
            exits.append(direction.title())
    print()
    if showFullExits:
        for direction in (NORTH, SOUTH, EAST, WEST):
            if direction in worldRooms[location]:
                print("%s: %s" % (direction.title(), worldRooms[location][direction]))
    else:
        print("Exits: %s" % " ".join(exits))

def moveDirection(direction):
    global location

    if direction in worldRooms[location]:
        print("You move to %s." % direction)
        location = worldRooms[location][direction]
        displayLocation(location)
    else:
        print("You cannot go in that direction.")

class TextAdventureCmd(cmd.Cmd):
    prompt = "\n> "

    def default(self, arg):
        print("I do not understand that command. Type 'help' for a list of commands.")

    def do_quit(self, arg):
        return True

    def do_north(self, arg):
        moveDirection("north")

    def do_south(self, arg):
        moveDirection("south")

    def do_east(self, arg):
        moveDirection("east")

    def do_west(self, arg):
        moveDirection("west")

if __name__ == "__main__":
    gameStart()
    displayLocation(location)
    TextAdventureCmd().cmdloop()
    print("Thanks for playing.")
