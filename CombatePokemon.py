import os
import random
from optparse import OptionParser

import readchar


MAP= """\
  ######################################
   ################    #################
#   ###########         ################
          ###             ##############
                               ######   
                                        
####                ##       ###########
##           #                     #####
#                         ##            
##                       ####          #
######                    ##            
###                            #####    
#            ###           #            
              #           ##        ####
#####       #####                 ######
######     #######            ##########
#######  ###########        ############
#####################      #############
########################################\
"""

map= [list(row) for row in MAP.split("\n")]
MAP_WIDTH = len(map[0])
MAP_HEIGHT = len(map)

POS_X = 0
POS_Y = 1
NUM_OF_TRAINERS = 5

PIKACHU_HP = 100
OPPONENT_HP = 100

num_of_opponents = []
trainers = []
my_position = [0,0]
win = False
#Trainers position generator
while len(trainers) < NUM_OF_TRAINERS:
    new_position = [(random.randint(0, MAP_WIDTH - 1)), (random.randint(0, MAP_HEIGHT - 1))]
    if new_position not in trainers and new_position != my_position and map[new_position[POS_Y]][
        new_position[POS_X]] != "#":
        trainers.append(new_position)


#Main Loop
while not win:
    print("+" + "-" * MAP_WIDTH * 2 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            tail_in_position = None

            for trainer in trainers:
                if trainer[POS_X] == cordinate_x and trainer[POS_Y] == cordinate_y:
                    if trainer[POS_X] == my_position[POS_X] and trainer[POS_Y] == my_position[POS_Y]:
                        num_of_opponents.append(trainer)
                    else:
                        char_to_draw = " *"

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = " @"


            if map[cordinate_y][cordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 2 + "+")

    pikachu_hp = PIKACHU_HP
    opponent_hp = OPPONENT_HP

    if len(num_of_opponents) == 1:
        os.system("cls")
        print("Entrenador cazabichos te deafía")
        print("Entrenador cazabichos saca a Beedrill")
        print("Sacas a tu pokémon: Pikachu te elijo a tí")
        print("Lanzaremos una moneda para ver quien ataca primero.(Cara[0]: Ataca tu oponente, Cruz[1]: Ataca Pikachu)")
        cara_cruz = random.randint(0, 1)
        if cara_cruz == 0:
            print("Empieza tu oponente!\n")
            while pikachu_hp > 0 and opponent_hp > 0:

                input("Turno de Beedrill!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Beedrill usa Picadura!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Beedrill usa Pin Misil!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Beedrill usa Picotazo Veneno!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Beedrill usa Agilidad!")

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!")
                    print("Beedrill gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Beedrill  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[0])
                    my_position = [0,0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Beedrill  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")


                if opponent_hp <= 0:
                    print("Beedrill queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Beedrill  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[0])
                    num_of_opponents.append([0,0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Beedrill  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")
        elif cara_cruz == 1:
            print("Empiezas tú!\n")
            while pikachu_hp > 0 and opponent_hp > 0:
                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")

                if opponent_hp <= 0:
                    print("Beedrill queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Beedrill  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[0])
                    num_of_opponents.append([0, 0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Beedrill  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))

                print("\n")
                input("Turno de Beedrill!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Beedrill usa Picadura!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Beedrill usa Pin Misil!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Beedrill usa Picotazo Veneno!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Beedrill usa Agilidad!")

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!\nBeedrill gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Beedrill  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[0])
                    my_position = [0, 0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Beedrill  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


    if len(num_of_opponents) == 3:
        os.system("cls")
        print("Entrenador montañero te deafía")
        print("Entrenador montañero saca a Golem")
        print("Sacas a tu pokémon: Pikachu te elijo a tí")
        print("Lanzaremos una moneda para ver quien ataca primero.(Cara[0]: Ataca tu oponente, Cruz[1]: Ataca Pikachu)")
        cara_cruz = random.randint(0, 1)
        if cara_cruz == 0:
            print("Empieza tu oponente!\n")
            while pikachu_hp > 0 and opponent_hp > 0:

                input("Turno de Golem!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Golem usa Placaje!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Golem usa Lanzarocas!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Golem usa Pedrada!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Golem usa Gruñido!")

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!")
                    print("Golem gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Golem  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[2])
                    my_position = [0,0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Golem  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")


                if opponent_hp <= 0:
                    print("Golem queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Golem  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[2])
                    num_of_opponents.append([0,0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Golem  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")
        elif cara_cruz == 1:
            print("Empiezas tú!\n")
            while pikachu_hp > 0 and opponent_hp > 0:
                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")

                if opponent_hp <= 0:
                    print("Golem queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Golem  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[2])
                    num_of_opponents.append([0, 0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Golem  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))

                print("\n")
                input("Turno de Golem!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Golem usa Placaje!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Golem usa Lanzarocas!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Golem usa Pedrada!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Golem usa Gruñido!")

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!\nGolem gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Golem  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[2])
                    my_position = [0, 0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Golem  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


    if len(num_of_opponents) == 5:
        os.system("cls")
        print("Recluta del Team Rocket te deafía")
        print("Recluta del Team Rocket saca a Golem")
        print("Sacas a tu pokémon: Pikachu te elijo a tí")
        print("Lanzaremos una moneda para ver quien ataca primero.(Cara[0]: Ataca tu oponente, Cruz[1]: Ataca Pikachu)")
        cara_cruz = random.randint(0, 1)
        if cara_cruz == 0:
            print("Empieza tu oponente!\n")
            while pikachu_hp > 0 and opponent_hp > 0:
                input("Turno de Arbok!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Arbok usa Triturar!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Arbok usa Bomba Lodo!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Arbok usa Bomba Lodo!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Arbok usa Malicioso!")

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!")
                    print("Arbok gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Arbok  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[4])
                    my_position = [0,0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Arbok  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")


                if opponent_hp <= 0:
                    print("Arbok queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Arbok  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[4])
                    num_of_opponents.append([0,0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Arbok  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")
        elif cara_cruz == 1:
            print("Empiezas tú!\n")
            while pikachu_hp > 0 and opponent_hp > 0:
                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")

                if opponent_hp <= 0:
                    print("Arbok queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Arbok  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[4])
                    num_of_opponents.append([0, 0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Arbok  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))

                print("\n")
                input("Turno de Arbok!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Arbok usa Triturar!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Arbok usa Bomba Lodo!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Arbok usa Bomba Lodo!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Arbok usa Malicioso!")

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!\nArbok gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Arbok  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[4])
                    my_position = [0, 0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Arbok  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


    if len(num_of_opponents) == 7:
        os.system("cls")
        print("Jessie y James te deafían")
        print("Jessie y James sacan Meowth")
        print("Sacas a tu pokémon: Pikachu te elijo a tí")
        print("Lanzaremos una moneda para ver quien ataca primero.(Cara[0]: Ataca tu oponente, Cruz[1]: Ataca Pikachu)")
        cara_cruz = random.randint(0, 1)
        if cara_cruz == 0:
            print("Empieza tu oponente!\n")
            while pikachu_hp > 0 and opponent_hp > 0:
                input("Turno de Meowth!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Meowth usa Mordisco!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Meowth usa Cuchillada!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Meowth usa Carantoña!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Meowth usa Gruñido!")

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!")
                    print("Meowth gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Meowth  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[6])
                    my_position = [0,0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Meowth  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")


                if opponent_hp <= 0:
                    print("Meowth queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Meowth  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[6])
                    num_of_opponents.append([0,0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Meowth  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")
        elif cara_cruz == 1:
            print("Empiezas tú!\n")
            while pikachu_hp > 0 and opponent_hp > 0:
                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")

                if opponent_hp <= 0:
                    print("Meowth queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Meowth  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[6])
                    num_of_opponents.append([0, 0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Meowth  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))

                print("\n")
                input("Turno de Meowth!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Meowth usa Mordisco!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Meowth usa Cuchillada!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Meowth usa Carantoña!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Meowth usa Gruñido!")

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!\nMeowth gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Meowth  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[6])
                    my_position = [0, 0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Meowth  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


    if len(num_of_opponents) == 9:

        os.system("cls")
        print("Giovani el líder del Team Rocket te desafía.")
        print("Giovani saca a Mewtwo")
        print("Sacas a tu pokémon: Pikachu te elijo a tí")
        print("Lanzaremos una moneda para ver quien ataca primero.(Cara[0]: Ataca tu oponente, Cruz[1]: Ataca Pikachu)")
        cara_cruz = random.randint(0, 1)
        if cara_cruz == 0:
            print("Empieza tu oponente!\n")
            while pikachu_hp > 0 and opponent_hp > 0:
                input("Turno de Mewtwo!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Mewtwo usa Confusión!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Mewtwo usa Poder Pasado!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Mewtwo usa Psíquico!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Mewtwo usa Recuperación!")
                    opponent_hp += 10

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!")
                    print("Mewtwo gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Mewtwo  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[8])
                    my_position = [0,0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Mewtwo  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")


                if opponent_hp <= 0:
                    print("Mewtwo queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Mewtwo  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[8])
                    num_of_opponents.append([0,0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Mewtwo  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")
        elif cara_cruz == 1:
            print("Empiezas tú!\n")
            while pikachu_hp > 0 and opponent_hp > 0:
                input("Turno de Pikachu!")
                pikachu_attack = None
                while pikachu_attack not in ["1", "2", "3", "4"]:
                    pikachu_attack = input(
                        "Que ataque quieres usar?\n[ 1-Placaje || 2-Trueno || 3-Rayo || 4-Gruñido ]")
                    if pikachu_attack == "1":
                        print("Pikachu usa Placaje!")
                        opponent_hp -= 5
                    elif pikachu_attack == "2":
                        print("Pikachu usa Trueno!")
                        opponent_hp -= 20
                    elif pikachu_attack == "3":
                        print("Pikachu usa Rayo!")
                        opponent_hp -= 30
                    elif pikachu_attack == "4":
                        print("Pikachu usa Gruñido!")

                if opponent_hp <= 0:
                    print("Mewtwo queda fuera de combate!\nPikachu gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Mewtwo  0hp [{}{}]".format("#" * opponent_live_bar,
                                                   " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  {}hp [{}{}]".format(pikachu_hp, "#" * pikachu_live_bar,
                                                        " " * (20 - pikachu_live_bar)))
                    trainers.remove(num_of_opponents[8])
                    num_of_opponents.append([0, 0])
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Mewtwo  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))

                print("\n")
                input("Turno de Mewtwo!")
                opponent_attack = random.randint(1, 4)
                if opponent_attack == 1:
                    print("Mewtwo usa Confusión!")
                    pikachu_hp -= 10
                elif opponent_attack == 2:
                    print("Mewtwo usa Poder Pasado!")
                    pikachu_hp -= 20
                elif opponent_attack == 3:
                    print("Mewtwo usa Psíquico!")
                    pikachu_hp -= 25
                elif opponent_attack == 4:
                    print("Mewtwo usa Recuperación!")
                    opponent_hp += 10

                if pikachu_hp <= 0:
                    os.system("cls")
                    print("Pikachu queda fuera de combate!\nMewtwo gana")
                    opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                    print(
                        "Mewtwo  {}hp [{}{}]".format(opponent_hp, "#" * opponent_live_bar,
                                                    " " * (20 - opponent_live_bar)))
                    pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                    print("Pikachu  0hp [{}{}]".format("#" * pikachu_live_bar,
                                                       " " * (20 - pikachu_live_bar)))
                    num_of_opponents.remove(num_of_opponents[8])
                    my_position = [0, 0]
                    break

                # Barras de vida
                opponent_live_bar = int(opponent_hp * 20 / OPPONENT_HP)
                print(
                    "Mewtwo  {}hp [{}{}] ".format(opponent_hp, "#" * opponent_live_bar,
                                                 " " * (20 - opponent_live_bar)))
                pikachu_live_bar = int(pikachu_hp * 20 / PIKACHU_HP)
                print("Pikachu  {}hp [{}{}]".format(pikachu_hp,
                                                    "#" * pikachu_live_bar,
                                                    " " * (20 - pikachu_live_bar)))
                print("\n")


    if len(num_of_opponents) == 10:
        win = True
        break

    os.system("cls")

    print("+" + "-" * MAP_WIDTH * 2 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            tail_in_position = None

            for trainer in trainers:
                if trainer[POS_X] == cordinate_x and trainer[POS_Y] == cordinate_y:
                    if trainer[POS_X] == my_position[POS_X] and trainer[POS_Y] == my_position[POS_Y]:
                        num_of_opponents.append(trainer)
                    else:
                        char_to_draw = " *"

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = " @"

            if map[cordinate_y][cordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 2 + "+")

    direction = readchar.readchar()

    new_position = None

    if direction == "w" or direction == "W":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s" or direction == "S":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a" or direction == "A":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d" or direction == "D":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q" or direction == "Q":
        win = True

    if new_position:
        if map[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")


if win:
    os.system("cls")
    print("\n" * 5)
    print("Has vencido a todos los entrenadores, tu y tu Pikachu habéis hecho un gran trabajo.\n¡¡¡Felicidades!!!")
    print("\n" * 5)