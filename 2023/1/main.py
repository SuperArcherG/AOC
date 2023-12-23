import os
import sys
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
list = open(os.getcwd() + "/Input.txt","r").read().splitlines()
numbers = "0123456789"
#search from left to right for first number
total = 0
for i,l in enumerate(list):
    start = ""
    end = ""
    combined = ""
    for li in l:
        for n in numbers:
            if li == n and start == "":
                start = n
    l = l[::-1]
    for li in l:
        for n in numbers:
            if li == n and end == "":
                end = n
    l = l[::-1]
    combined = start + end
    print(combined)
    total += int(combined)
print("A: ",total)
print("B: TODO")
