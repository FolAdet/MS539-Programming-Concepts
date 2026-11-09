import random
import sys
#starting adventurere stats
health = 100
oxygen = 100
power = 50
survivalPoints = 0
timeRemaining = 45
keycard = False
ammunition = False
electricalTool = False

#function that diplays current stat of the adventurer
def display_statistics(health, oxygen, power, survivalPoints, timeRemaining):
    print(f"Health: {health}")
    #give warning at low health stages
    if health < 25:
        print("WARNING: Low Health at 25%")
    elif health > 80:
        print("Health is optimal")
    print(f"Power: {power}")
    print(f"Survival Points: {survivalPoints}")
    print(f'Time Remaining: {timeRemaining}')

#Create an adventure game sim
#first lets display the title of the sim
print("=======================================================================")
print("                         Let the Adventure Begin                       ")
print("=======================================================================")

print("Introduction: THE LAST SIGNAL")
print("")
print("You wake up to the sound of an alarm.")
print("")
print("A dim red light flashes above your head. Your ears are ringing, your vision is blurry, and your body feels as though it has been asleep for weeks.")
print("")
print("You are lying on the cold metal floor of a medical examination room aboard the Astra-9, an advanced research station orbiting an uncharted planet.")
print("")
print("")
print("You slowly get up and notice three things:")
print("-The station's emergency power is failing.")
print("-The crew's whereabouts are unknown.")
print("-Something is moving inside the ventilation system.")
print("")
print("")
print("")
print("")
print("You approach the medical terminal. Its screen flickers before displaying an automated emergency report:")
print("")
#user will have to press enter to continue
input("Press Enter to continue....")
print("")
print("")
print("ASTRA-9 EMERGENCY REPORT")
print("OXYGEN LEVEL: 68%")
print("-Estimated breathable oxygen remaining: 45 minutes.")
print("")
print("POWER: 23%")
print("-Multiple station systems offline.")
print("")
print("CREW STATUS: UNKNOWN")
print("-No active life signs detected.")
print("")
print("UNIDENTIFIED MOVEMENT: DETECTED")
print("-Ventilation network, Decks 2–5.")
print("")
print("Automated message: 'If you can hear this, do not attempt to access the lower ventilation network.'")
print("")
print("You have no memory of what happened before waking up.")
print("")
print("A second message appears on the screen:")
print("")
print("'COMMANDER, IF YOU ARE AWAKE, DO NOT TRUST THE CREW MANIFEST.'")
print("Before you can investigate, the terminal shuts down.")
print("")
print("You are alone.")
print("Or at least, you think you are.")
print("")
#user will have to press enter to continue
input("Press Enter to continue....")

#game directions
print("Directions and gameplay rules")
print("Your decisions will determine whether you survive, discover the truth, and escape the station.")
print("")
print("There are 10 scenarios. Each scenario presents three choices. Every choice has consequences that affect your survival and the final outcome.")
print("")
print("Your main objectives:")
print("-Explore the station and discover what happened to the crew.")
print("-Collect useful equipment, including keycards, weapons, and oxygen supplies.")
print("-Avoid or confront the unknown creature.")
print("-Restore the station's power and life-support systems if possible.")
print("-Decide whether to repair the station or escape.")
print("")

#player stats
print("Player statistics")
print("Start the adventure with the following statistics:")
print("Statistic")
print("Oxygen: 100")
print("Health: 100")
print("Power: 50")
print("Survival points: 0")
print("Time remaining: 45 minutes")
print("Oxygen is represented as a survival resource from 100 to 0. It decreases as time passes.")

#point system
print("_" * 80)
print("""
Point system
Each decision affects your survival score.
- +10 points
   Excellent decision: improves your chances of survival.
- +5 points
   Good decision: provides a useful advantage.
- 0 points
   Neutral decision: neither helps nor hurts significantly.
- -5 points
   Poor decision: creates additional problems.
- -10 points
   Dangerous decision: puts your survival at risk.
""")
exCh = 10
goCh = 5
nuCh = 0
poCh = -5
daCh = -10

print("_" * 80)
print("""
Time passed	Oxygen lost
1 minute	2 points
2 minutes	4 points
3 minutes	6 points
5 minutes	10 points
""")

#rules for the adventure
print("""Important rules:
- If oxygen reaches zero, you die.
- If health reaches zero, you die.
- Certain keycards and items unlock special choices later.
- Some decisions have consequences that only become apparent several scenarios later.
- Your final ending depends on your score, inventory, and decisions.
Inventory
You begin with:
- Emergency flashlight
- Damaged communication device
- Basic medical kit (one use)
You can collect additional items throughout the adventure.
""")

#player inventory
print("""
Inventory
You begin with:
- Emergency flashlight
- Damaged communication device
- Basic medical kit (one use)
You can collect additional items throughout the adventure.
""")


#scenerio one
print("-"*80)
print("""
Scenario 1: The Medical Bay

You step away from the medical terminal and examine the room.

A cabinet is hanging open. Medical supplies are scattered across the floor. You notice a dead security officer near the entrance. His uniform is torn, and there are deep scratches across the metal wall beside him.

You approach the body and notice a security keycard attached to his belt.

Suddenly, something bangs against the ventilation shaft above you.

What do you do?
A 
Choice A: Search the medical cabinets for supplies.

B 
Choice B: Immediately leave the medical bay.

You decide that staying in the room is too dangerous. You leave without investigating the body or the cabinets.

C 
Choice C: Open the ventilation shaft and investigate the noise.

You climb onto a medical cabinet and remove the ventilation cover. Something rushes toward you from the darkness. You barely manage to escape, but it scratches your arm.
""")

#this will take the user choice and store it as a variable
user_choice = input("Enter your choice ( A, B, C): ").strip().upper()
while user_choice not in ["A", "B", "C"]:
    print("Invalid input. Please choose A, B, or C.")
    user_choice = input("Enter your choice (A, B, or C): ").strip().upper()
#evaluate the user choice and update the score, health, and oxygen
if user_choice == "A":
    survivalPoints += exCh
    timeRemaining -= 3
    oxygen -= 6
    print("you found 2 oxygen canisters and 1 medical injection")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
elif user_choice == "B":
    survivalPoints += nuCh
    timeRemaining -= 1
    oxygen -= 2
    print("you found nothing")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)


elif user_choice == "C":
    survivalPoints -= daCh
    health -= 15
    timeRemaining -= 4
    oxygen -= 8
    print("you found nothing and lose health")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)


#scenerio two
print("-"*80)
print("""
Scenario 2: The Security Checkpoint
You enter the main corridor.

The lights flicker, and the emergency announcement system begins repeating the same message:

"Warning. Unauthorized biological presence detected. Lockdown in progress."

At the end of the corridor, you see a security checkpoint. A locked door separates you from the central operations deck.

You notice three possible ways forward.

What do you do?
A 
Choice A: Search the security officer's body from the medical bay, if you haven't already.


B
Choice B: Attempt to bypass the security terminal.

C 
Choice C: Force the security door open.
""")
#this will take the user choice and store it as a variable
user_choice = input("Enter your choice ( A, B, C): ").strip().upper()
while user_choice not in ["A", "B", "C"]:
    print("Invalid input. Please choose A, B, or C.")
    user_choice = input("Enter your choice (A, B, or C): ").strip().upper()
#evaluate the user choice and update the score, health, and oxygen
if user_choice == "A":
    if keycard == True:
        ammunition = True
        print("you discovered a spare ammunition magazine")
    survivalPoints += exCh
    timeRemaining -= 2
    oxygen -= 4
    keycard = True
    print("You retrieve his security keycard. It grants access to restricted areas of the station.")
    print("You gained Security Keycard Level 1.")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
    
elif user_choice == "B":
    survivalPoints += nuCh
    timeRemaining -= 3
    oxygen -= 6
    power -= 5
    print("You use your technical knowledge to override the checkpoint. The process works, but the terminal consumes some emergency power.")
    print("you can now access the security checkpoint")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
    
elif user_choice == "C":
    survivalPoints -= daCh
    health -= 20
    timeRemaining -= 5
    oxygen -= 10
    print("You repeatedly strike the door's control panel. Eventually, the door opens, but the damaged electrical system releases a powerful shock.")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)


#scenerio three
#scenerio two
print("-"*80)
print("""
Scenario 3: The Crew Quarters
You enter the crew quarters.

Personal belongings are scattered everywhere. Some beds appear to have been abandoned in a hurry. A coffee cup floats near the ceiling, and someone's personal computer is still running.

You find a recording from Dr. Elena Vasquez, the station's lead scientist.

"We made a mistake. The specimen wasn't dead. It was adapting. Captain ordered us to move it to the lower laboratory, but I don't think it should ever have been brought aboard."

The recording ends abruptly.

You hear a metallic scraping sound coming from the next room.

What do you do?
A 
Choice A: Search the crew quarters for useful equipment.

B 
Choice B: Examine Dr. Vasquez's computer.

C
Choice C: Hide inside one of the sleeping compartments.
""")
#this will take the user choice and store it as a variable
user_choice = input("Enter your choice ( A, B, C): ").strip().upper()
while user_choice not in ["A", "B", "C"]:
    print("Invalid input. Please choose A, B, or C.")
    user_choice = input("Enter your choice (A, B, or C): ").strip().upper()
#evaluate the user choice and update the score, health, and oxygen
if user_choice == "A":
    enePistol = True
    eneAmmo = 1
    if ammunition == True:
        print("you load the weapon")
    survivalPoints += exCh
    timeRemaining -= 3
    oxygen -= 6
    print("You discover a compact energy pistol inside a locked storage compartment.")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
    
elif user_choice == "B":
    survivalPoints += goCh
    timeRemaining -= 4
    oxygen -= 8
    creatureResearchData = True
    engAccessCode = True
    print("You discover a research report explaining that the creature is sensitive to intense electrical energy.")
    print("You also find a partial access code for the engineering deck.")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
    
elif user_choice == "C":
    coin = ["Heads", "Tails"]
    result = random.choice(coin)
    if result == "Tails":
        print("you fell asleep while hiding and suffocated before finding any other oxygen capsules")
        sys.exit(0)
    survivalPoints -= poCh
    health -= 5
    timeRemaining -= 5
    oxygen -= 10
    print("You wait for the noise to disappear. Unfortunately, the compartment has a damaged oxygen regulator, causing you to waste valuable breathable air.")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)

#Scenerio four
print("-"*80)
print("""
Scenario 4: The Engineering Deck
You reach the engineering deck.

The reactor is unstable. Electrical sparks shoot from exposed cables, and the station's power supply is dangerously low.

You discover that the reactor can be stabilized, but doing so requires a functioning control terminal.

You also notice a maintenance locker containing several tools.

What do you do?
A
Choice A: Use the engineering access code to stabilize the reactor.

B 
Choice B: Search the maintenance locker.

C 
Choice C: Attempt to restart the reactor without examining the controls.
""")
#this will take the user choice and store it as a variable
user_choice = input("Enter your choice ( A, B, C): ").strip().upper()
while user_choice not in ["A", "B", "C"]:
    print("Invalid input. Please choose A, B, or C.")
    user_choice = input("Enter your choice (A, B, or C): ").strip().upper()
#evaluate the user choice and update the score, health, and oxygen
if user_choice == "A":
    power += 30
    survivalPoints += exCh
    timeRemaining -= 5
    oxygen -= 10
    print("You access the control terminal and successfully restart the auxiliary power system.")
    print("The station's lights turn on, and several security doors become operational again.")

    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
    
elif user_choice == "B":
    electricalTool = True
    powerCell = True
    if ammunition == True:
        if powerCell == True:
            print("you forgot you aren't suppose to put the ammo and cell in the same pocket and exploded you legs causing you to bleed out")
            sys.exit(0)
    survivalPoints += goCh
    timeRemaining -= 2
    oxygen -= 4
    print("You find a portable electrical tool and a spare power cell.")
    print("These could help you repair equipment or defend yourself.")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
    
elif user_choice == "C":
    coin = ["Heads", "Tails"]
    result = random.choice(coin)
    if result == "Tails":
        print("reactor explodes")
        sys.exit(0)
    survivalPoints -= daCh
    health -= 10
    timeRemaining -= 3
    oxygen -= 6
    power -= 15
    print("You activate the wrong sequence. The reactor releases a small energy surge, damaging the surrounding equipment.")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)

#scenerio five
print("-"*80)
print("""
Scenario 5: The Ventilation System
You hear movement above you.

The ventilation system runs throughout the entire station, connecting nearly every room. You approach a maintenance hatch and notice deep claw marks along its edges.

Suddenly, your communication device activates.

A distorted voice whispers:

"Commander... it's not one of us anymore..."

The transmission cuts out.

You realize that whatever is inside the ventilation system may be following you.

What do you do?
A 
Choice A: Use the electrical tool to overload the ventilation system.

B 
Choice B: Seal the ventilation access points.

C 
Choice C: Enter the ventilation system to investigate.

""")
#this will take the user choice and store it as a variable
user_choice = input("Enter your choice ( A, B, C): ").strip().upper()
while user_choice not in ["A", "B", "C"]:
    print("Invalid input. Please choose A, B, or C.")
    user_choice = input("Enter your choice (A, B, or C): ").strip().upper()
#evaluate the user choice and update the score, health, and oxygen
if user_choice == "A":
    if electricalTool == False:
        print("tool not inventory and unable to proceed")
    power -= 10
    survivalPoints += exCh
    timeRemaining -= 3
    oxygen -= 6
    print("You redirect electricity into the ventilation fans. A loud screech echoes throughout the station.")
    print("Something falls from the ventilation shaft and disappears into the darkness.")
    print("At the moment you are safe and can rest assured you averted the main danger. Move with confidence but still move with caution")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
    sys.exit(0)
    
elif user_choice == "B":
    survivalPoints += goCh
    timeRemaining -= 4
    oxygen -= 8
    print("You manually close the maintenance hatches and lock them.")
    print("This temporarily restricts the creature's movement.")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
    
elif user_choice == "C":
    coin = ["Heads", "Tails"]
    result = random.choice(coin)
    if result == "Tails":
        print("your head is eaten")
        sys.exit(0)
    survivalPoints -= daCh
    health -= 25
    timeRemaining -= 5
    oxygen -= 10
    print("You crawl inside with your flashlight. You discover strange biological material covering the walls")
    print("Before you can turn around, something attacks from behind.")
    print("You escape, but suffer serious injuries.")
    #displays stats
    display_statistics(health, oxygen, power, survivalPoints, timeRemaining)
