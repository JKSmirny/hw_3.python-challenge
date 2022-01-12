import os
import csv

total_value = 0.00
diff = 0.00
average = 0.00
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)        
    csv_header = next(csvreader)
    column = []
    for line in csvreader:
        column.append(float(line[1]))
    total_value = sum(column)
    print(total_value)
    
    txtpath = os.path.join('analysis', 'changes.txt')
    txtfile = open(txtpath, "w")
    text1 = ["The changes in Profits/Losses: "]
    text2 = str(column)
    txtfile.writelines(text1)
    txtfile.writelines(text2)
    text2+=str(column)
    txtfile.close()
    print(column)

    txtpath = os.path.join('analysis', 'total_value.txt')
    txtfile = open(txtpath, "w")
    text1 = ["The total net of Profits/Losses: "]
    text2 = str(total_value)
    txtfile.writelines(text1)
    txtfile.writelines(text2)
    text2+=str(total_value)
    txtfile.close()
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    lines= len(list(csvreader)) - 1
    print(lines) 
    txtpath = os.path.join('analysis', 'total_months.txt')
    txtfile = open(txtpath, "w")
    text1 = ["The total amount of months: "]
    text2 = str(lines)
    txtfile.writelines(text1)
    txtfile.writelines(text2)
    text2+=str(lines)
    txtfile.close()
 
 
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    column = []
    for line in csvreader:
        column.append(float(line[1]))
        change = []
        diff = 0.00
        max = 0.00
        min = 0.00
        prev_column = column[0]
        for i in range(1, len(column)):
            diff = column[i] - prev_column
            change = [diff]
            prev_column = column[i]
        
            average = total_value/lines
            print (average)
 
    txtpath = os.path.join('analysis', 'Budget.average.txt')
    txtfile = open(txtpath, "w")
    text1 = ["The average change in Profits/Losses: "]
    text2 = str(average)
    txtfile.writelines(text1)
    txtfile.writelines(text2)
    text2+=str(average)
    txtfile.close()
 






