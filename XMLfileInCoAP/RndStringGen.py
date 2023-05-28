import random

char = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
NumChar = 52
MaxLen = 2

def NewInput():

    f = open("words.txt", "w")

    # print all single characters
    index = []
    for i in range(0,NumChar):
        f.write(char[i] + " ")

    # random char combinations len 2...12
    for i in range(1, 12):
        for j in range(500):
            word = ""
            for k in range(0,i+1):
                word += random.choice(char)
            word += " "
            f.write(word)
    f.close()
