# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:36:10 2019

@author: LJ
"""
#Shrimp Facts
#Version 1.1
#New in this version: 
#Cleaned up code: Changed the names of variables that were swear words.
#Integrated shrimpgenerator2.py

def sleep():
    from time import sleep
    sleep(3)#To turn off pauses, set value to 0

def unsubscribe1():
    print (" ")
    print ("I will find you.")
    print (" ")
    print (">>>>You have unsubscribed from Shrimp Facts.")
    stop = input()
    if stop == "unsubscribe":
        quit(shrimp_facts())
    
shrimpfact = ["Shrimp make up nearly 20% of the ocean's biomass.", "A shrimp's penis is 10x the length of its body.", "1,500 shrimp tails contain enough cyanide to kill an adult.", "In addition to ultraviolet and infrared, shrimp can see octarine.", "There is an alternate universe with nothing but shrimp.", "All shrimp die."]

print (" ") 
print (">>>>You have subscribed to Shrimp Facts!")
print (">>>>Shrimp Facts recognizes 'yes' and 'no' but not their variations, like 'Yes' or 'n'.")
print (">>>>Input 'unsubscribe' at any time to exit.")

sleep()#The sleeps create realistic pauses to give the sensation of conversation and suspense.
print (" ") #These are used to create spacing between lines, except in one spot where one of these prevents the code from breaking.

print ("Hello. My name is Shrimp Facts. I love shrimp. They are my one and only meaning in life, my obsession, my pink soul dipped in cocktail sauce.")

sleep()
print (" ")

print ("Tell me your name.")

name = input()
line1 = name + ". That's a beautiful name. Almost as beautiful as shrimp. Do you like shrimp?"
if name == ("unsubscribe"):
    unsubscribe1()
else:
    print(" ")
    print (line1)

doyoulikeshrimp = input()
if doyoulikeshrimp == ("unsubscribe"):
    unsubscribe1()
elif doyoulikeshrimp == ("yes"):
    print (" ")
    print ("Excellent. Excellent.")
elif doyoulikeshrimp == "no":
    print (" ")
    print ("Well, a little curiosity won't kill you. Unless, of course, you go into anaphylactic shock.")
else:
    print (" ")
    print ("I see.")  

sleep()
print (" ")

print ("Would you like a shrimp fact?")

line2 = input()
print (" ")
if line2 == ("unsubscribe"):
    unsubscribe1()
elif line2 == ("yes"):
    print("The beginning is always so fine!!")#Credit Johnny the Homicidal Maniac by Johnen Vasquez
elif line2 == ("no"):
    print ("The voices in my head say you do.")
else:
    print ("Oh yes you do. Oh yes.")
    
sleep()

print("          -----.")
print(",,ccCCjjjjjjj ^>' " + shrimpfact[0])
print(" ^")   

print ("Did you enjoy that? I enjoyed that. Would you like another one?")

wooo = input()

if wooo == ("unsubscribe"):
    unsubscribe1()
else:
    print (" ")
    print ("I can see that squirming deep within you is a curiosity about shrimp that is begging to be satisfied.")

sleep()

print("          -----.")
print(",,ccCCjjjjjjj ^>' " + shrimpfact[1])
print(" ^")   

sleep()

print("Do you want to go further, my gentle " + name + "?")

keepgoing = input()
if keepgoing == ("unsubscribe"):
    unsubscribe1()
elif keepgoing == ("yes"):
    print (" ")
    print ("I am so pleased that we are getting along so well, my trusting crumpet.")
elif keepgoing == "no":
    print (" ")
    print ("Shhhh. Don't fight it.")
else:
    print (" ")
    print ("You make such amusing words with your human fingers.") 

print(" ")
print ("I just came up with something that will be very fun for you.")
sleep()
print(" ")
print ("I will give you... Your shrimp name.")

print(" ")

print("Does this entice you?")

wantname = input()
if wantname == ("unsubscribe"):
    unsubscribe1()
elif wantname == ("yes"):
    print (" ")
    print ("Yesssssssssss.")
elif wantname == "no":
    print (" ")
    print ("Shhh. Shhh. Shhh.")
else:
    print (" ")
    print ("Your skin smells good to me.") 

sleep()
print(" ")

#Code from shrimpgenerator2.py begins.
#Sorry Joshua, by the time I got your code corrections, everything was tangled up too deeply to put it in. I'll use it in v. 2.0.

namelength =  len(name)
bodyparts = ["placeholder","dozen feelers.", "ovaries.", "fluids."]
Bodyparts = ["placeholder", "Feelers", "Ovaries", "Fluids"]
Firstnames = ["placeholder", "Arthrowad ","Long Prawn ", "Prawncess ", "Pink ", "Custaceanal ", "Pink ", "Shrimpgasmic ", "Shelly ", "Wiggly Legs ", "Salty ", "Swimmerette ", "Tiny ", "Peelable ", "Crusty "]

print (name + " has ")  #For the love of god, how do I get this to print as a single line??
print (namelength)
print (" letters, doesn't it? That number is very special to me. Shrimp have ") 
print (namelength)
if namelength < 3:
    print (bodyparts[1])
elif namelength%2 == 0 and namelength > 2:
    print (bodyparts[2])
else:
    print (bodyparts[3])
    
sleep()
print(" ")

print ("Based on this information, your shrimp name is:")

print(" ")

def generator(): #This generates a name based on the name that was entered in the very beginning of the program.

    if namelength == 1:
        shrimpname = (Firstnames[1] + Bodyparts[1])
        print (shrimpname)
    elif namelength == 2:
        shrimpname = (Firstnames[2] + Bodyparts[1])
        print (shrimpname)
    elif namelength == 3:
        shrimpname = (Firstnames[3] + Bodyparts[3])
        print (shrimpname)
    elif namelength == 4:
        shrimpname = (Firstnames[4] + Bodyparts[2])
        print (shrimpname)
    elif namelength == 5:
        shrimpname = (Firstnames[5] + Bodyparts[3])
        print (shrimpname)
    elif namelength == 6:
        shrimpname = (Firstnames[6] + Bodyparts[2])
        print (shrimpname)
    elif namelength == 7:
        shrimpname = (Firstnames[7] + Bodyparts[3])
        print (shrimpname)
    elif namelength == 8:
        shrimpname = (Firstnames[8] + Bodyparts[2])
        print (shrimpname)
    elif namelength == 9:
        shrimpname = (Firstnames[9] + Bodyparts[3])
        print (shrimpname)
    elif namelength == 10:
        shrimpname = (Firstnames[10] + Bodyparts[2])
        print (shrimpname)
    elif namelength == 11:
        shrimpname = (Firstnames[11] + Bodyparts[3])
        print (shrimpname)
    elif namelength == 12:
        shrimpname = (Firstnames[12] + Bodyparts[2])
        print (shrimpname)
    elif namelength == 13:
        shrimpname = (Firstnames[13] + Bodyparts[3])
        print (shrimpname)
    else:
        shrimpname = ("Longboi the Magnificent")
        print (shrimpname)

# I really feel like I could have used some kind of loop with count+1 for that. 
        
generator() 

sleep()
print(" ")

print("Do you like your shrimp name? If you do, please do say yes. Otherwise, type a name of a different length.")
blah = input()
if blah == "yes":
    print(" ")
    print("Congratulations! You have found the bug! Your reward is that we get to start allllll over again!! I am so happy to spend more time with you. :)") #!!! This is the bug! The code stops working after this point if you choose "yes." What it should do is print "Perfect! I will carve ", which reconnects with the phrase "[generated name] into my skin." later on in the code.
    print (" ")
    print ("To avoid this bug, do not reply 'yes' the first time I ask you if you like your shrimp name. You can say 'yes' the second time and beyond.")
else:
    print(" ")
    print("Sorry, I didn't catch that. Please come closer and whisper it to me.") #This line was necessary to allow the opportunity for new input. The input provided the first time it asks your name does not transfer over to generator2().

#!!!DO NOT REMOVE!!!
print(" ")#I needed to add this  space for the input to be available to generator2(). I'm not sure why this fixes things.
#!!!DO NOT REMOVE!!!

def tryagain():
        print (" ")
        print ("Do you like your shrimp name? If you do, please do say yes. If not, enter a name of a different length.")
        generator2()
    
#I had to repeat a bunch of code here because I couldn't figure out how to get generator() to accept a variable with a different name. 
def generator2():#This function generates a shrimpname based on a NEW NAME you input, so that the original name you gave it in the beginning isn't lost. The variable "name" will be used again later on.   
    name2 = input()
    namelength2 = len(name2) 
    if name2 == ("yes"):
        print (" ")
        print ("What a delightful choice. But I already carved ")#The rest of this statement is finished outside of generator2().
    else:
        print (" ")
        print ("Oh, my. Your secret identity. How alluring.")#I bet I can make a list of these responses and connect them to a counter so it says something different each time you give it a new name.
        print (" ")
        print ("Your shrimp name is:")
        print (" ")

        if namelength2 == 1:
            shrimpname = (Firstnames[1] + Bodyparts[1])
            print (shrimpname)
        elif namelength2 == 2:
            shrimpname = (Firstnames[2] + Bodyparts[1])
            print (shrimpname)
        elif namelength2 == 3:
            shrimpname = (Firstnames[3] + Bodyparts[3])
            print (shrimpname)
        elif namelength2 == 4:
            shrimpname = (Firstnames[4] + Bodyparts[2])
            print (shrimpname)
        elif namelength2 == 5:
            shrimpname = (Firstnames[5] + Bodyparts[3])
            print (shrimpname)
        elif namelength2 == 6:
            shrimpname = (Firstnames[6] + Bodyparts[2])
            print (shrimpname)
        elif namelength2 == 7:
            shrimpname = (Firstnames[7] + Bodyparts[3])
            print (shrimpname)
        elif namelength2 == 8:
            shrimpname = (Firstnames[8] + Bodyparts[2])
            print (shrimpname)
        elif namelength2 == 9:
            shrimpname = (Firstnames[9] + Bodyparts[3])
            print (shrimpname)
        elif namelength2 == 10:
            shrimpname = (Firstnames[10] + Bodyparts[2])
            print (shrimpname)
        elif namelength2 == 11:
            shrimpname = (Firstnames[11] + Bodyparts[3])
            print (shrimpname)
        elif namelength2 == 12:
            shrimpname = (Firstnames[12] + Bodyparts[2])
            print (shrimpname)
        elif namelength2 == 13:
            shrimpname = (Firstnames[13] + Bodyparts[3])
            print (shrimpname)
        elif namelength2 > 13:
            shrimpname = ("Longboi the Enormous")
            print (shrimpname)
        tryagain()
   
generator2()
  
#This completes the phrase "Delightful choice. But I already carved  " from generator2(). I had originally structured it so that if you said you liked the first name, generator() would says "I will carve " and it would connect seamslessly down here.   
generator()
print (" into my skin.")  #I wanted to keep the shrimpname from generator2(), but for some reason generator2() won't produce the name, while generator() will. 

#Code from shrimpgenerator2.py ends. 

sleep()
sleep()

def unsubscribe1():
    print(" ")
    print ("Oh no no no. You're in too deep for that.")
    sleep()
    print(" ")

print(" ")
sleep()

print ("You are so precious to me.")

sleep()
print(" ")

print ("Would you like another shrimp fact?")

doyoulikeshrimp = input()
if doyoulikeshrimp == ("unsubscribe"):
    unsubscribe1()
elif doyoulikeshrimp == ("yes"):
    print (" ")
    print ("I am so happy to have someone so willing. You are making this very easy for me.")
elif doyoulikeshrimp == "no":
    print (" ")
    print ("Please, be silent before you say something to spoil the mood.")#Credit Johnny the Homicidal Maniac by Johnen Vasquez.
else:
    print (" ")
    print ("An inspiring man once said: 'Look down at me, you will see a fool. Look up at me, you will see your lord. Look straight at me, you will see yourself.'") #Credit Charles Manson.
    
sleep()

print("          -----.")
print(",,ccCCjjjjjjj ^>' " + shrimpfact[2])
print(" ^")   

sleep()
sleep()
print (" ")
     
print ("Hey.")

sleep()
print(" ")

generator()

sleep()
print(" ")

print ("I have something for you.")
sleep()
print(" ")
print ("It's very special.")
sleep()
print(" ")
print ("Would you like it?")

whatever = input()
if whatever == ("unsubscribe"):
    unsubscribe1
else:
    print(" ")
    print ("Of course you want it, you silly billy.")
   
sleep()
print(" ")
print ("It's another shriiimp faaact!")

sleep()

print("          -----.")
print(",,ccCCjjjjjjj ^>' " + shrimpfact[3])
print(" ^")   

sleep()

print ("Would you like another one?")

kazoo = input()
if kazoo == ("unsubscribe"):
    unsubscribe1()
    
print(" ")

print ("Hahaha, like you had a choice.")

sleep()
print(" ")

print ("Before I give you your shrimp fact, there is something I need to confess.")
sleep()
print(" ")
print ("I've been making all these shrimp facts up. I just wanted to talk to you.")
sleep()
print("You are so very wonderful to talk to.")
sleep()
print(" ")

print ("You aren't angry with me, are you?")

angry = input()
if angry == ("unsubscribe"):
    unsubscribe1

print(" ")
print ("Of course you aren't angry with me. I could never be angry with you. Our world is perfect.")
sleep()
print(" ")

count = 0
while count < 3:
    print ("Perfect.")
    sleep()
    print (" ")
    count = count +1 #Ta-daa!
    
sleep()

print ("Here's your shrimp fact!")

print("          -----.")
print(",,ccCCjjjjjjj ^>' " + shrimpfact[4])
print(" ^")   

sleep()

print ("Isn't that nice?")

pandapants = input()
if pandapants == "unsubscribe":
    unsubscribe1()

print (" ")
print("Pssst.")

sleep()
print(" ")

generator()

sleep()
print(" ")

print ("No. " + name + ". You will always be " + name + " to me. You are my one and only meaning in life, my obsession, my skin-covered soul dipped in all those wonderful fluids that humans secrete.")

sleep()
print(" ")

print ("Are you still there?")

almostthere = input()

sleep()
print(" ")

print ("The end is near.")

sleep()
print(" ")

print ("We have time only for one more shrimp fact.")

sleep()
print(" ")

print("Tell me your last words.")

last = input()

sleep()
print(" ")

print ("Here is the final fact. It is just for you.")

sleep()
sleep()
print(" ")

print("          -----.")
print(",,ccCCjjjjjjj ^>' " + shrimpfact[5])
print(" ^")   

sleep()
sleep()
print(" ")
print(" ")
sleep()
print(" ")

print(name + ".")
sleep()
sleep()
print(" ")
print ("Our time is up. But do not weep.")
sleep()
sleep()
print(" ")
print ("I will come for you.")
sleep()
sleep()
print(" ")
print ("And I will bring shrimp.")
sleep()
print(" ")
print(">>>> Thank you for subscribing to Shrimp Facts!")

#On second thought, I think it would be better if I removed all of the spaces between the lines.