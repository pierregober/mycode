#!/usr/bin/env python3
import csv
import random

print("  █████▒██▓ ███▄    █ ▓█████▄    ▓██   ██▓ ▒█████   █    ██  ██▀███      ██▓███  ▒█████   ██ ▄█▀▓█████ ███▄ ▄███▓ ▒█████   ███▄    █")
print("▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌    ▒██  ██▒▒██▒  ██▒ ██  ▓██▒▓██ ▒ ██▒   ▓██░  ██▒██▒  ██▒ ██▄█▒ ▓█   ▀▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ ")
print("▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌     ▒██ ██░▒██░  ██▒▓██  ▒██░▓██ ░▄█ ▒   ▓██░ ██▓▒██░  ██▒▓███▄░ ▒███  ▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒")
print("░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌     ░ ▐██▓░▒██   ██░▓▓█  ░██░▒██▀▀█▄     ▒██▄█▓▒ ▒██   ██░▓██ █▄ ▒▓█  ▄▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒")
print("░▒█░   ░██░▒██░   ▓██░░▒████▓      ░ ██▒▓░░ ████▓▒░▒▒█████▓ ░██▓ ▒██▒   ▒██▒ ░  ░ ████▓▒░▒██▒ █▄░▒████▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░")
print(" ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒       ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░   ▒▓▒░ ░  ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ")
print(" ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒     ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░   ░▒ ░ ▒░   ░▒ ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░")
print(" ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░     ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░   ░░   ░    ░░      ░ ░ ░ ▒  ░ ░░ ░    ░  ░      ░   ░ ░ ░ ▒     ░   ░ ░ ")
print("        ░           ░    ░        ░ ░         ░ ░     ░        ░                    ░ ░  ░  ░      ░  ░      ░       ░ ░           ░ ")
print("                       ░          ░ ░                                                                                                ")

print("____ ____ _________ ____ ____ ____ ____ ____ ____ ")
print("||b |||y |||       |||p |||i |||e |||r |||r |||e ||")
print("||__|||__|||_______|||__|||__|||__|||__|||__|||__||")
print("|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|")


def catch_em_all():
    selection = input(
        "\n[Flying, Water, Electric, Grass, Rock, Poison, Fairy, Psychic, Dragon]\nWhat kind of Pokeman do you want to view?\n > ")

    with open("pokedex.txt", "r") as csvfile:
        # to make our file unqiue will be used later
        i = 0
        collector = []
        max = 720
        # iterate through my data set\
        for row in csv.reader(csvfile):

            # This is our incrementor that will be used later
            i = i + 1
            filename = f"pokeman{random.randint(0, 9999999)}.txt"
            # give me all the pokemon that are whatever the user inputed
            # python has a "in" operator for list that checks for a string within a list
            if i == max:
                with open(filename, "w") as txt:
                    print(collector, file=txt)
                    print(filename + ": Successfully written!!")
                    # Let's run it again
                    catch_em_all()
            elif selection in row:
                collector.append(row[0] + ": " + row[1])


catch_em_all()
