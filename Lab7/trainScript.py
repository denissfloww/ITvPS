import Export
import Import
import NaivBayes
import PreProcessing
import VecModel
import Roccio

trainDocName = ['sport_all.txt', 'tech_all.txt']
doc, countDocInClass, docClass = Import.ImportTrainDocumets(trainDocName)
for key, val in doc.items():
    val[0] = PreProcessing.ToLowerCase(str(val[0]))
    val[0] = PreProcessing.PunctuationReplace(str(val[0]))
    val[0] = PreProcessing.Tokenizer(val[0])
    val[0] = PreProcessing.LemmAndStem(val[0])
universum = VecModel.MakeUniversum(doc)
tfdict = VecModel.TF(universum, doc)
tfidfDict = VecModel.TFIDF(tfdict, len(doc), universum, doc)
res = Roccio.RoccioTrain(countDocInClass, tfidfDict, docClass)
Export.Export("roccio.csv", res)