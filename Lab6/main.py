import FPRcalculation
import Import
import NaivBayes
import PreProcessing

pwcValues = Import.Import()
testValues, sourceClasses = Import.ImportTestDocuments("test.csv")
pcCounts = Import.Import("pc.csv")
for key, val in testValues.items():
    val[0] = PreProcessing.ToLowerCase(str(val[0]))
    val[0] = PreProcessing.PunctuationReplace(str(val[0]))
    val[0] = PreProcessing.Tokenizer(val[0])
    val[0] = PreProcessing.LemmAndStem(val[0])
res = NaivBayes.Pcd(testValues, pwcValues, pcCounts)
resultClasses = []
for key, val in res.items():
    resultClasses.append(val[0].index(max(val[0])) + 1)
emptyDict = FPRcalculation.DictFiller(len(pcCounts))
infoClasses = FPRcalculation.Count(sourceClasses, resultClasses, emptyDict)
resultDict = FPRcalculation.Calculate(len(pcCounts), infoClasses)
for key, val in resultDict.items():
    print("Класс " + str(key) + ":")
    print("P: " + str(val[0]))
    print("R: " + str(val[1]))
    print("F1: " + str(val[2]))
    print("____________________________________________________________________________")
