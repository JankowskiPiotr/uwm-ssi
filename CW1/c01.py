class SystemDecyzyjny:
    NUMBER_OF_ATTRIBUTES = 15

    def printFile(self):
        f = open(self)
        print(f.read())

def main():
    SystemDecyzyjny.printFile("australian-type.txt")




if __name__ == "__main__":
    main()
