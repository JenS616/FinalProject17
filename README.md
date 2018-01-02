# FinalProject17
The player arrives on Mars from a spaceship crash and is separated from the crew, who are waiting for rescuers in an escape pod in an unknown area of the planet. The object of the game is for the player to survive alone with only the supplies from the crashed spaceship until the crew can be contacted. An additional challenge for the player is to prevent the health status from reaching zero.

Storyline:
Starts with player arriving on Mars with backstory on how they were separated from crew
Lists what items the player has (broken spaceship, broken satellite, spacesuit, etc.) and objective (to survive using those materials while trying to call the crew for help), also lists what the player can do
Allows player to inspect the broken spaceship or survey surroundings
Broken spaceship has 3 day supply of food and water along with tools (screwdriver, wrench, hammer and nails, etc.) to fix the tools
Player can add tools to their inventory (ex. can pick up one of the tools or food)
Can only hold 3 things at a time
If holding food, can eat it to regain health (other than that, not necessary)
If holding a tool, can use it to fix a part of the spaceship or the satellite
A dust storm comes; player loses health and has to fix the broken part of the spaceship with a hammer and nails
Player can explore ourside of the spaceship
When exploring outside, finds parts to the missing satellite
Player can inspect satellite and see which parts are missing or needed to be fixed (list each problem as a class for the satellite?)
List of things player can do: inspect (place, object), fix (need a tool in the inventory and need to be near the object), send messgae (once the satellite is fixed), pickup object (to place in inventory), drop object (to put back in original spot - spots can be lists?), walk (inside spaceship, corner of spaceship (with broken part), outside of spaceship - east, west, north, south)
first problem is part of the suit is ripped - need to find a sewing kit, loses health
when the crew is called, the game finishes, outro is that the crew arrives in their escape pod to pick the player up and they wait in the pod for 2 weeks until some advanced space shuttle picks them up and takes them back to Earth

Things/Objects that need classes:
  satellite (in self init there are variables for each part of the satellite that needs fixing)
  person
  the different objects?? - can have different functions??

Things/objects that are lists/dictionaries:
  areas? - can be a list or dictionary of all the things in the room/area

Things/objects that are in the person's class:
  (self.)health (a variable from 0 to 100), defined in init function
  (self.)inventory (list inside the person's class, if there are more than 3 things in the list, the person has to drop something - definied in init function
  walking (function)
  eating (function) - increases health, deletes the food variable from the program (because it's eaten)
  fix (function) - should there be separate fix functions for each problem??
  pickup object - asks player what to pickup, adds it to the inventory, needs a statement saying that if there are already 3 things in the inventory, don't complete the pickup function
  drop object - doesn't have to drop the object in the same place it is found, just add it to the list of stuff for that specific place the player is in when it's dropped
  send message - calls for the outro statement, lists health, boom final project is finished
  inspect object - lists details about the object, what it can be used for - if each object is a class, it could say print(item/place.info)
  
Additional notes:
  can use the split() command to split the user input into different words, then say self.(action, object), unless the command isn't in the list of stuff the player can do
  use a while loop?? - can keep asking for user input and then do a function based on the input, when the game is finished it can break
