import os

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

spl = "\n 1   2   3   4   5   6   7   8   9 \n"
input = open(os.getcwd() + "/Input.txt","r").read()
initial = input.split(spl)[0]
list = input.split(spl)[1][1:].replace("move ","").replace(" from "," ").replace(" to "," ").splitlines()
singleLine = "]" + initial.replace("\n"," ")
while "]     " in singleLine:
    singleLine = singleLine.replace("]     ","] [0] ")
while "]    " in singleLine:
    singleLine = singleLine.replace("]    ","] [0] ")
singleLine = singleLine[2:].split(" ")
compiled = ""
for i,slot in enumerate(singleLine):
    compiled = "{}{}{}".format(compiled, str(slot), '\n' if ((i+1) % 9 == 0) else ' ')#
compiled=compiled[:-1].replace("]","").replace("[","").replace(" ","")
array = [["" for i in range(len(compiled.splitlines()))] for i in range(len(compiled.splitlines()[0]))] 
compiled=compiled.replace("\n","")
for i,char in enumerate(compiled):
    col = i%9
    ind = 7-round((i+1/9)/9-0.5)
    array[col][ind] = char
for i,l in enumerate(array):
    array[i] = [char for char in array[i] if char != "0"]

#print(array)

for i,instruction in enumerate(list):
    inst = instruction.split(" ")
    count = int(inst[0])
    fro = int(inst[1])-1
    to = int(inst[2])-1 
    for x in range(count):
        array[to].append(array[fro].pop())

print("A: ",end="")
for i,item in enumerate(array):
    print(array[i][len(array[i])-1],end="")
print()

array = []

#reset the array for part B
compiled = ""
for i,slot in enumerate(singleLine):
    compiled = "{}{}{}".format(compiled, str(slot), '\n' if ((i+1) % 9 == 0) else ' ')#
compiled=compiled[:-1].replace("]","").replace("[","").replace(" ","")
array = [["" for i in range(len(compiled.splitlines()))] for i in range(len(compiled.splitlines()[0]))] 
compiled=compiled.replace("\n","")
for i,char in enumerate(compiled):
    col = i%9
    ind = 7-round((i+1/9)/9-0.5)
    array[col][ind] = char
for i,l in enumerate(array):
    array[i] = [char for char in array[i] if char != "0"]

#print(array)

for i,instruction in enumerate(list):
    inst = instruction.split(" ")
    count = int(inst[0])
    fro = int(inst[1])-1
    to = int(inst[2])-1 
    #print(array[fro],array[to])
    #print(count,fro,to)    
    for i in array[fro][-count:]:
        array[to].append(i)
    array[fro] = array[fro][:-count]
    
print("B: ",end="")
for i,item in enumerate(array):
    print(array[i][len(array[i])-1],end="")
print()