#Mia Sanchez
#01-19-2024
#38 Magic 8 Ball

#Initialize

import random

magicList = ["Without a Doubt", "Yes Definitely", "Most Likely", "Signs Point to Yes", "Ask Again Later", "Concentrate and Ask Again", "Don't Count On It", "Outlook is not so good", "Very Doubtful", "My Reply is No"]

print("Welcome to Magic 8 Ball!")

#Functions

def Magic8Ball():
    x = input("Input a question you wish to answer, and remember to put a questionmark!\n")
        
    q1 = x.endswith("?")
        
    if q1 == False:
        print("ERROR Missing Questionmark")
        Magic8Ball()
    elif q1 == True:
        print (random.choice(magicList))
        q2 = input("Do you want to ask another question?\n")
        if q2.lower() == "yes" or q2.lower() == "y":
            Magic8Ball()
        elif q2.lower() == "no" or q2.lower() == "n" :
            quit()
        

        
            

#Main
                
Magic8Ball()