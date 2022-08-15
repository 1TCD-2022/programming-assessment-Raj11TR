import time
"""
Filename:generalquiz.py
Author: Raj Rautela
Date: 28/06/2022
Description: I will be doing a general quiz, there will be questions 10 questions printed and the user will have to answer with in 3 options they get to pick and at the end they will be asked if they would like to do a second general quiz or not.
"""
#The list which has questions
Q1 = ["what is the capital city of new zealand? 1.auckland 2.christchurch or 3.wellington" ]
Q2 = ["who was the prime minster before jacinda arden? 1.john key 2.bill english or 3.winston peters"]
Q3 = ["what's the tiniest country? 1.vatican city 2.moncao or 3.vatican city"] 
Q5 = [ "what's the hardest sport in the world? 1.water polo 2.boxing or 3.basketball"]
Q6 = ["what's tony starks dad's name? 1.tonnie stark 2.joseph stark or 3.howard stark"]
Q7 = ["who was the richest person to ever live? 1.andrew carnegie 2.augustus caesar or 3.mansa musa"]
Q8 = ["what's the most visited country by people? 1.france 2.china 3.italy"]
Q9 = ["which is the highest grossing harry potter film? 1.harry Potter and the half-blood prince 2.harry potter and the deathly hallows part 2 or 3.harry Potter and the philosopher's stone"] 
Q10 = ["what's the richest company in the world 1.tesla 2.microsoft " ]
#options to pick with in each question 




# A General Quiz
print("~~~~~~~~General Quiz~~~~~~~~")
#Ask the user name
user_name = input("Please enter your name ").strip()
print("         ")
print("         ")
print("Hello", user_name, "welcome to the General Quiz")
time.sleep(2)
print("Welcome to the General we will be testing your knowledge")
time.sleep(0.5)
print("You will be given 10 question, make sure you take your time to answer!")

# Ask the user if there ready or not
ready_selection = "no"
while ready_selection != "yes":
    ready_selection = input("Are you ready? yes or no : ").strip()
print("Ok, let's go")
print("GOODLUCK!")
time.sleep(1)
current = 0
Q_1 = input(Q1[current]) 
if Q_1 in ANSWERS1:
  print("that's correct")
else:
  print("sorry incorrect")
  

