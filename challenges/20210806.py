#!/usr/bin/env python3
import csv

words = ["FIZZ", "BUZZ", "FIZZBUZZ"]

countFIZZ = 0
countBUZZ = 0
countFIZZBUZZ = 0

with open("../numfile.txt", "r") as csvfile:
    for num in csv.reader(csvfile):
        number = int(num[0])
        if number % 15 == 0:
            print(words[2])
            countFIZZBUZZ = countFIZZBUZZ + 1
        elif number % 5 == 0:
            print(words[1])
            countBUZZ = countBUZZ + 1
        elif number % 3 == 0:
            print(words[0])
            countFIZZ = countFIZZ + 1
        else:
            print(number)
print("FIZZ: ", countFIZZ, "BUZZ: ", countBUZZ, "FIZZBUZZ: ", countFIZZBUZZ)
