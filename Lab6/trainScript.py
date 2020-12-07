import Export
import Import
import NaivBayes
import PreProcessing
import VecModel

countClasses, values = Import.ImportTrainDocumets("train.csv")
for key, val in values.items():
    val[0] = PreProcessing.ToLowerCase(str(val[0]))
    val[0] = PreProcessing.PunctuationReplace(str(val[0]))
    val[0] = PreProcessing.Tokenizer(val[0])
    val[0] = PreProcessing.LemmAndStem(val[0])

universum = VecModel.MakeUniversum(values)
tfdict = VecModel.TF(universum, values)
commcountDict = NaivBayes.CountWordInEachClasses(values)
pwcdict = NaivBayes.Pwc(tfdict, commcountDict, universum)
pc = NaivBayes.Pc(countClasses)
Export.Export('pwc.csv', pwcdict)
Export.Export('pc.csv', pc)