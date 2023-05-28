import random

MAXDEPTH = 0
MAXCHILD = 3
MAXATTR = 0
PERCENT = 25
MAXDATA = 2

# generate rnd data for xml values
def RandomData(maxInt):
    n = random.randint(1,maxInt)
    if n > maxInt/2:
        return str (random.randint(0,40))
    else:
        StringVal = ""
        for x in range(random.randint(1,MAXDATA)):
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
                StringVal = StringVal + ' ' + newrand + "=\"" + RandomData(10) + "\""
                x = x + 1
    return StringVal

# generate and print xml tree
def xml_tag(depth, string):
    name = random.choice(open("htmltags.txt","r").readline().split())
    child = random.randint(0, MAXCHILD)
    string += '<' + name + AttributeGen() + '>'
    if (depth == MAXDEPTH or child == 0):
        string += RandomData(10)
    else:
        for x in range(child):
            string = xml_tag(depth+1, string)
    string += ' ' + '</'+name+'>'
    return string

# print xml file
def XmlGen():
    string = "<?xml version=\"1.0\" encoding=\"UTF-8\"?> "
    string = xml_tag(0, string)
    return string

