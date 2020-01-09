import Common
import random


class TrainAndTest():
    def main(self):
        print("T&T")
        fDec = open("result/dec_bayesT&T.txt", "w+")
        lines = Common.listAttributesAndTheirNumbers(open("australian.txt").read())
        randomSystemIndexList = TrainAndTest.generateTRNandTSTIndexList(lines, 0.5)
        randomTrnSystem = Common.fromIndexToList(randomSystemIndexList[0], lines)
        randomTstSystem = Common.fromIndexToList(randomSystemIndexList[1], lines)
        countedParams = Common.countParam(randomTstSystem, randomTrnSystem)
        classified = Common.numOfCorrectlyClassified(countedParams, Common.getListOfDecisionsTST(randomTstSystem), fDec)
        globalAccuracy = Common.getGlobalAccuracy(classified)
        allClasses = Common.unique(Common.getListOfDecisionsTST(lines))
        print("Global accuracy = " + str(globalAccuracy))
        print("Balanced accuracy = " + str(Common.getBalancedAccuracy(allClasses, classified)))
        fAcc = open("result/acc_bayesT&T.txt", "w+")
        fAcc.write(f"Global accuracy = " + str(globalAccuracy) + "\nBalancedAccuracy = " + str(
            Common.getBalancedAccuracy(allClasses, classified)))
        print("\n")

if __name__ == "__main__":
