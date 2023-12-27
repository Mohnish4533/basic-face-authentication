
#functions

import time

def FluidText(line):
    global time
    for i in range (0,len(line)):
        print(line[i],end="")
        time.sleep(0.02)
        
def Design(line):
    print("=========================")
    FluidText(line)
    print("=========================")

def TimeDelay(delay):

    time.sleep(delay)

def TypeCheck(text):
    for i in range(0, int(len(text))):
        char = text[i]
        if ord(char)==48 or ord(char)==49 or ord(char)==50 or ord(char)==51 or ord(char)==52 or ord(char)==53 or ord(char)==54 or ord(char)==55 or ord(char)==56 or ord(char)==57:
            return False
    return True

def PresenceCheck(Array, text):
    try:
        index = Array.index(text)
        result = True
    except ValueError:
        index = None 
        result = False
    finally:
        return result, index

def save(object1, object2):
    file = open("Array_Storage.txt","w")
    for i in range(0, len(object1)):
        file.write(object1[i])
        file.write("\n")

    for i in range(0, len(object2)):
        file.write(str(object2[i]))
        file.write("\n")

def retrieve():

    line1 = []
    line2 = []

    file = open("Array_Storage.txt","r")
    line = file.readlines()
    for i in range (0, len(line)):
        line[i] = line[i][0:-1]

    length = len(line)
    array_length = int(length/2)

    for i in range(0, array_length):
        line1.append(line[i])
    for i in range(array_length, length):
        line2.append(line[i])

    return line1, line2

def delete_image(file):
    import os
    import os.path
    result= os.path.isfile(file)
    if result == True:
        os.remove(file)