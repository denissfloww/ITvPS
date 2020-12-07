import Import
import NaivBayes
import PreProcessing

pwcValues = Import.Import()
testValues = Import.ImportTestDocuments("test.csv")
pcCounts = Import.Import("pc.csv")

for key, val in testValues.items():
    val[0] = PreProcessing.ToLowerCase(str(val[0]))
    val[0] = PreProcessing.PunctuationReplace(str(val[0]))
    val[0] = PreProcessing.Tokenizer(val[0])
    val[0] = PreProcessing.LemmAndStem(val[0])

res = NaivBayes.Pcd(testValues, pwcValues, pcCounts)
docClasses = []
for key, val in res.items():
    docClasses.append(val[0].index(max(val[0])) + 1)
