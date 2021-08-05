#!/usr/bin/env python3
import random

print("=================================================================================")
print("You are now taking the quiz: ")
print("\"Let me guess what star wars character are you!!\"")
print("=================================================================================")

questions  = ["Q1) How old are you? ",
              "\nQ2) Choices: mint, chocolate, vanilla, strawberry, purple, superman, none \nWhat is your favorite out of these ice creams? ",
              "\nQ3)  Choices: Yes, No, Somewhat \nDo you know how to code using Java? "]

characters = ["Darth Vader", "Luke Skywalker", "Obi Wan", "R2D2", "BB-8", "Kylo Ren", "Princess Leia", "C3PO"]

#Decare my vars for the program
age = 0
flavor = 0
code = 0

def calc():
    print("Congratulations you are more like: ")
    print(random.choice(characters))

def q3():
    code = input(questions[2])
    code = code.lower()
    if code == "yes":
        del characters[0]
        calc()
    elif code == "no":
        del characters[2]
        calc()
    elif code == "somewhat":
        del characters [0]
        del characters [3]
        calc()
    else:
        print("Error type a correct flavor please!!")
        q3()
        
def q2():
    flavor = input(questions[1])
    flavor = flavor.lower()
    if flavor == "mint":
        del characters[0]
        q3()
    elif flavor == "chocolate":
        del characters[1]
        q3()
    elif flavor == "vanilla":
        del characters[2]
        q3()
    elif flavor == "strawberry":
        del characters[3]
        q3()
    elif flavor == "purple":
        del characters[4]
        q3()
    elif flavor == "superman":
        del characters[5]
        q3(age, flavor)
    elif flavor == "none":
        del characters[6]
        q3()
    else:
        print("Error type a correct flavor please!!")
        q2()


#Depends on your age it would remove a character from the list
def q1():
    try:
        age = input(questions[0])
        #Make it so it expects an int, fail it runs the program again
        isinstance(int(age),int)
        #If the above is truthy then convert
        age = int(age)
        if age <= 20:
            characters.remove("C3PO")
            q2()
        elif age <= 22:
            characters.remove("Princess Leia")
            q2()
        elif age <= 24:
            characters.remove("Kylo Ren")
            q2()
        elif age <= 26:
            characters.remove("BB-8")
            q2()
        elif age <= 28:
            characters.remove("R2D2")
            q2()
        elif age <= 30:
            characters.remove("Obi Wan")
            q2()
        elif age <= 32:
            characters.remove("Luke Skywalker")
            q2()
        elif age <= 34:
            characters.remove("Darth Vader") 
            q2()
    except ValueError:
        print("Error invlaid age try again!")
        q1()
        
#Entry point     
q1()
