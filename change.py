import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    column = []
    for line in csvreader:
        column.append(float(line[1]))
        print(column)

txtpath = os.path.join('analysis', 'Budget.changes.txt')
txtfile = open(txtpath, "w")
text1 = ["Changes in Profits/Losses: "]
text2 = str(column)
txtfile.writelines(text1)
txtfile.writelines(text2)
text2+=str(column)
txtfile.close()