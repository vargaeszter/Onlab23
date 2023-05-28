import datetime
import os

def MakeDirectory():
    time = datetime.datetime.now()

    timestamp = time.timestamp()

    dirName = str(timestamp)

    os.mkdir(dirName)

    return dirName