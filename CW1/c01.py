class SystemDecyzyjny:
    NUMBER_OF_ATTRIBUTES = 15

    def printFile(self):
        f = open(self)
        print(f.read())

    def getNumericAttributes(self):
        i = 0
        array = []
        for elem in self:
            if "n" in elem:
                array.append(i)
            i += 1
        return array

    def minAttributeValue(self, numericAttributes):
        for i in numericAttributes:
            array = []
            for x in range(len(self)):
                array.append(self[x][i])
            print("attribute", i, "min value", min(array))

    def maxAttributeValue(self, numericAttributes):
        for i in numericAttributes:
            array = []
            for x in range(len(self)):
                array.append(self[x][i])
            print("attribute", i, "max value", max(array))

    def splitIntoLines(self):
        return re.split(r'\n', self)

    def listAttributesAndTheirNumbers(self):
        lines = SystemDecyzyjny.splitIntoLines(self)
        myArray = []
        for line in lines:
            myArray.append(line.split(" "))
        return myArray


def main():
    SystemDecyzyjny.printFile("australian-type.txt")
    array = SystemDecyzyjny.splitIntoLines(open("australian-type.txt").read())
    print(array)
    lines = SystemDecyzyjny.listAttributesAndTheirNumbers(open("australian.txt").read())
    SystemDecyzyjny.minAttributeValue(lines, SystemDecyzyjny.getNumericAttributes(array))
    SystemDecyzyjny.maxAttributeValue(lines, SystemDecyzyjny.getNumericAttributes(array))


if __name__ == "__main__":
    main()