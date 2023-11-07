import os
import sys
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
input = open(os.getcwd() + "/Input.txt","r").read()
for i,letter in enumerate(input):
    if i > 3:
        a,b,c,d=input[i],input[i-1],input[i-2],input[i-3]
        joined = a+b+c+d
        a2,b2,c2,d2 = joined.count(a),joined.count(b),joined.count(c),joined.count(d)
        if a2+b2+c2+d2 == 4:
            print("A:",i+1)
            break

for i in range(len(input)+1):
    if i > 13:
        packet = input[:14]
        total = 0
        for l in packet:
            total += packet.count(l)
        if total == 14:
            print("B:",i)
            break
        input = input[1:]