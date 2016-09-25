import csv
import random

occFile = open("occupations.csv","r")
#use to deal with anything weird the user may have done (spaces, commas, etc.)
occReader = csv.DictReader(occFile)
occDict = {}

for row in occReader:
    occDict[row["Job Class"]] = (float)(row["Percentage"])

occFile.close()

def printDict():
    for row in occDict:
        print row + ":", #want to print on same line
        #diagnostics
        print occDict[row] + 0, #still same line
        print "%"

def randomPick():
    rand = random.randrange(100)
    for row in occDict:
        rand -= occDict[row]
        if rand <= 0:
            return row
    return "Something went wrong"

def getDict():
    return occDict

#diagnostics
#printDict()
print randomPick()
