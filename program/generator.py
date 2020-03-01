from time import sleep
from random import *
import linecache

name = linecache.getline("help.txt", 3)
name = name.replace('\n', '')

def main_program():
    user_input = input(name + ':~$ ')
    if user_input == 'roll':
        with open("warframes.txt", "r") as file:
            data_read_1 = len(file.readlines())
            a = randint(0, int(data_read_1))
            frame = linecache.getline("warframes.txt", a)
            frame = frame.replace('\n', '')
        with open("planets.txt", "r") as file:
            data_read_2 = len(file.readlines())
            b = randint(0, int(data_read_2))
            planet = linecache.getline("planets.txt", b)
            planet = planet.replace('\n', '')
        with open("missions.txt", "r") as file:
            data_read_3 = len(file.readlines())
            c = randint(0, int(data_read_3))
            mission = linecache.getline("missions.txt", c)
            mission = mission.replace('\n', '')
        with open("builds.txt", "r") as file:
            data_read_4 = len(file.readlines())
            d = randint(0, int(data_read_4))
            build = linecache.getline("builds.txt", d)
            build = build.replace('\n', '')
        roll = ("Play a(n) " + mission + " mission on/in " + planet + " using a(n) " + build + " build on " + frame)
        print(roll)
        with open("rolls.log", "a") as file:
            data = file.write(roll + '\n')
        main_program()
    elif user_input == 'exit':
        exit_confirm()
    elif user_input == 'viewLog':
        with open("rolls.log", "r") as file:
            log_view = file.read()
            print(log_view)
        main_program()
    elif user_input == 'clrLog':
        with open("rolls.log", "w") as file:
            log_clear = file.write('\n ____LOG CLEARED____ \n')
        main_program()
    elif user_input == 'help':
        with open("help.txt", "r") as file:
            help_view = file.read()
            print(help_view)
        main_program()
    else:
        print("unknown command, type 'help' for more information")
        main_program()

def exit_confirm():
    print("Are you sure? y/n")
    user_input = input(name + ':~$ ')
    if user_input == 'yes':
        print('closing. . .')
        sleep(1)
    elif user_input == 'y':
        print('closing. . .')
        sleep(1)
    elif user_input == 'no':
        print("returning. . .")
        main_program()
    elif user_input == 'n':
        print("returning. . .")
        main_program()
    else:
        print("unknown input: " + user_input + "\nReturning. . .")
        main_program()

main_program()
