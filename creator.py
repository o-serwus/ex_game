import random

name_1 = input("What is your name? ")
name_2 = input("What is your name? ")
name_3 = input("What is your name? ")
name_4 = input("What is your name? ")
name_5 = input("What is your name? ")

one_class = ""
one_strength = strength
one_health = health
one_magic = magic


player_class_pos = random.randint (1,3)
if (player_class_pos == 1):
    player_class = "Warrior"
elif(player_class_pos == 2):
    player_class = "Wizard"
elif(player_class_pos == 3):
    player_class = "Potato"
    
    
    
strength = random.randint(5, 10)
health = random.randint(5, 10)
magic = random.randint (5, 10)

if(player_class == "warrior"):
    strength *= 3
elif(player_class == "wizard"):
    magic *= 3
elif(player_class == "potato"):
    health *3
    
    