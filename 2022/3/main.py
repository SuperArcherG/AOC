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

print("A:",total)

groupedSacks = [["" for _ in range(3)] for _ in range(int(len(list)/3))]
slot = 2
ind = 0
for sack in list:
    if slot < 2:
        slot = slot + 1
    else:
        slot = 0
    ind = ind + 1
    group = round(((ind-1)/3)-1/3)
    #print("Group:",group,", Slot:", slot, "Contents:", sack)
    groupedSacks[group][slot] = sack

groupMatch = ["" for _ in range(int(len(list)/3))]
ind = 0
total = 0
for group in groupedSacks:
    match = ""
    for letterA in group[0]:
        for letterB in group[1]:
            for letterC in group[2]:
                if letterA == letterB == letterC:
                    match = letterA
    
    groupMatch[ind] = match
    ind = ind + 1

    ##Calculate the priority
    priority = ord(match) - ord('a') + 1 #calculate the initial value
    
    if priority < 0: #account for capitals
        priority = priority + 58 
        
    total += priority #add to total

    #print(match)
print("B",total)
