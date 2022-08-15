import time
import sys
"""
Filename:generalquiz.py
Author: Raj Rautela
Date: 28/06/2022
Description: I will be doing a general quiz, there will be questions 10 questions printed and the user will have to answer with in 3 options they get to pick and at the end they will be asked if they would like to do a second general quiz or not.
"""
#The list which has questions
QUESTIONS = [
    "Q_1) what is the capital city of new zealand?",
    "Q_2) who was the prime minster before jacinda arden?",
    "Q_3) what's the tiniest country?",
    "Q_4) what's the hardest sport in the world?",
    "Q_5) what's tony starks dad's name?",
    "Q_6) who was the richest person to ever live?",
    "Q_7) what's the most visited country by people?",
    "Q_8) which is the highest grossing harry potter film?",
    "Q_9) what's the richest company in the world",
    "Q_10) how far is the sun from earth?"
]

ANSWERS = [
    "1.auckland 2.christchurch or 3.wellington",
    "1.john key 2.winston peters or 3.bill english",
    "1.vatican city 2.moncao or 3.san marino",
    "1.water polo 2.boxing or 3.basketball",
    "1.howark stark 2.joseph stark or 3.tonnie stark",
    "1.andrew carnegie 2.augustus caesar or 3.mansa musa",
    "1.france 2.china 3.italy",
    "1.harry Potter and the half-blood prince 2.harry potter and the deathly hallows part 2 or 3.harry Potter and the philosopher's stone",
    "1.tesla 2.saudi aramco or 3.microsoft",
    "1. 151.81 million km 2. 742.1 million km 3. 384,400 km"
]

# A General Quiz
print("▀▄▀▄▀▄~𝑔𝑒𝓃𝑒𝓇𝒶𝓁 𝓆𝓊𝒾𝓏~▀▄▀▄▀▄ ")
# Ask the username
user_name = input("Please enter your name: ").strip()
txt = "hello {} welcome to the general quiz"
print(txt.format(user_name, ))
print("    ")
print("    ")
time.sleep(2)
print(
    "Welcome to the General Quiz, once again we will be testing your knowledge"
)
time.sleep(0.5)
print("You will be given 10 question, make sure you take your time to answer!")
print("   ")

# Ask the user if there ready or not
ready_selection = "no"
while ready_selection != "yes":
    person = input('are you ready yes or no?: ').lower().strip()
    if person == 'yes':
        ready_selection = "yes"
    elif person == 'no': 
        person_2 = input("are you sure: ").lower().strip()
        if person_2 == 'yes':
            print('Good bye!')
            sys.exit()
    else:
        continue
print("   ")
time.sleep(1)
#score point everytime they get a question right
score = 0
#options to pick with in each question
print(QUESTIONS[0])
Q_1 = input(ANSWERS[0] +
            "\nPlease type in a number either 1 , 2 or 3 to pick an a option "
            ).strip()
print("   ")
while not (Q_1 == "1" or Q_1 == "2" or Q_1 == "3"):
    Q_1 = input("not a valid answer").strip()
if Q_1 == ("3"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 3")
print("     ")

print(QUESTIONS[1])
Q_2 = input(
    ANSWERS[1] +
    "Please type in a number either 1 , 2 or 3 to pick an a option ").strip()
print("   ")
while not (Q_2 == "1" or Q_2 == "2" or Q_2 == "3"):
    Q_2 = input("not a valid answer").strip()
if Q_2 == ("2"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 2")
print("     ")

print(QUESTIONS[2])
Q_3 = input(
    ANSWERS[2] +
    "Please type in a number either 1 , 2 or 3 to pick an a option ").strip()
print("   ")
while not (Q_3 == "1" or Q_3 == "2" or Q_3 == "3"):
    Q_3 = input("not a valid answer").strip()
if Q_3 == ("1"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 1")
print("     ")

print(QUESTIONS[3])
Q_4 = input(
    ANSWERS[3] +
    "Please type in a number either 1 , 2 or 3 to pick an a option ").strip()
print("   ")
while not (Q_4 == "1" or Q_4 == "2" or Q_4 == "3"):
    Q_4 = input("not a valid answer").strip()
if Q_4 == ("2"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 2")
print("     ")

print(QUESTIONS[4])
Q_5 = input(
    ANSWERS[4] +
    "Please type in a number either 1 , 2 or 3 to pick an a option ").strip()
print("   ")
while not (Q_5 == "1" or Q_5 == "2" or Q_5 == "3"):
    Q_5 = input("not a valid answer").strip()
if Q_5 == ("1"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 1")
print("     ")

print(QUESTIONS[5])
Q_6 = input(
    ANSWERS[5] +
    "Please type in a number either 1 , 2 or 3 to pick an a option ").strip()
print("   ")
while not (Q_6 == "1" or Q_6 == "2" or Q_6 == "3"):
    Q_6 = input("not a valid answer").strip()
if Q_6 == ("3"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 3")
print("     ")

print(QUESTIONS[6])
Q_7 = input(
    ANSWERS[6] +
    "Please type in a number either 1 , 2 or 3 to pick an a option ").strip()
print("   ")
while not (Q_7 == "1" or Q_7 == "2" or Q_7 == "3"):
    Q_7 = input("not a valid answer").strip()
if Q_7 == ("1"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 1")
print("     ")

print(QUESTIONS[7])
Q_1 = input(ANSWERS[7] +
            "\nPlease type in a number either 1 , 2 or 3 to pick an a option "
            ).strip()
print("   ")
while not (Q_1 == "1" or Q_1 == "2" or Q_1 == "3"):
    Q_1 = input("not a valid answer").strip()
if Q_1 == ("2"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 2")
print("     ")

print(QUESTIONS[8])
Q_1 = input(ANSWERS[8] +
            "\nPlease type in a number either 1 , 2 or 3 to pick an a option "
            ).strip()
print("   ")
while not (Q_1 == "1" or Q_1 == "2" or Q_1 == "3"):
    Q_1 = input("not a valid answer").strip()
if Q_1 == ("2"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 2")
print("     ")

print(QUESTIONS[9])
Q_1 = input(ANSWERS[9] +
            "\nPlease type in a number either 1 , 2 or 3 to pick an a option "
            ).strip()
print("   ")
while not (Q_1 == "1" or Q_1 == "2" or Q_1 == "3"):
    Q_1 = input("not a valid answer").strip()
if Q_1 == ("1"):
    print("that's right great work!")
    score = score + 1
else:
    print("Sorry that's inncorrect the answer was 1")
print("     ")

print("Your total score for the quiz is: " + str(score))
