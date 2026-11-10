# Aranthia Adventure Game

#Provides functions to allows for the program to stop running later for later when using sys.exit()

import sys

#Importing modules that allow certain functions - import time assists in creating delays in text

import time

#Settings - define variable (typewriter_print) that allows text to appear delayed

def typewriter_print(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.04)
    print()
    
#Uses variable (typewriter_print) to delay text
    
typewriter_print("⋆. ݁₊ ⊹ . ݁˖ . ݁✩₊˚.⋆☾⋆⁺₊✧Hello! Welcome to the World of Aranthia⋆. ݁₊ ⊹ . ݁˖ . ݁✩₊˚.⋆☾⋆⁺₊✧\n")

#Input pauses game to wait for user to type anything to continue. Creating breaks between text so it's easier to read and \n to create space between lines for same purpose

input("\n[Click Enter to continue]\n")

# Introduction to game
# Print ("") to show text. Have divided into separate lines so it is easier for user to read

print("Aranthia is in grave danger and we need your help! Vorgath, ruler of the Crimson Hallows has put all of the mortals of Aranthia under a sleeping trance.\n")
print("Only us animals and mythical creatures can resist against his ghastly spells... but not for long!\n")
print("If Vorgath has a hold of the Aetherium Stone, he will take over Aranthia for good and we'll all be doomed! Quickly mortal from a distant realm, sign your name now!\n")

# Enter name
#.strip().lower() so code can still be read if answer has random spaces and/or is capitalised - makes it lowercase
#f string allows variables to be inserted and recognised like in this case where {name} is a variable

name = input("Enter your name: ").strip().lower()
print()
print(f"Good luck, {name}! Your choices will decide our fate...\n")

#Check their answer to start game
#While True loop so that conditional statements can be kept inside to create a loop until something breaks it
#Conditional statments - if checks the first condition, elif checks other condition if first one is not met, else checks anything else
# == Compares two values, = Assigns a value
# break exits the while True loop onto the next part of the story and quit() exits the program
# Input asks user to enter an answer which becomes a string
#I've created a loop in which the string is dependent on start_game and answer determines user's path. Else as an invalid answer will restart the loop until the user breaks out of it. 

while True:
    start_game = input("Will you help save Aranthia? (yes/no): ").strip().lower()
    print()
    if start_game == "yes":
        print("Let's go!\n")
        break
    elif start_game == "no":
        print("Goodbye!")
        quit()
    else:
        print("Invalid. Try again.")

# Start the game
# "-" * 60 creating line for a barrier between sections
# print() provides space between lines / alternative option to \n
        
input("[Click ENTER to continue]\n")
print("-" * 60)
print()
print("Before we begin...")
    
    
# Choose weapon & inventory
# Creating an inventory for player to use later in the game
# Ending_choice empty string and inventory (empty list) here so that these variables can be determined before the start of the game

inventory = []
ending_choice = ""

# while True loop to choose weapon and add to inventory
# Wanted to try out emojis and emoticons so used print(""") so that text inside could be presented and readable
# Continue inside loop allows player to restart the loop again so second chance to answer
# f string again to input variable {weapon}
# inventory.append shows inventory
# if, elif, else statements under while True loop have to be indented to work within that loop

while True:
    print("""
    ⟡ CHOOSE YOUR WEAPON ⟡

    A) SWORD 🗡️
               
    B) CROSSBOW 🏹
         
    """)
    choice = input("Choose your weapon (a/b): ").strip().lower()
    print()

    if choice == "a":
        weapon = "sword"
        print("You have selected the sword!🗡️\n")
        
    elif choice == "b":
        weapon = "crossbow"
        print("You have selected the crossbow!🏹\n")
        
    else:
        print("Invalid choice! Please choose a or b")
        continue

    while True:
        confirm = input(f"Are you sure you want the {weapon}? You cannot change this later (yes/no): ").strip().lower()
        print()
        if confirm == "yes":
            inventory.append(weapon)
            print(f"You have acquired a {weapon}! It has been added to your inventory")
            break

        elif confirm == "no":
            print("Okay! Let's choose again.")
            break

        else:
            print("Please enter yes or no.")
    if confirm == "yes":
        break
print()
print("Your inventory:", inventory)
print()
print("-" * 60)
print()
typewriter_print("Your adventure begins...\n")
input("\n[Click Enter to continue]\n")

  

# CHAPTER 1
# Experimented by using borders for chapter headings
# .center allows text to be in center of lower and upper borders
# f string for name

print("\n" + "=" * 60)
typewriter_print("CHAPTER 1: THE ENCHANTED FOREST".center(60))
print("=" * 60 + "\n")
typewriter_print(f"Welcome {name}! You've spawned in the Enchanted Forest. I'm Lumi, a dew sprite from Sylvanmere and I'll accompany you for your journey to save Aranthia. Come on, hurry, we haven't much time!\n")
input("[Click ENTER to continue]\n")
print("You surely cannot travel in this attire! Let's pick a more appropriate outfit shall we...\n")

# while True loop again for choices
# breaks in between to get out of the loop
while True:
    
    print("Would you prefer to wear ironclad attire or gilded corsetry over a draped tunic? \n")
    print("1. Ironclad Attire")
    print("2. Gilded Corsetry")
    print()
    

    outfit = input("Choose your outfit (1 or 2): ") 

    if outfit == "1":
        print("\nPerfect! Now you're much safer!...\n")
        break
    elif outfit == "2":
        print("\nStunning! These garments are much well suited in Aranthia, you'll blend in perfectly...\n")
        break

    else:
        print("Invalid choice. Try again.\n")

# Function castle
# Define and creating a function - first one to make is the castle storyline
# global ending_choice inside the function so that when the variable is mentioned outside of the function, it is still remembered which affects the ending outcome of story
# 033[3mtext\033[0m using ANSI escape codes which in this case, formats the text to be italicised when ran
# Another f string for {name}
def castle():
    global ending_choice
    print("\n\033[3mAs you turn left, you follow a deserted, winding path as your boots crunch and muffle against leaves and soft moss.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print("\033[3mA violet haze blankets the air, an icy breeze slightly pricks upon the hairs on your neck.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print("\033[3mIn the distance you see ember, golden hues peeking through the darkness of the forest. As you approach, luminescent shards shimmer as they toast against your skin.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print(f"Sunlight? We rarely get sunlight anymore in Aranthia. Maybe it's because you're here {name}.\n")
    print("\033[3mAs you stand on the outskirts of the Enchanted Forest, you see nearby, a glimmering, majestic castle. Its' glass stained windows luminscent and resplendent reflecting the dayspring sun.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print("\n" + "=" * 60)
    typewriter_print("CHAPTER 2: THE GRAND EMBERCREST CASTLE".center(60))
    print("=" * 60 + "\n")
    print("Home to one of the five high rulers of Aranthia. There's an Astraea Pearl in the far north wing ballroom. We must be careful to go unnoticed.\n")
    input("[Click ENTER to continue]\n")
    print("We have two options of where to enter. There's a kitchen on the backside of the castle, there are no guards there. Or can you see that balcony with the lacy, flowing curtains on the second floor? We could enter through the open window.\n")
    
# Creating another while True loop for choices
# Everything inside function is indented otherwise it will be an error

    while True:
        
        print("1. Enter through the kitchen")
        print("2. Enter through the balcony")

        entrance = input("Which entrance will you choose (1 or 2): ")

        if entrance == "1":
            print("\033[3mAs you carefully cross over the meadow, you finally reach the backside of the castle. No guards. Phew...\033[0m\n")
            print("\033[3mAs you make your way to the kitchen entrance, you make sure nobody is inside.\033[0m\n")
            input("[Click ENTER to continue]\n")
            print("Oh no!\n")
            input("[Click ENTER to continue]\n")
            print("\033[3mYou see something standing over a large, dirty cauldron, facing away and stirring whatever goop is cooking as it bubbles and hisses.\033[0m\n")
            input("[Click ENTER to continue]\n")
            print("That's an ogre. Vorgath has captured all the ogres in Aranthia and forced them to be his slaves and army. I suppose Vorgath must've sent some ogres to guard this castle against trespassing animals and mythical creatures.\n")
            print("However, I can distract him. You must enter with caution.")
            input("[Click ENTER to continue]\n")
            print("\033[3mAs you safely enter, you notice your tummy grumble and churn. You feel a little light-headed. On a countertop, you see a most delectable piece of raspberry cake.\033[0m\n")

# Made a loop within a loop so that specific choices in the earlier pathway in this loop go out to a different story branch
# Breaks again to exit this loop. Elif statement with value [entrance] is indented the same because that is the original question before it branches out

            while True:
                cake = input("Would you like to eat the cake? (yes/no): ").lower()

                if cake == "yes":
                    ending_choice = "cake_yes"
                    print("\033[3mYou take a bite and swiftly finish the entire slice. It wasn't the best but it'd suffice your hunger.\033[0m\n")
                    input("[Click ENTER to continue]\n")
                    print("What are you doing? Come on, we must hurry along to the ballroom!\n")
                    break

                elif cake == "no":
                    ending_choice = "cake_no"
                    print("\033[3mYou turn away from the tempting cake and although you're starving, you don't want to take any risks or waste any time. You cradle your howling stomach and wait for Lumi.\033[0m\n")
                    input("[Click ENTER to continue]\n")
                    print("Perfect, let's go make haste to the ballroom!\n")
                    break

                else:
                    print("Invalid choice. Try again")
            break

# There are ending_choice == "" with reference to earlier. These are here to determine player's final outcome to whether they win or lose dependent on their answers that include the string ending_choice
# Essential to include the global earlier as these choices are very important to the game later outside of this function

        elif entrance == "2":
            print("\033[3mAs you carefully cross the meadow, you finally arrive beneath the balcony.\033[0m\n")
            input("[Click ENTER to continue]\n")
            print("See these vines, they're Jade Ivy. It's incredibly strong and you can use them to climb upward.\n")
            input("[Click ENTER to continue]\n")
            print("\033[3mAs you grip tightly onto the vines, you swiftly climb your way upward as your feet shuffle against the stone walls. As you near the balcony you fling your legs to snuggle them between the ivory balusters and push yourself over the railing.\033[0m\n")
            input("[Click ENTER to continue]\n")
            print("Good job! Not bad for your first time. Let's go inside.\n")
            input("[Click ENTER to continue]\n")
            print("Oh... this was Princess Caelia's room. Poor thing. Her and the rest of her family were taken by Vorgath. Now they're all trapped in his dungeon. We must save them. Let me quickly check the premises to ensure the coast is clear to the ballroom.\n")
            print("\033[3mAs Lumi exits the room, your eyes come across a sparkling, tall crystal glass, filled with a peachy rose-coloured liquid sat on the bedside table. You are decently parched.\033[0m\n")

            while True:
                drink = input("Will you take a sip of the mysterious drink? (yes/no): ").lower()

                if drink == "yes":
                    ending_choice = "drink_yes"
                    print("\033[3mYou take a deep gulp of the rosy drink. It's refreshing and cold. It tastes a little bitter but mostly sweet and sour like cranberry, soursop and bubbly fizz\033[0m\n")
                    input("[Click ENTER to continue]\n")
                    print("Coast is clear, let's go now!\n")
                    break

                elif drink == "no":
                    ending_choice = "drink_no"
                    print("\033[3mYou remain decently parched but you are fine. You leave the drink untouched and wait near the door of the room.\033[0m\n")
                    input("[Click ENTER to continue]\n")
                    print("All good, the coast is clear, let's go!\n")
                    break

                else:
                    print("Invalid choice. Try again")
            break

# Next chapter where the branches from the previous loop all end up here as it's outside the loop but still indented inside the function

    print("\n" + "=" * 60) 
    typewriter_print("CHAPTER 3: THE GRAND EMBERCREST BALLROOM".center(60))
    print("=" * 60 + "\n")
    print("\033[3mYou hurry through the hallways and eventually reach two grand pale cream doors. As you enter the ballroom, your footsteps soften as they echo from wall to wall.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print("\033[3mRight in the center, a dusty chandelier hangs from the high ceilings, its jeweled beads dangling, gently swaying as a calm breeze from the open window passes through.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print("\033[3mAt the other end of the ballroom, twinkling in the shadows, you see the Astraea Pearl.\033[0m\n")

# inventory append adds item to inventory
# continue again in loop to restart the question/loop

    while True:
        pearl_choice = input("Will you take the Astraea Pearl? (yes/no): ").lower()

        if pearl_choice == "yes":
             inventory.append("Astraea Pearl")
             print("\nYou have acquired the Astraea Pearl!\n")
             print("The Astraea Pearl has been added to your inventory.")
             break
        elif pearl_choice == "no":
            print("\nYou decide to leave the Astraea Pearl behind.")
            confirm_pearl = input("Are you sure? We might need that later. Would you like to choose again? (yes/no): ").lower()
            if confirm_pearl == "yes":
                continue
            elif confirm_pearl == "no":
                print("\nYou leave the pearl behind.\n")
                break
        else:
            print("Invalid choice. Try again")
    
# if statement not in a loop so this recognises that this is the option if you have the pearl in inventory

    if "Astraea Pearl" in inventory:

        while True:
            print("You've now acquired the Astraea Pearl! Let's make haste to the Aetherium Stone!\n")
            input("[Click ENTER to continue]\n")
            print("You have a choice now for your means of transport to Opafire.\n")
            print("Which shall you choose?\n")
            input("[Click ENTER to continue]\n")
            print("1. Horse")
            print("2. Hippogriff")

            transport_a = input("Choose your transport (1 or 2): ")

            if transport_a == "1":
                print("Good choice! Your steed moves quickly as you make your way to Opafire Labyrinth, galloping past treacherous forests and vast plains.\n")
                break
            elif transport_a == "2":
                print("Good choice! You hold on tightly as your hippogriff prepares for flight. While you properly adjust yourself, you are quickly in the air soaring above the realm of Aranthia.\n")
                input("[Click ENTER to continue]\n")
                print("From up above you see the Enchanted Forest, all different types of forests, blossoming meadows, vast deserts and treacherous plains. A foggy mist envelops the lands, shadowing everything below.\n")
                break
            else:
                print("Invalid choice. Try again")
                
# Function lagoon
# Define and creating a function - second one to make is the lagoon storyline
# global ending_choice inside the function so that when the variable is mentioned outside of the function, it is still remembered which affects the ending outcome of story

def lagoon():
    global ending_choice
    print("\n\033[3mAs you turn right, you follow a deserted, winding path as your boots crunch and muffle against leaves and soft moss.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print("\033[3mA violet haze blankets the air, an icy breeze slightly pricks upon the hairs on your neck.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print("\033[3mIn the distance you see an emerald lagoon shimmering in the shadows of the forest. As you approach, sun peeks ever so slightly from above through the canopy and its luminescent shards shimmer as they toast against your skin.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print(f"Sunlight? We rarely get sunlight anymore in Aranthia. Maybe it's because you're here {name}.\n")
    input("[Click ENTER to continue]\n")
    print("\033[3mAs you approach the lagoon, the smell of the running water is crisp and electric. Refreshingly, all shades of azure and turquoise illuminate and reflect like glass against each other.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print("\n" + "=" * 60)
    typewriter_print("CHAPTER 2: AURELIA'S LAGOON".center(60))
    print("=" * 60 + "\n")
    print("Only few are ever so lucky to come here because it is the only place in all of Aranthia where it can hide itself from unwanted visitors. It's also home to one of the Astraea Pearls in possession by Aurelia, the mermaid who rules this lagoon. We have to earn her trust if we want to acquire the pearl from her.\n")
    print("What should we do? Do we want to go see Celeste's Water Lily or wait by the waterfall?\n")

# More choices = more while True loops
# Am very careful to not create new values the same name as others so that code has no errors
# ending_choice again here - these answers will directly impact final results for player
# Both functions, this one and lagoon have same structure, just different storylines

    while True:
        
        print("1. Celeste's Water Lily")
        print("2. Waterfall")

        explore = input("Which would you like to explore (1 or 2): ")
        if explore == "1":
            print("This is Celeste's Water Lily. It's the largest flower in all of Aranthia and it's said that if you make a wish, it will bless you and grant whatever you desire to become true!\n")
            input("[Click ENTER to continue]\n")
            print("You spot a bundle of silver moondust on the lily pad.\n")

            while True:
                moondust = input("Will you sprinkle some moondust over the lagoon? (yes/no): ").lower()

                if moondust == "yes":
                    ending_choice = "moondust_yes"
                    print("\033[3mYou sprinkle the moondust over the lagoon as it shines over the water's surface.\033[0m\n")
                    input("[Click ENTER to continue]\n")
                    print("\033[3mTo your surprise, you see a mermaid appear as she sirens you over.\033[0m\n")
                    break

                elif moondust == "no":
                    ending_choice = "moondust_no"
                    print("\033[3mYou choose to not sprinkle the moondust and rather admire the Water Lily\033[0m\n")
                    input("[Click ENTER to continue]\n")
                    print("\033[3mTo your surprise, you see a mermaid appear as she sirens you over.\033[0m\n")
                    break

                else:
                    print("Invalid choice. Try again")
            break
        
        elif explore == "2":
            print("\033[3mThe waterfall is enticing, glittery as it streams and crashes below.\033[0m\n")
            input("[Click ENTER to continue]\n")
            print("\033[3mYou feel quite parched.\033[0m\n")
            
            while True:
                waterfall = input("Would you like to take a sip from the waterfall? (yes/no: ").lower()

                if waterfall == "yes":
                    ending_choice = "waterfall_yes"
                    print("\033[3mYou cup your hands and take a sip from the waterfall.\033[0m\n")
                    input("[Click ENTER to continue]\n")
                    print("\033[3mHow sweet!\033[0m\n")
                    input("[Click ENTER to continue]\n")
                    print("\033[3mTo your surprise, you see a mermaid appear as she sirens you over.\033[0m\n")
                    break
                elif waterfall == "no":
                    ending_choice = "waterfall_no"
                    print("\033[3mYou choose to not drink from the waterfall and remain parched.\033[0m\n")
                    input("[Click ENTER to continue]\n")
                    print("\033[3mTo your surprise, you see a mermaid appear as she sirens you over.\033[0m\n")
                    break
                else:
                    print("Invalid choice. Try again")

            break
        
# All storylines earlier that have branched outward in this function all come here to the next chapter no matter the choice

    print("\n" + "=" * 60)
    typewriter_print("CHAPTER 3: AURELIA".center(60))
    print("=" * 60 + "\n")

    print("Hello, welcome to Aranthia.\n")
    input("[Click ENTER to continue]\n")
    print("My name is Aurelia.\n")
    input("[Click ENTER to continue]\n")
    print("I know well of your plans to save our realm.\n")
    print("I've trusted you into my lagoon and I can see how true your heart is.\n")
    input("[Click ENTER to continue]\n")
    print(f"Here take this Astraea Pearl, I hope it serves you well {name}\n")

# Pearl choice is repeated in both functions as it is pivotal to the story later as both storylines comes together

    while True:
        pearl_choice = input("Will you take the Astraea Pearl? (yes/no): ").lower()
        if pearl_choice == "yes":
             inventory.append("Astraea Pearl")
             print("\nYou have acquired the Astraea Pearl!\n")
             print("The Astraea Pearl has been added to your inventory.")
             break
        elif pearl_choice == "no":
             print("\nYou decide to not take the Astraea Pearl.")
             confirm_pearl = input("Are you sure? We might need that later. Would you like to choose again? (yes/no): ").lower()
             if confirm_pearl == "yes":
                continue
             elif confirm_pearl == "no":
                print("\nYou leave the pearl behind.\n")
                break
        else:
            print("Invalid choice. Try again")
    
# If you don't take the pearl, you skip this next part and skip straight to the next function

    if "Astraea Pearl" in inventory:

        while True:
            print("You've now acquired the Astraea Pearl! Let's make haste to the Aetherium Stone!\n")
            input("[Click ENTER to continue]\n")
            print("You have a choice now for your means of transport to Opafire.\n")
            print("Which shall you choose?\n")
            input("[Click ENTER to continue]\n")
            print("1. Gondola")
            print("2. River Wyrm")

            transport_b = input("Choose your transport (1 or 2): ")

            if transport_b == "1":
                print("Good choice! The gondola rows itself as it passes through a shortcut to Opafire Labyrinth.\n")
                break
            elif transport_b == "2":
                print("Good choice! Aurelia summons a river wyrm and sirens it to Opafire Labyrinth. As you hold on tightly, the river wyrm slithers its way through shortcuts and secret passages.\n")
                break
            else:
                print("Invalid choice. Try again")
                
# As the next line is not indented, it is outside of the previous function.
# Both storylines end up here
# This next section is actually said earlier in the game but could only be said now because now both functions of the storyline exist to where it branches out
# So the original path that is very early in the game is determined which way to go in the forest. Function only runs if like "name of function()" is explicitly said in code

while True:
    print(f"Quickly {name}! We haven't much time, we must make way to find the Aetherium Stone.\n")
    input("[Click ENTER to continue]\n")
    print("The Aetherium Stone is located at Opafire Labyrinth but we cannot enter without an Astraea Pearl, there's only a few left in our realm. Let's find one first shall we.\n")
    
    path = input("Would you like to turn left or right? (left or right): ").lower()

    if path == "left":
        castle()
        break

    elif path == "right":
        lagoon()
        break

    else:
        print("Invalid choice. Try again!")

# Last function I've created 
# Define and creating a function - this is the last function which earlier functions of castle and lagoon both merge into this plotline
# global ending_choice is used earlier so that choices from other functions are relevant inside this function to reference earlier decisions
# If pearl was not obtained from earlier, player jumps straight to Opafire function storyline

def opafire():
    print("\n" + "=" * 60)
    typewriter_print("CHAPTER 4: OPAFIRE LABYRINTH".center(60))
    print("=" * 60 + "\n")

    print("\033[3mYou finally arrive at Opafire Labyrinth. The outside, tall and ancient, its' walls a dark cobblestone covered in tangled overgrown mossy, deep viridian vines.\033[0m\n")
    input("[Click ENTER to continue]\n")
    print("\033[3mAs you approach the labyrinth to what seems to be the entrance, there is a round crevice dented into the wall that appears to be for the Astraea Pearl.\033[0m\n")
    input("[Click ENTER to continue]\n")

# If item is in inventory, story goes on but if the pearl is missing, the game is over
# sys.exit() exits the player from game
# Everything indented to fit inside function

    if "Astraea Pearl" in inventory:
        print("Luckily we have the Astraea Pearl in our inventory!\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou place the pearl in the crevice and slowly the labyrinth walls begin to open.\033[0m\n")
        
    else:
        print("You cannot enter without the Astraea Pearl.\n")
        print("Vorgath has managed to enter before you and retrieve the Astraea Pearl himself!\n")
        print("You have failed your mission to save Aranthia...\n")
        typewriter_print("Goodbye. GAME OVER")
        sys.exit()

 # Doesn't need break because not in loop, goes straight to next part
 
    input("[Click ENTER to continue]\n")
    print("...It's pitch black inside\n")
    input("[Click ENTER to continue]\n")
    print("Choose what to use as a source of light!")
    input("[Click ENTER to continue]\n")
    print("1. Candle")
    print("2. Glow moss")

  # Some options do not have an effect in the game, they're just for the player to choose and interact with the story like ths "light" one
  
    while True:
        light = input("What will you choose? (1 or 2): ")

        if light == "1":
            print("\nYou have chosen to use a candle!\n")
            break

        elif light == "2":
            print("\nYou have chosen to use glow moss\n")
            break
        else:
            print("Invalid choice. Try again")

# Mini maze simulation - I used while True loops to create 2 series of options and use continue so that the player can remake decisions
# turn_a & turn_b named different so values aren't confused

    print("\033[3mWith caution, you walk through the labyrinth and come across your first junction.\033[0m\n")
    input("[Click ENTER to continue]\n")

    while True:
        turn_a = input ("Which way would you like to turn? (left or right): ")

        if turn_a == "left":
            print("\nYou hit a dead end!\n")
            print("So many cobwebs... let's turn back.\n")
            input("[Click ENTER to continue]\n") 
            continue
        elif turn_a == "right":
            print("\nYou walk some more trying not to look back into the black abyss.\n")
            break
        else:
            print("Invalid choice. Try again")

    print("\033[3mYou come across another junction\033[0m\n")

    while True:
        turn_b = input ("Which way would you like to turn? (left or right): ")

        if turn_b == "right":
            print("\nYou hit a dead end!\n")
            print("There seems to be a mysterious red goo dripping on the walls... let's turn back.\n")
            input("[Click ENTER to continue]\n") 
            continue
        elif turn_b == "left":
            print("\nYou've reached the center of the labyrinth!\n")
            break
        else:
            print("Invalid choice. Try again")
            
# Indented out of loop so that all decisions lead to next story pathway

    print("\n" + "=" * 60)
    typewriter_print("FINAL CHAPTER".center(60))
    print("=" * 60 + "\n")

    print("\033[3mSconces on the corners of the wall light up as you enter, revealing the Aetherium Stone, fiery and glistening inside a glass encasement.\033[0m\n")
    input("[Click ENTER to continue]\n")
    typewriter_print("Oh no...\n")
    input("[Click ENTER to continue]\n")
    typewriter_print("...It's Vorgath!\n")
    print("How did he manage to get in here? He must've been following us!\n")
    input("[Click ENTER to continue]\n")
    print("Quick take out your weapon!\n")

# These are all 8 different endings based from the ending_choice strings that have been mentioned earlier outside of this function
# Does not require while True loops because there are no more answers to input for the player
# if and elif conditional statements - ending directly impacted from conditions earlier chosen by player
# no "else" because player must have had to choose answers from previous functions to get to this point
# There are 4 good endings & 4 bad endings
#Below this are ending_choice's from the castle function

    if ending_choice == "cake_yes":
        print("\033[3mYou take out your weapon and fight against Vorgath!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("His powers are too strong!\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mHis blade cuts against your upper waist...\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mBut in a defence, you push him away with your hands and it burns him!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mThe cake you ate earlier contained Embergrit! Vorgath's kind cannot come into any type of contact with it.\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("You defeat Vorgath and acquire the Aetherium Stone!\n")
        input("[Click ENTER to continue]\n")
        print("Success! You have saved the World of Aranthia!\n")

    elif ending_choice == "cake_no":
        print("\033[3mYou take out your weapon and fight against Vorgath!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("His powers are too strong!\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou feel lightheaded again and you pass out...\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("...\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou wake up and Vorgath and the Aetherium Stone are gone!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("It'a too late now! You have failed in saving the World of Aranthia...\n")

    elif ending_choice == "drink_yes":
        print("\033[3mYou take out your weapon and fight against Vorgath!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("His powers are too strong!\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mAll of a sudden your vision becomes hazy and you can't see anything!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mIt must've been the drink!...You pass out...\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("...\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou wake up and Vorgath and the Aetherium Stone are gone!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("It'a too late now! You have failed in saving the World of Aranthia...\n")

    elif ending_choice == "drink_no":
        print("\033[3mYou take out your weapon and fight against Vorgath!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mHe's strong but you're quicker. His blade takes a jab at your upper waist.\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou attack him and he falls backwards and rolls down a set of a million stairs!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("You defeat Vorgath and acquire the Aetherium Stone!\n")
        input("[Click ENTER to continue]\n")
        print("Success! You have saved the World of Aranthia!\n")
        
# Below this are ending_choice 's from the lagoon function

    elif ending_choice == "moondust_yes":
        print("\033[3mYou take out your weapon and fight against Vorgath!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mHe's strong but you're quicker. His blade takes a jab at your upper waist.\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou distract him by blowing into the air some extra moondust you still have from the lagoon!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou attack him and he falls backwards and rolls down a set of a million stairs!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("You defeat Vorgath and acquire the Aetherium Stone!\n")
        input("[Click ENTER to continue]\n")
        print("Success! You have saved the World of Aranthia!\n")

    elif ending_choice == "moondust_no":
        print("\033[3mYou take out your weapon and fight against Vorgath!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("His powers are too strong!\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou trip over a loose vine and fall down a set of stairs!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mWhen you get back up, Vorgath and the Aetherium Stone are gone!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("It'a too late now! You have failed in saving the World of Aranthia...\n")

    elif ending_choice == "waterfall_yes":
        print("\033[3mYou take out your weapon and fight against Vorgath!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("His powers are too strong!\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mHis blade cuts against your upper waist...\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mBut it instantly heals!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou get back up and fight until Vorgath surrenders!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("You defeat Vorgath and acquire the Aetherium Stone!\n")
        input("[Click ENTER to continue]\n")
        print("Success! You have saved the World of Aranthia!\n")

    elif ending_choice == "waterfall_no":
        print("\033[3mYou take out your weapon and fight against Vorgath!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("His powers are too strong!\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mYou trip over a loose vine and fall down a set of stairs!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("\033[3mWhen you get back up, Vorgath and the Aetherium Stone are gone!\033[0m\n")
        input("[Click ENTER to continue]\n")
        print("It'a too late now! You have failed in saving the World of Aranthia...\n")

# Next line is printed no matter the ending as it's not part of the earlier conditional statements

    typewriter_print("Thank you for playing! Goodbye!")
    
# opafire() function must be included so that after the castle and lagoon functions, it merges into the opafire function and storyline
# Otherwise game will not continue after the functions before this one

opafire()

# The End! :)
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
                
        
        
        
        
        
        
        
        
        
        
        
    


    

    

        
        
    
    
            


    


    
        
        
        
        
        
        
        
        
                
                
                
                
                

            
    
    
          
    
    
    
            
            
         

    
     
    


    
                    
                

            
        

    

    
    









 
