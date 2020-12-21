import FPRcalculation
import Import
import NaivBayes
import PreProcessing
import Roccio
import VecModel

roccioValues = Import.Import("roccio.csv")

testValues = Import.ImportTestDocuments("test.csv")

for key, val in testValues.items():
    val[0] = PreProcessing.ToLowerCase(str(val[0]))
    val[0] = PreProcessing.PunctuationReplace(str(val[0]))
    val[0] = PreProcessing.Tokenizer(val[0])
    val[0] = PreProcessing.LemmAndStem(val[0])
universum = VecModel.MakeUniversum(testValues)
tfdict = VecModel.TF(universum, testValues)
tfidfDict = VecModel.TFIDF(tfdict, len(testValues), universum, testValues)
roccioClassCount = 0
for key, val in roccioValues.items():
    roccioClassCount = len(val)
    break
res = Roccio.RoccioCalc(tfidfDict, roccioValues, len(testValues), roccioClassCount)
for key, val in res.items():
    print(val)
