import random

MAXDEPTH = 3
MAXCHILD = 3
SAMPLENUM = 10000
MAXATTR = 4 
PERCENT = 25
MAXDATA = 10

# generate rnd data for xml values
def RandomData(maxInt):
    n = random.randint(1,maxInt)
    if n > maxInt-2:
        return str (random.randint(0,2001))
    elif n == maxInt-2:
        return random.choice(open("firstnames.txt","r").readline().split()) + ' ' + random.choice(open("surnames.txt","r").readline().split())
    else:
        StringVal = ""
        for x in range(n):
            if(x > 0):
                StringVal = StringVal + ' '
            StringVal = StringVal + random.choice(open("words.txt","r").readline().split())
        return StringVal

# generates attributes for xml tags
def AttributeGen():
    yn = random.randint(0,100)
    StringVal = ""
    if yn < PERCENT:
        n = random.randint(0,MAXATTR)
        mylist = list()
        x = 0
        while x < n:
            newrand = random.choice(open("words.txt","r").readline().split())
            flag = 0
            for i in range(0,len(mylist)):
                if newrand == mylist[i]:
                    flag = 1
            if flag == 0:
                mylist.append(newrand)
                StringVal = StringVal + ' ' + newrand + "=\"" + RandomData(MAXDATA) + "\""
                x = x + 1
        # for x in range(n):
            # newrand = random.choice(open("words.txt","r").readline().split())
            # StringVal = StringVal + ' ' + newrand + "=\"" + RandomData(MAXDATA) + "\""
    return StringVal

# generate and print xml tree
def xml_tag(depth, f):
    name = random.choice(open("words.txt","r").readline().split())
    child = random.randint(0, MAXCHILD)
    f.write('<' + name + AttributeGen() + '>')
    if (depth == MAXDEPTH or child == 0):
        f.write(RandomData(10))
    else:
        for x in range(child):
            xml_tag(depth+1, f)
    if depth == 0:
        f.write(' ' + '</'+name+'>')
    else:
        f.write(' ' + '</'+name+'>')

# print xml file
def XmlGen():
    f = open("XmlSource.xml", "w")
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?> ")
    xml_tag(0, f)
    f.close()

XmlGen()