import re

def listAttributesAndTheirNumbers(self):
    lines = splitIntoLines(self)
    myArray = []
    for line in lines:
        myArray.append(line.split(" "))
    return myArray

def splitIntoLines(self):
    return re.split(r'\n', self)

def delLastColumnAndRow(self):
    for i in range(len(self)):
        del self[i][len(self[i]) - 1]
    del self[len(self) - 1]
    return self