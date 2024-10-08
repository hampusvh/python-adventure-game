# Projektarbete Hampus


# I detta projektarbete har jag valt att göra ett textbaserat
# äventyrsspel. Det finns en huvudmeny och när man väljer att börja
# spelet så kommer det menyer där man måste välja alternativ för
# att gå vidare i spelet. Beroende på vad användaren väljer så finns
# det olika scenarion. Användaren kan välja att slåss mot olika
# varelser. I andra skeden av spelet så kan det hända att användaren
# dör och spelet avslutas, om användaren väljer "fel" alternativ.
# I tärningsspelet så är det de slumpmässiga resultat av tärningen
# som avgör om användaren kan gå vidare i spelet eller inte.

# Det här spelet har inget slut och inget mål. Den har få alternativ
# och loopar i slutändan till olika funktioner som man kan göra om
# och om igen.


import random

# Har valt 'import random' till funktionen med tärningsspelet
# samt till 'encounter_monster' för att generera slumpmässiga
# integers som är passande till programmet. 

import time

# Har valt 'import time' för funktionen time.sleep() som gör en
# fördröjning på texten som printas i programmet. Detta för att
# inte all text ska printas samtidigt, och att det blir en form
# av "flöde" i programmet. 

def safe_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == "quit":
        print("\n\nExiting the game.\nPress ENTER to close:")
        input()
        mainmenu()
    return user_input

# Har lagt till en funktion, safe_input, som gör det möjligt för
# användaren att när som helst avsluta programmet och gå tillbaka
# till huvudmenyn. Från huvudmenyn kan användaren välja alternativet
# Quit för att stänga programmet. 

def mainmenu():
    print("\n\n\n ---------- GAME MENU ---------- \n")
    print("At any moment during the game,\nyou can type 'quit' to exit")
    print("and return to this menu.") 
    print("\n------- Select an option: -------\n")
    optionmenu = safe_input("       1.Begin adventure\n       2.Quit\n")
    
    while True:
        if optionmenu == "1":
            welcome()
        elif optionmenu == "2":
            quit()
        else:
            optionmenu = safe_input("Please select a valid option.\n")

def journeystart():
    print("\n\n_______The journey begins!_______\n")
    time.sleep(0.5)
    print("\nYou wander on an exciting path.")
    print("\nSoon, the path seems to divide into two directions.")
    time.sleep(0.5)
    print("\n          \U0001f333                         \U0001f311")
    print("\nOne leads into a forest. The other leads into a cave.")
    time.sleep(0.5)
    option = safe_input("\nWhere would you like to go?\n\n1. Enter the forest\n2. Enter the cave\n")

    while option != "1" and option != "2":
        option = safe_input("Please select a valid option.\n")
    if option == "1":
        print("\n        You decide to enter the forest...")
        forest()
    elif option == "2":
        print("\nYou decide to enter the cave...")
        time.sleep(0.5)
        cave()

def welcome():
    print("\nWelcome, adventurer,")
    time.sleep(0.5)
    print("\nan exciting journey awaits!")
    time.sleep(0.5)
    print("\nBefore you continue, there are two things you might want to consider.\n")
    time.sleep(1)
    print("           \U0001f5e1                     \U0001f9ea\n")
    print("Here is a magical sword. Here is also an antidote.")
    time.sleep(0.5)
    print("\nDo you want to bring anything with you?")
    time.sleep(0.5)
    select = safe_input("\n1. Magical Sword\n2. Antidote\n3. Nothing\n4. Go back to main menu\n")

    while True:
        if select == "3":
            select = safe_input("It would be wise of you to bring something with you.\n")
        elif select == "1":
            print("\n       \U0001f5e1\n\nYou chose the sword.\nYou must be brave!")
            time.sleep(0.5)
            print("\nPress ENTER to begin journey:\n")
            input()
            journeystart()
        elif select == "2":
            print("       \U0001f9ea\n\nThe antidote!\nYou made a good choice.")
            time.sleep(0.5)
            print("\nPress ENTER to begin journey:\n")
            input()
            journeystart()
        elif select == "4":
            mainmenu()
        else:
            select = safe_input("Please select a valid option.\n")

# I den här delen av programmet behöver användaren välja ett av de två
# givna alternativen för att kunna gå vidare. Inget av alternativen har
# en särskild betydelse senare i programmet.

def forest():
    print("\n                 \U0001f333 \U0001f333 \U0001f333")
    print("\n         This is a mysterious place.")
    time.sleep(0.5)
    print("\n       Suddenly, a creature approaches!")
    time.sleep(0.5)
    print("\n                      \U0001f479\n")
    time.sleep(1)
    print("Make a choice:")
    option = safe_input("\n1. Fight\n2. Run away\n")
    while option != "1" and option != "2":
        option = safe_input("Please select a valid option.\n")
    if option == "1":
        encounter_monster()
    if option == "2":
        runaway()  

def cave():   
    print("\n        \U0001f311\U0001f311\U0001f311\U0001f311\U0001f311\U0001f311\U0001f311")
    time.sleep(0.5)
    print("\n      This is a dark place.")
    time.sleep(0.5)
    print("\n  Suddenly, a creature approaches.")
    time.sleep(0.5)
    print("\n               \U0001f9cc\n")
    time.sleep(0.5)
    print("   The creature confronts you!\n")
    time.sleep(0.5)
    print("Make a choice:")
    option = safe_input("\n1. Fight\n2. Run away\n")
    while option != "1" and option != "2":
        option = safe_input("Please select a valid option.\n")
    if option == "1":
        encountertwo()
    if option == "2":
        print("You run back and exit the cave!")
        time.sleep(0.5)
        print("That was close, but you made it out!")
        time.sleep(0.5)
        print("What will you do next?")
        time.sleep(0.5)
        question = safe_input("\n\n1. Explore the forest\n2. Go back into the cave\n")
        if question == "1":
            print("You decide to enter the forest...")
            time.sleep(0.5)
            return forest()
        elif question == "2":
            print("You decide to enter the cave...")
            time.sleep(0.5)
            return cave()
        else:
            question = safe_input("Please select a valid option.\n")

def explorecave():
    print("\nYou decide to explore the cave further.")
    time.sleep(0.5)
    print("\nYou keep wandering. It's too dark to see.")
    time.sleep(0.5)
    print("\nSuddenly, you slip and fall down a deep pit!")
    time.sleep(0.5)
    print("\n\nPress ENTER to continue:")
    input()
    return pitfall()
        
def pitfall():
    print("\nYou find yourself in a dark place.")
    time.sleep(0.5)
    print("\nYou are in trouble, there seems to be no way out.")
    time.sleep(0.5)
    print("\nYou find a dice on the ground.")
    print("\n             \U0001f3b2\n")
    time.sleep(0.5)
    print("\nYou pick up the dice and find a note..")
    time.sleep(0.5)
    print("\n             \U0001f4dc\n")
    time.sleep(0.5)
    print("\nPress ENTER to read the note:")
    input()
    print("\nYou read the note. It says:\n")
    time.sleep(0.5)
    print("\n\n        ''TO ESCAPE, ")
    print("       YOU MUST ROLL A 6")
    print("     YOU HAVE 3 ATTEMPTS...''\n\n")
    time.sleep(1)
    rolldice = safe_input("\nDo you wish to try your luck?\n\n1. Yes\n2. No\n")
    if rolldice == "1":
        return dicegame()
    elif rolldice == "2":
        print("\nYour journey will end here...")
        print("\nPress ENTER to continue:\n")
        input()
        mainmenu()
    else:
        rolldice = safe_input("Invalid option.\n")

def roll_dice():
    return random.randint(1, 6)

def dicegame():
    input("\nPress ENTER to roll:\n")
    rolls = 0
    while rolls < 3:
        dice_roll = roll_dice()
        print("         You rolled:", dice_roll)
        if dice_roll == 6:
            print("\n   Congratulations! You rolled a 6!")
            time.sleep(0.5)
            print("\nYou will now be teleported out of the cave.")
            input("\n     Press ENTER to continue:\n")
            return journeymenu()
        else:
            rolls += 1
            if rolls < 3:
                print("\n     Better luck next time!")
                input("\nPress ENTER to roll the dice again...\n")
            else:
                print("\n\n    You have failed in rolling 6 ...")
                time.sleep(0.5)
                print("\n       Your journey ends here.\n")
                print("                \U0001f480")
                time.sleep(0.5)
                input("\n    Press ENTER to return to menu:\n")
                return mainmenu()

# I den här delen av programmet så kommer det ett tärningsspel.
# När man väljer att kasta tärningen kommer en slumpmässig siffra
# mellan 1-6. Om användaren slår 6 så flyttas man till journeymenu().
# Man har 3 försök på sig, annars förlorar man och återgår till
# huvudmenyn. 

def journeymenu():
    print("\n\n\n_______You are back, and find yourself on a path with choices_______\n")
    time.sleep(0.5)
    print("\nWhat would you like to do next?\n")
    choice = safe_input("1. Enter the forest\n2. Enter the cave\n")
    while choice != "1" and choice != "2":
        choice = safe_input("Please select a valid option.\n")
    if choice == "1":
        print("\n       You decide to enter the forest...")
        time.sleep(0.5)
        forest()
    elif choice == "2":
        print("\n   You decide to enter the cave...")
        time.sleep(0.5)
        cave()

def encounter_monster():
    print("\n\n_____________Prepare to fight!_____________\n")
    time.sleep(0.5)
    
    player_health = 100
    monster_health = 50
    
    while player_health > 0 and monster_health > 0:
        print("\n\n            Your health:", player_health)
        print("           Creature's health:", monster_health)
        print("\nSelect option:\n")
        action = safe_input("1. Attack\n2. Run away\n")
        
        if action == "1":
            player_damage = random.randint(10, 20)
            monster_damage = random.randint(5, 15)
            print("\nYou attack the creature and deal", player_damage, "damage!")
            monster_health -= player_damage
            time.sleep(0.5)
            if monster_health > 0:
                print("The creature strikes back and deals", monster_damage, "damage!")
                player_health -= monster_damage
                time.sleep(0.5)
        elif action == "2":
            print("\nYou attempt to run away...")
            time.sleep(0.5)
            escape_chance = random.random()
            if escape_chance < 0.5:
                print("You successfully escape from the creature!")
                return journeymenu()
            else:
                print("You couldn't escape! The creature blocks your path.")
                time.sleep(0.5)
                print("Prepare to fight again!")
        else:
            action = safe_input("Invalid option.\n")

    if player_health <= 0:
        print("\nYou have been defeated by the creature. The journey is over.")
        print("\n          \U0001f480\n")
        time.sleep(1)
        print("Press ENTER to continue:\n")
        input()
        mainmenu()
    elif monster_health <= 0:
        print("\n          You defeat the creature!\n")
        time.sleep(0.5)
        print("          What do you wish to do next?\n")
        option = safe_input("1. Loot creature\n2. Proceed with adventure\n")
        while option != "1" and option != "2":
            option = safe_input("Please select a valid option.\n")
        if option == "1":
            print("\nYou search the fallen creature.")
            time.sleep(0.5)
            print("\nYou find a mysterious book.")
            time.sleep(0.5)
            print("\n            \U0001f4d5\n")
            time.sleep(0.5)
            readbook = safe_input("\nDo you want to read the book?\n\n1. Yes\n2. No\n")
            if readbook == "1":
                print("\nYou read through the pages of the book.")
                time.sleep(0.5)
                print("\nThere is nothing written in it...")
                time.sleep(0.5)
                print("\nPress ENTER to continue\nthe adventure:\n")
                input()
                return proceed()
            elif readbook == "2":
                print("\nYou decide to leave the book unread.\n")
                print("Press ENTER to continue\n   the adventure:\n")
                input()
                return proceed()
            else:
                readbook = safe_input("Invalid option.\n")
        elif option == "2":
            proceed()

# Här finns två liknande funktioner med en monster encounter, där
# användaren har valt att slåss. Player och monster damage är en
# slumpmässig integer som påverkar varandras health. Man kan göra
# spelet svårare och höja siffrorna för monster damage samt health.
# För att göra programmet lite enklare och demonstrera hur det funkar
# så är det nästan omöjligt för användaren att förlora i denna funktion.

# Användaren kan också välja att springa iväg, och detta alternativ
# har ett slumpmässigt genererat resultat på 50% för att lyckas med detta.  

def encountertwo():
    print("_____________Prepare to fight!_____________")
    time.sleep(1)
    
    player_health = 100
    monster_health = 50
    
    while player_health > 0 and monster_health > 0:
        print("\n            Your health:", player_health)
        print("           Creature's health:", monster_health)
        print("\nSelect option:\n")
        action = safe_input("1. Attack\n2. Run away\n")
        
        if action == "1":
            player_damage = random.randint(10, 20)
            monster_damage = random.randint(5, 15)
            print("\nYou attack the creature and deal", player_damage, "damage!")
            monster_health -= player_damage
            time.sleep(0.5)
            if monster_health > 0:
                print("The creature strikes back and deals", monster_damage, "damage!")
                player_health -= monster_damage
                time.sleep(0.5)
        elif action == "2":
            print("\nYou attempt to run away...")
            time.sleep(0.5)
            escape_chance = random.random()
            if escape_chance < 0.5:
                print("You successfully escape from the creature!")
                return journeymenu()
            else:
                print("You couldn't escape! The creature blocks your path.")
                time.sleep(0.5)
                print("Prepare to fight again!")
        else:
            print("\nInvalid choice. Please try again.")

    if player_health <= 0:
        print("\nYou have been defeated by the creature. Your journey ends here.")
        print("\n          \U0001f480\n")
        time.sleep(1)
        print("Press ENTER to continue:")
        input()
        mainmenu()
    elif monster_health <= 0:
        print("You have defeated the creature!\n")
        time.sleep(0.5)
        choseincave = safe_input("\nWhat do you wish to do?\n\n1. Go back and exit the cave\n2. Continue exploring\n")
        if choseincave == "1":
            return journeymenu()
        elif choseincave == "2":
            return explorecave()
        else:
            choseincave = safe_input("Please select a valid option.\n")

def runaway():
    print("\nYou run for your life and don't look back.\n")
    time.sleep(0.5)
    print("\nYou escape, and after a while you feel safe again.\n")
    time.sleep(0.5)
    print("\nYou are lucky. You made it this time.")
    time.sleep(0.5)
    journeymenu()

def proceed():
    print("\n         ------- The journey continues -------\n\n\n")
    time.sleep(0.5)
    print("You feel there is nothing that can stop you.")
    time.sleep(0.5)
    print("\nAs you wander, you find something on the ground.")
    time.sleep(0.5)
    print("\nIt looks like a mushroom.")
    time.sleep(0.5)
    print("\n     \U0001f344\n")
    time.sleep(0.5)
    print("What do you want to do with it?\n")
    time.sleep(1)
    option = safe_input("\n1. Pick it up and eat it.\n2. Leave it where it is.\n")
    while option != "1" and option != "2":
        option = safe_input("Please select a valid option.\n")
    if option == "1":
            print("\n           You eat the mushroom.")
            time.sleep(0.5)
            print("\n          That was a silly mistake,")
            time.sleep(0.5)
            print("\n         the mushroom is poisonous...")
            time.sleep(0.5)
            print("\n           Eventually it kills you.")
            time.sleep(0.5)
            print("\n                   \U0001f480\n")
            time.sleep(1)
            print("           Press ENTER to continue:")
            input()
            mainmenu()
    if option == "2":
            print("\nYou made a wise choice,")
            time.sleep(0.5)
            print("\nit's better to leave it where it is...")
            time.sleep(0.5)
            print("\nPress ENTER to continue:")
            input()
            journeymenu()

mainmenu()
