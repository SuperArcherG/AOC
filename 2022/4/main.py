import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Change the current working directory to the script's directory
os.chdir(script_dir)

list = open(os.getcwd() + "/Input.txt","r").read().splitlines()
total = 0
for pair in list:
    splitPair = pair.split(",")
    la = splitPair[0]
    lb = splitPair[1]
    laa = int(la.split("-")[0])
    lab = int(la.split("-")[1])
    lba = int(lb.split("-")[0])
    lbb = int(lb.split("-")[1])
    if (laa <= lba and lab >= lbb) or (lba <= laa and lbb >= lab):
        #print(la,lb,laa,lab,lba,lbb)
        #print("Overlap",la,lb)
        total += 1

print("A:",total)

total = 0
for pair in list:
    splitPair = pair.split(",")
    la = splitPair[0]
    lb = splitPair[1]
    laa = int(la.split("-")[0])
    lab = int(la.split("-")[1])
    lba = int(lb.split("-")[0])
    lbb = int(lb.split("-")[1])
    over = False
    for i in range(laa,lab+1):
        for x in range(lba,lbb+1):
            if i == x:
                over = True
    if over:
        total += 1
              
print("B:",total)
