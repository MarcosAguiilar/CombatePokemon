import os
import random

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
                        trainers.remove(trainer)
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