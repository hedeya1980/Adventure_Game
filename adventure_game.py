# You can use this workspace to write and submit your adventure game project.
# Run the game by entering python3 adventure_game.py in the terminal
import time
import random
import sys

ogoroth_wand=False
turns=0
total_score=0

def print_pause(s):
    print(s)
    time.sleep(2)
    
def play_again():
    global ogoroth_wand
    global turns
    choice=""
    while choice not in ["y", "n"]:
        choice=input("Would you like to play again? (y/n) ").lower()
    if choice=="y":
        print_pause("Excellent! Restarting the game ...")
        #ogoroth_wand=False
        #turns=0
        main()
        
def scoring(score):
    global turns
    global total_score
    if turns==1 and score<0:
        score=0
        total_score=0
        print_pause("*** Caution: The next time you run away, you will start losing score! ***")
        return 
    print_pause("*** Your score is now: "+str(score)+" ***")
    if (score<=0 and turns>1) or (score<10 and turns>10):
        print_pause("*** Sorry! You lost the game! ***")
        sys.exit()
    elif score>=10:
        print_pause("*** You won! Hurray! ***")
        sys.exit()

def defend(choice, enemy):
    # Things that happen when the player is approached by an enemy
    global total_score
    global ogoroth_wand
    global turns
    if choice=="1":
        if ogoroth_wand:
            print_pause("As the {} moves to cast a spell, you raise your new Wand of Ogoroth.".format(enemy))
            print_pause("The Wand of {} shines brightly in your hand as you brace yourself for the spell.".format(enemy))
            print_pause("But the {} takes one look at your shiny new wand and runs away!".format(enemy))
            print_pause("You have rid the town of the {}. You are victorious!".format(enemy))
            total_score+=2
            scoring(total_score)
        else:
            print_pause("You do your best...")
            print_pause("but your rusty old magic wand is no match for the {}.".format(enemy))
            print_pause("You have been turned into a frog!")
            total_score+=1
            scoring(total_score)
        play_again()
    else:
        print_pause("You run back into the field. Luckily, you don't seem to have been followed."+"\n")
        total_score-=1
        scoring(total_score)
        field(enemy)    

def field(enemy):
    # Things that happen when the player runs back to the field
    global turns
    turns+=1
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice=""
    while choice not in ["1", "2"]:
        choice=input("(Please enter 1 or 2): ")
    if choice=="1":
        house(enemy)
    else:
        cave(enemy)

def cave(enemy):
    global ogoroth_wand
    # Things that happen to the player goes in the cave
    print_pause("You peer cautiously into the cave.")
    if not ogoroth_wand:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Wand of Ogoroth!")
        print_pause("You discard your rusty old magic wand and take the Wand of Ogoroth with you.")
        ogoroth_wand=True
    else:    
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field."+"\n")
    field(enemy)
        
def house(enemy):
    global ogoroth_wand
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a {}.".format(enemy))
    print_pause("Eep! This is the {}'s house!".format(enemy))
    print_pause("The {} finds you!".format(enemy))
    if not ogoroth_wand:
        print_pause("You feel a bit under-prepared for this, what with only having a tiny, rusty old magic wand.")
    choice=""
    while choice not in ["1", "2"]:
        choice=input("Would you like to (1) cast a spell or (2) run away? ")
    defend(choice, enemy)

def main():
    global turns, ogoroth_wand
    # set up an array of enemies
    enemies = ['pirate', 'dragon', 'troll', 'wicked fairy']

    # choose a random enemy: 
    enemy = random.choice(enemies)

    print_pause("\nYou find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a {} is somewhere around here, and has been terrifying the nearby village.".format(enemy))
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    if not ogoroth_wand:
        print_pause("In your hand you hold your trusty (but not very effective) magic wand.")
    else:
        print_pause("In your hand you hold the Wand of Ogoroth.")
    field(enemy)

if __name__ == "__main__":
    main()
