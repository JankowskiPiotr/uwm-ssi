import Common


class NaiwnyKlasyfikatorBayesa():
    def main(self):
        lines = Common.listAttributesAndTheirNumbers(open("australian_TST.txt").read())
        australianTRNList = Common.listAttributesAndTheirNumbers(open("australian_TRN.txt").read())
        lines = Common.delLastColumnAndRow(lines)
        australianTRNList = Common.delLastColumnAndRow(australianTRNList)


if __name__ == "__main__":
    NaiwnyKlasyfikatorBayesa.main("args")