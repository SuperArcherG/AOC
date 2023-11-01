import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Change the current working directory to the script's directory
os.chdir(script_dir)

list = open(os.getcwd() + "/Input.txt","r").read().splitlines()

total = 0

for sack in list:
    #initial calculations
    sackSize = len(sack)
    compartmentSize = sackSize // 2
    
    #Split the sack into its two equal compartments
    compartmentA = sack[compartmentSize:]
    compartmentB = sack[:compartmentSize]
    
    #Check which item is in both compartments
    match = ""
    for letterA in compartmentA:
        for letterB in compartmentB:
            if letterA == letterB:
                match = letterA
                
    ##Calculate the priority
    priority = ord(match) - ord('a') + 1 #calculate the initial value
    
    if priority < 0: #account for capitals
        priority = priority + 58 
        
    total += priority #add to total

print("A: " + str(total))

