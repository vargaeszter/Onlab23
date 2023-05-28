import random
import xml_gen
import math

MaxURI = 3

def CodeGen():
    #class
    c = random.choice('0245')

    #details
    if (c == "0"): #Method Code
        d = "0"+random.choice('1234')
    elif (c == "2"): #Response Code
        d = "0"+random.choice('12345')
    elif (c == "4"):
        d = random.choice(("00","01","02","03","04","05","06","12","13","15"))
    else:
        d = "0"+random.choice('012345')
    return c+"."+d

def TokenGen(TKL):    
    token = ""
    hexa = "abcdef"
    if(TKL == 0):
        token = "0"
    while(TKL != 0):
        left = math.fmod(TKL,16)
        TKL = (TKL-left) / 16
        if(left > 9):
            nextchar = hexa[int(left) - 10]
        else:
            nextchar = str(int(left))
        token = nextchar + token
    token = "0x" + token
    return token

def URIgen():
    URI = "URI = coap://"+random.choice(open("words.txt","r").readline().split())
    URI += "."+random.choice(("com","org","net","edu","int"))
    for i in range(0,random.randint(0,MaxURI)):
        URI += "/" + random.choice(open("words.txt","r").readline().split())
    URI += "\n"
    return URI

def OptionsGen():
    options = ""
    options += "Content-Format: application/xml\n"
    set = ("ETag","Location-Path","Location-Query","Max-Age","Proxy-Uri","Proxy-Scheme","Uri-Host","Uri-Path","Uri-Port","Uri-Query","Accept","If-Match","If-None-Match","Size1")
    for i in range(14):
        n = random.randint(0,20)
        if n < 3:
            options += set[i]+": \""+random.choice(open("words.txt","r").readline().split())+"\"\n"
    return options

def CoAPgen(i, dir):

    fout = open(dir + "/coap"+str(i)+".txt", "w")
    
    for n in range(0,xml_gen.SAMPLENUM):
        xml_gen.XmlGen()

        T = random.choice(("CON","NON","ACK","RST"))

        TKL = i*xml_gen.SAMPLENUM + n

        Code = CodeGen()

        MessageID = "0x"
        for x in range(4):
            MessageID += random.choice('0123456789abcdef')

        Token = TokenGen(TKL)

        TKL = len(Token) - 2

        Options = OptionsGen()

        #print header
        fout.write("Header: " + Code + " (T=" + T + ", Code=" + Code + ", MID=" + MessageID + ")\n")

        if Code[0] == '0':
            fout.write(URIgen())

        if Token != "0x":
            #print token
            fout.write("Token: " + Token + "\n")

        fin = open("XmlSource.xml", "r")
        payload = fin.read()
        fin.close()

        payload += "\""
        if n < xml_gen.SAMPLENUM - 1:
            payload += "\n\n"

        #print payload
        fout.write(Options + "Payload: \"" + payload)
    
    fout.close()
    return


def CoAPgenTESTER(i):

    fout = open("coap"+str(i)+".txt", "w")
    
    for n in range(0,34):
        xml_gen.XmlGen()

        T = random.choice(("CON","NON","ACK","RST"))

        #TKL = random.randint(0,8)
        TKL = i*xml_gen.SAMPLENUM + n

        Code = CodeGen()

        MessageID = "0x"
        for x in range(4):
            MessageID += random.choice('0123456789abcdef')

        Token = TokenGen(TKL)

        TKL = len(Token) - 2

        Options = OptionsGen()

        #print header
        fout.write("Header: " + Code + " (T=" + T + ", Code=" + Code + ", MID=" + MessageID + ")\n")

        if Code[0] == '0':
            fout.write(URIgen())

        if Token != "0x":
            #print token
            fout.write("Token: " + Token + "\n")

        fin = open("XmlSource.xml", "r")
        payload = fin.read()
        fin.close()

        payload += "\""
        if n < xml_gen.SAMPLENUM - 1:
            payload += "\n\n"

        #print payload
        fout.write(Options + "Payload: \"" + payload)
    
    fout.close()
    return

CoAPgenTESTER(0)