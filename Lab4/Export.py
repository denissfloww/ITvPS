import csv


def ExportCsv(dict, counter):
    with open('model.csv', 'w+', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        first_str = "Term "
        for i in range(1, counter):
            first_str += "Text:" + str(i) + " "

        first_str = first_str.split(" ")
        a_pen.writerow(first_str[:-1])
        for i, doc in dict.items():
            str_r = [i] + doc
            a_pen.writerow(str_r)


def ExportCsvMeasures(cos, jacc, dice, inpNumber):
    with open('Measures.csv', 'w+', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow("Текст Cosine Jaccard Dice".split(" "))
        i = 0
        for key, val in cos.items():
            str_r = ""
            str_r += str(inpNumber[i]) + ";"
            str_r += str(cos[key][0]) + ";"
            str_r += str(jacc[key][0]) + ";"
            str_r += str(dice[key][0])
            a_pen.writerow(str_r.split(";"))
            i += 1
