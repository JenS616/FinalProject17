################################ ROOMS #########################################
class Room(object):

    def __init__(self, name):
        self.name = name

    def dire(self, north, south, east, west): #directions (what's north/south/etc. of the room)
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def items(self):
        self.items = []

    def desc1(self, desc1): #First description of the room, when the player first enters
        self.desc1 = desc1

    def desc2(self, desc2): #Description of the room after the player has already entered it and read the first description
        self.desc2 = desc2  #Remember to add something if the player hasn't picked up all the items yet

    def desc3(self):
        if len(self.items) == 0:
            print(" There are no items in this area.")
        else:
            print(f"You see the {self.items} there.")

#The official name of the room that corresponds to its variable
home = Room('home')
smq = Room("spaceship's main quarters")
spw = Room('spaceship outer wall')
slq = Room('living quarters')
north = Room('north')
northeast = Room('northeast')
east = Room('east')
southeast = Room('southeast')
south = Room('south')
southwest = Room('southwest')
west = Room('west')
northwest = Room('northwest')
#None is if the player can't walk any further
none = Room('none')

#Defines the directions
home.dire(smq, south, east, west)
smq.dire(spw, home, none, slq)
spw.dire(none, smq, none, slq)
slq.dire(none, none, smq, none)
north.dire(none, home, northeast, northwest)
northwest.dire(none, west, north, none)
west.dire(northwest, southwest, home, none)
southwest.dire(west, none, south, none)
south.dire(home, none, southeast, southwest)
southeast.dire(east, none, none, south)
east.dire(northeast, southeast, none, home)
northeast.dire(none, east, none, north)

#Description 1 (description of the room when the player first enters)
home.desc1("This is your starting point. Choose to walk south, east, west, or venture inside the spaceship by typing 'north' (You can get to the northern territory from the northeast or northwest regions). Each path reveals new secrets that can help you on your mission to contact the crew.")
smq.desc1("You enter the spaceship’s main quarters. Resting against the right wall beside the broken satellite is a toolbox with a screwdriver, wrench, and a hammer. Maybe one of these tools could help in your further adventures.")
spw.desc1("An unusual shimmer of light is coming through the side of the wall. A piece of the metal wall has been ripped off, exposing the setting sun. Being how the broken spaceship is your home for the next few days, it would be important to fix the hole… ")
slq.desc1("Here is the room you have gotten to know very well over the last couple of months, the living quarters of the spaceship. Recent memories of spending days with the crew float through your head as your eyes aimlessly wander the room. Next to your bed lies some thread for sewing, and on the opposite side of the room is a package of space food you’ve grown so accustomed to.")
north.desc1("Although this planet is far away from Earth, and even farther from the Sun, a glimpse of the beautiful sunset in the distance convinces you to walk north. There, peeking out from underneath the dust, is a shimmer of metal reflecting the Sun’s fading light. It appears to be a piece of the spaceship’s outer wall that has appeared to have broken off during the crash.")
northwest.desc1("A silver motor appears to stand out from the ever present red backdrop here in the northwest region. You wonder how it could have landed so far away from the spaceship and the satellite from which it broke off of.")
west.desc1("Similar to the midwestern United States, the western area of your travels does not have much excitement going on. The only thing here is the broken satellite - remember to come to this spot to attach broken parts.")
southwest.desc1("The southwest is very different from the south. The weather is calm and mountains can only faintly be seen in the distance. There is a keyboard that appears to have broken off of the satellite, which perhaps would help in typing a message...")
south.desc1("Even in the dust storm, the south has magnificent scenery unlike any place you’ve ever seen; there are mountains in the distance that are hundreds of times larger than any skyscraper on Earth. However, you bring your focus back to the transmitter that you recently laid your eyes on.")
southeast.desc1("Through the clouds of red dust in this southeast region, you make out silver batteries that, other than a coating of dust, look perfectly good to use.")
east.desc1("The land to the east does not seem to have much activity going on, although you come close to stepping on an antenna lying just below your feet.")
northeast.desc1("The northeast border of your travels have an outstanding view of the nearest volcano, but what interests you more is a flat square material lying flat in the dirt. Closer inspection reveals the material to be a solar panel from the satellite.")

#If the player can't walk anymore (ex. can't walk south of southwest)
none.desc1("You cannot walk anymore in this direction. Please walk in a different direction.")

#Description 2 (description atfer the player has already entered the room once & read that description)
home.desc2(home.desc1)
smq.desc2("You are back in the spaceship’s main quarters.")
spw.desc2("The hole in the spaceship’s wall is still there. It should really be fixed soon…")
slq.desc2("You arrive back at the spaceship’s living quarters.")
north.desc2("You are back in the north, the Sun almost below the horizon now.")
northeast.desc2("You come to the northeast again. It has a great view of the volcano, and you hope it doesn’t erupt while you’re still trapped on the planet.")
west.desc2("You are back in the west. The only thing here is the broken satellite - remember to come to this spot to attach broken parts.")
southwest.desc2("You return to the southwest, the calmest region of Mars. You could spend the day here relaxing- if you didn’t have a mission at hand.")
south.desc2("The view of the mountains in the south never cease to amaze you, not matter how many times you return.")
southeast.desc2("The southeast is the same dusty place that you visited before.")
east.desc2("You are in the eastern region again, although there is not much to look at here.")
northwest.desc2("You come back to the northwest region to enjoy the view.")

#The items that are present during the start of the game in each room
home.items = []
smq.items = ['wrench', 'hammer', 'screwdriver']
spw.items = []
slq.items = ['thread', 'food']
north.items = ['piece']
northeast.items = ['panel']
east.items = ['antenna']
southeast.items = ['batteries']
south.items = ['transmitter']
southwest.items = ['keyboard']
west.items = []
northwest.items = ['motor']

############################# PLAYER ############################################

class Player(object):

    def __init__(self):
        self.health = 100
        self.inventory = []
        self.room = home

    def eat(self, food):
        if food in self.inventory:
            self.health += 50
            if self.health > 100:
                self.health = 100
            print(f"Your health increased to {self.health}.")
        else:
            print(f"You do not have {food.lower()} in your inventory.")

    def pickup(self, item):
        if item == 'satellite':
            self.inventory.append(item)
            self.room.items.remove(item)
            self.ripsuit()
        elif item in self.room.items:
            if len(self.inventory) == 8:
                print("You are already holding eight items. Drop one to pick up another item.")
            else:
                self.inventory.append(item)
                self.room.items.remove(item)
                print(f"You pickup the {item}.")
        else:
            print(f"The {item} is not in this area.")
        return self.inventory
        return self.room.items

    def drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.room.items.append(item)
            print(f"You have dropped the {item} in the {self.room.name} area.")
        else:
            print(f"{item.title()} is not in your inventory.")
        return self.inventory
        return self.room.items

    def not_in_int(self, inpt): #Used for functions involving objects, says what to do if object isn't in the inventory
        if inpt(1) not in self.inventory:
            print(f"The {inpt(1).lower()} is not in the inventory. Action cannot be completed.")

    def walk(self, direction): #WORKS!!!!!
        directions = {'north': self.room.north, 'south' : self.room.south, 'east' : self.room.east, 'west' : self.room.west}
        self.room = directions[direction]
        if self.room == smq and 'satellite' in self.inventory:
            self.callcrew
        else:
            if self.room != none:
                if self.room not in prevroom:
                    prevroom[self.room] = 0 #adds the room to the dictionary
                prevroom[self.room] +=1 #Previous room that the player has been in is added to the dictionary with a count
                prevroomlist.append(self.room)
                if prevroom[self.room] > 1: #Prints desc1 or desc2 (depends on # of times the person was in the room)
                    print(self.room.desc2), self.room.desc3() #Prints desc2 and list of items
                else:
                    print(self.room.desc1)
            else:
                print(self.room.desc1)
                self.room = prevroomlist[-1] #last visited room
                prevroom[self.room] += 1
                return prevroom

    def myinventory(self):
        print("You have: ")
        for item in self.inventory:
            print(item)
        print("in your inventory.")

    def mend(self, item): #mends the suit with the thread
        if 'suit' in item:
            answer = input("With what? ")
            if 'thread' in answer:
                if 'thread' in self.inventory:
                    print("You are able to fix the problem and sew up the rip in your suit with the thread. You are now able to focus on the task that's still at hand: fixing the satellite, which is in your inventory. Just go to the spaceship's main quarters!")
                    self.inventory.remove('thread')
                    mendedsuit = 1
                    return mendedsuit
                else:
                    print("Good idea, but you do not have the thread in your inventory. You should probably go get it...")
            else:
                print("Try thinking along the lines of sewing material...")
        else:
            print(f"You cannot mend the {item}. However, you can mend clothing, perhaps a suit of some sort.")

    def attach(self, item): #attaches parts to the satellite
        if self.room != west:
            if item != 'piece':
                print(f"You cannot attach the {item} to the shuttle when you are in the {self.room.name}. The satellite is in the western region.")
            else:
                if self.room == spw:
                    answer = input('With which tool? ')
                    if 'hammer' in answer:
                        print('You are able to fix the side of the ship and reattach the broken piece.')
                        self.inventory.remove('piece')
                        piecefixed = 'y'
                        return piecefixed
                    else:
                        print(f"The {answer} is the wrong tool.")
                else:
                    print("You need to be at the spaceship wall to attach the broken piece to the wall.")
        else:
            if item not in attachtosat.keys() or item == 'piece':
                print(f"You can't attach {item} to the satellite.")
            else:
                answer = input('With which tool? ')
                if answer == attachtosat[item]:
                    print(f'You are able to successfully attach the {item} to the satellite with the {answer} (remember: the {answer} can be used more than once). You are one step closer in messaging your crew.')
                    self.inventory.remove(item)
                    onthesat.append(item)
                    print(f"You have attached {len(onthesat)}/6 broken parts to the satellite.")
                    if len(onthesat) == 6:
                        self.fixsat()
                else:
                    print(f'That is the wrong tool to attach the {item}. Try using a different one.')

    def fixsat(self):
        west.items.append('satellite')
        print("You have successfully repaired the satellite! To send the message, pickup the satellite and move it the the spaceship's main quarters")
        objects.append('satellite')
        return objects #Now if the player types in the command pickup satellite, it will bring the player to the ripsuit function

    def callcrew(self):
        answer = input("You have brought the satellite to the spaceship's main quarters. Would you like to call the crew? Y/N").lower()
        if answer == 'y':
            if piecefixed == 'y': #Ends the game - player brought satellite to the smq and the broken piece of the ship is fixed
                print("Luckily, you already fixed the broken piece in the spaceship's wall, so you are able to make the call to your crew and alert them of your situation with no problems. Two days pass, and on the third day, you see an escape pod coming towards you in the distance. You are saved! - for now... \n \n *****THE END*****")
            if piecefixed == 'n':
                self.health -= 20
                print(f"Sadly, when you try to contact the crew, a gust of wind from the open spaceship wall flew into the room and toppled over the satellite, which landed on you. You lost 50% health; your health is now {self.health}%. Try again after you attach the broken piece to the wall.")
        elif answer == 'n':
            pass
        else:
            print("Type in an answer that makes sense next time, please.")

    def ripsuit(self): #The first time the player rips the suit
        self.health -= 10
        print(f"Oh no! When you picked up the satellite, something from the satellite sagged your spacesuit and ripped it. You are losing pressure quick; your health is now {self.health}%. You better solve this problem quickly, or else your health will continue to drop.")
        mendedsuit = 0
        return mendedsuit

    def travelwithrip(self, mendedsuit): #Each time the player goes to a different room with a ripped suit, they lose 10% health
        if mendedsuit == 1:
            pass
        if mendedsuit == 0:
            self.health -= 10
            print(f"You continue to lose pressure in your spacesuit; your health is {self.health}%.")

commands = ['eat', 'pickup', 'drop','mend', 'attach', 'inventory', 'walk']

player = Player() #lets the player use everything in the Player class

#Used in the runcommand function, says what function to run based on user input
actions = {'eat' : player.eat, 'pickup' : player.pickup, 'drop' : player.drop, 'walk' : player.walk, 'inventory' : player.myinventory, 'mend' : player.mend, 'attach' : player.attach}

############################ LISTS, VARIABLES, AND DICTIONARIES #############################

#Is the broken piece fixed? n if no, changes to y if yes
piecefixed = 'n'

#Prints the statement when the player types in 'needhelp'
needhelp = "Your list of commands include: eat, pickup, drop, mend, attach, inventory, and walk, followed by an item you wish to use. \n(When using the walk command, type in north/south/east/west. The inventory command displays your inventory and does not need to be followed by an item) \nType in ‘needhelp’ to access this information again."

#List of objects that the player can pickup or modify (doesn't include the satellite)
objects = ['wrench', 'hammer', 'screwdriver', 'antenna', 'piece', 'panel', 'batteries', 'transmitter', 'keyboard', 'food', 'motor', 'thread', 'north', 'south', 'east', 'west', 'suit']

#The key is what attaches the object (ex. the screwdriver attaches the batteries)
attachtosat = {'antenna' : 'wrench', 'piece' : 'hammer', 'panel' : 'hammer', 'batteries' : 'screwdriver', 'transmitter' :'screwdriver', 'keyboard' : 'screwdriver', 'motor' : 'screwdriver'}

#The things that need to be added to the satellite are added to the list below once they are attached by the player
onthesat = []

#List of areas, used for the hint function
areas = [home, smq, spw, slq, north, northeast, northwest, east, west, south, southeast, southwest]

#If the suit is ripped, mendsuit = 0
mendedsuit = 1

#Dictionary of previous rooms visited and how many times (used in player.walk)
prevroom = {}
#List of previous rooms visited (used in player.walk) (list is used because order matters when figuring out the previous room)
prevroomlist = []

##############################STANDALONE FUNCTIONS ##############################

def beginning():
    print("You have been selected to participate in the Journey to Mars, a program formed by NASA to send humans to and from Mars to explore the red planet. As a member of the journeying crew, you and five other astronauts took a six month long trip through space, but it did not go as planned. During the landing sequence, the spacecraft broke down and the crew was forced to evacuate in an escape pod, leaving you (who they assumed dead) behind with a broken ship, a broken satellite, and a day’s worth of food. Your only hope of surviving is to contact the crew to alert them of your survival so they can rescue you. Can you fix the satellite to alert your crew in time?\n")
    print(needhelp)
    print("\nOne last warning: remember to keep your health above 0%. With that, you are ready to begin your journey.\n")
    print(home.desc1, '\n')

def runcommand():
    command = input().split()
    if len(command) == 0:
            print("The directions were not understood. Please type 'needhelp' to see a list of commands.")
    elif command[0] == 'inventory':
        player.myinventory()
        pass
    elif command[0] == 'needhelp':
        print(needhelp)
        pass
    elif command[0] == 'hint':
        hint()
        pass
    else:
        for word in command:
            if word not in actions.keys() and word not in objects:
                command.remove(word)
        if len(command) < 2:
            print("The directions were not understood. Please type 'needhelp' to see a list of commands.")
        if command[0] in actions.keys() and command[1] in objects:
            actions[command[0]](command[1])
        else:
            print("The directions were not understood. Please type 'needhelp' to see a list of commands.")
            return command

def hint(): #Gives different hints based on what stage of the game the player is in
    if mendedsuit == 0:
        print("You can use the thread, located in the spaceship's living quarters, to mend the spacesuit. Just walk to the spaceship main quarters and travel west. Pickup the thread and type in 'mend suit'.")
    elif player.health < 100:
        print("If you eat the food located in the spaceship's living quarters, you can gain back your health. The spaceship's living quarters are located west of the spaceship's main room.")
    elif len(onthesat) < 6:
        print("Use the tools located in the spaceships main quarters to attach the satellite parts to the satellite (which is located in the western region). The satellite parts are scattered throughout the areas of Mars. You have yet to visit: ")
        for area in areas:
            if area not in prevroomlist:
                print(area.name)
        print("Most of these areas have satellite parts that you can pick up.")
    else:
        print("There are no hints at this time.")

#############################RUNNING EVERYTHING!!!!##################################

beginning()
while True:
    if player.health == 0:
        print("You health reached 0%. As they say on Mars, you just kicked the bucket. Better luck next time.")
        break
    player.travelwithrip(mendedsuit) #Checks to see if health should be subtracted if there's a rip in the suit
    runcommand()
    print('\n') #Just to space things out more to make it easier to look at


