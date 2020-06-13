import time
import sys
import random




def print_pause(message):
    print(message)
    time.sleep(1.5)


def intro():
    print("************************************************************")
    print_pause("You find Someone leave you in a Dense forest "
                "late in the evening.")
    print("************************************************************")
    print_pause("It's was 2'O Clock Night")
    print("************************************************************")
    print_pause("Your Aim is to safely reach to the Highway So any one Can "
                "Give You  lift ")
    print("************************************************************")
    print_pause("And you can Reach Your Home")
    print("************************************************************")




def find_trunk(items_list):
    print_pause("And walking through your way ,you find a box contain three items in it.")
    print("************************************************************")
    print_pause("However, only one item can take with yourself")
    print("************************************************************")
    print_pause("Which item would you like to take?\n")
    print_pause(f" - {items_list[0].capitalize()}\n"
                f" - {items_list[1].capitalize()}\n"
                f" - {items_list[2].capitalize()}\n")
    item = valid_input("Please, enter a name of the item.\n", items_list)
    print("************************************************************")
    print_pause(f"You put {item} in your bag and continue your way.")
    print("************************************************************")
    items_list.remove(item)
    return item
 
 
    

def valid_input(message, options):
    while True:
        response = input(message).lower()
        for option in options:
            if option in response:
                response = option
                return response
        print_pause("Sorry, this option is not avaliable")

        

def trick_or_treaters(item, play_again_list):
    if item == "gold":
        print_pause("Gold made the robbers very happy.")
        print("************************************************************")
        print_pause("They let you continue your way.")
        print("************************************************************")
    else:
        if item == "guns":
            print_pause("Robbers are in major Quantity "
                        "and they also Contains Guns.")
            print("************************************************************")
        elif item == "iron_rod":
            print_pause("iron_rod isn't something robbers expect "
                        "to get at Halloween!. It only made them cry.")
        print("************************************************************")
        print_pause("After Seeing the Gun In Your Hand They Will Kill You")
        print("************************************************************")
        print_pause("You Killed By Robbers :(  You didn't able to reach your home.")
        print("************************************************************")
        print_pause("You lost the Game")
        print("************************************************************")
        play_again(play_again_list)






def bears(item, play_again_list):
    if item == "guns":
        print_pause("With your guns you shot directly to Bears' heads.")
        print("************************************************************")
        print_pause("Bears died! You may continue your way.")
        print("************************************************************")
    elif item == "gold":
        print_pause("You selected Gold ")
        print("************************************************************")
        print_pause("But what would you do with gold if yor are not alive")
        print("************************************************************")
        print_pause("This wasn't effektive against Bears!")
        print("************************************************************")
        print_pause("You lost! :( 🐢 You've also become food for Bear   "
                    "you won't come back home.")
        print("************************************************************")
        play_again(play_again_list)
    elif item == "iron_rod":
        print_pause("This wasn't effektive against bears!")
        print("************************************************************")
        print_pause("You lost! You've also become a zombie and "
                    "you won't come back home.")
        print("************************************************************")
        play_again(play_again_list)

        

def cobra_snake(item, play_again_list):
    if item == "iron_rod":
        print_pause("You splashed the cobra_snake with iron_rod.")
        print("************************************************************")
        print_pause("All cobra_snake died! You may continue your way.")
        print("************************************************************")
    elif item == "gold" or item == "guns":
        print_pause("This wasn't effektive against cobra_snake!")
        print_pause("************************************************************")
        print_pause("You lost! You've killed by Cobra_snake poison "
                    "you won't come back home.")
        print("************************************************************")
        play_again(play_again_list)



def action_1(animals, item, items_list, play_again_list, enemies):
    
    enemies.remove(animals)
    if animals == "robbers":
        trick_or_treaters(item, play_again_list)
    elif animals == "bears":
        bears(item, play_again_list)
    elif animals == "cobra_snake":
        cobra_snake(item, play_again_list)
    print_pause("Your bag is empty again.")
    print("************************************************************")
    items_list.append(item)

    

def action_2(animals, item, items_list, play_again_list, enemies):
    print_pause("You are back at the box.")
    print("************************************************************")
    print_pause(f"Which item do you want to exchange {item} for?\n")
    items_list.append(item)
    print_pause(f" - {items_list[0].capitalize()}\n"
                f" - {items_list[1].capitalize()}\n")
    item = valid_input("Please, enter a name of the item.\n", items_list)
    print_pause(f"You put {item} in your bag and return to the {animals}.")
    items_list.remove(item)
    action_1(animals, item, items_list, play_again_list, enemies)

def start_game():
    items_list = ["gold", "guns", "iron_rod"]
    enemies = ["robbers", "bears", "cobra_snake"]
    actions = ['1', '2']
    play_again_list = ["yes", "no"]
    intro()
    game_items(items_list, enemies, actions, play_again_list)   



def meet_animals(item, items_list, actions, play_again_list, enemies):
      
    animals = random.choice(enemies)
    print_pause(f"Suddenly, you've been found {animals} in your way.")
    print("************************************************************")
    print_pause("What's your next step?\n")
    print("************************************************************")
    print_pause(f" 1. Get your {item} out of the bag.\n"
                " 2. Run back to the box to exchange your item.\n")
    action = valid_input("Please enter a number 1 or 2.\n", actions)
    if action == '1':
        action_1(animals, item, items_list, play_again_list, enemies)
    elif action == '2':
        action_2(animals, item, items_list, play_again_list, enemies)



def play_again(play_again_list):
    print_pause("Would you like to play again?")
    response = valid_input("Please, enter yes or no.\n", play_again_list)
    if response == "yes":
        print_pause("Great! Restarting the game...\n")
        start_game()
    elif response == "no":
        sys.exit()


def game_items(items_list, enemies, actions, play_again_list):
    while len(enemies) != 0:
        item = find_trunk(items_list)
        meet_animals(item, items_list, actions, play_again_list, enemies)
    print_pause("Congratulatons!")
    print_pause("You defeated all enemies and safely reached your home!")
    play_again(play_again_list)





start_game()
