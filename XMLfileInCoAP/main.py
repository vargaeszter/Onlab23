
import CoAPgen
import directory
import RndStringGen

CycleNUM = 10

def main():
    dir = directory.MakeDirectory()
    for x in range(0,CycleNUM):
        RndStringGen.NewInput()
        CoAPgen.CoAPgen(x, dir)
    return
 
main()