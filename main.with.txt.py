import os
import csv

election_csv = os.path.join('.','Resources','election_data.csv')

Khan = 0
Correy = 0
Li = 0
OTooley = 0

with open(election_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
                if row[2] == "Khan":
                        Khan += 1
                if row[2] == "Correy":
                        Correy += 1        
                if row[2] == "Li":
                        Li += 1
                if row[2] == "OTooley":
                        OTooley += 1

total_votes = Khan + Correy + Li + OTooley

print(f'Khan:, {Khan/total_votes}')
print(Khan)
print(f'Correy:, {Correy/total_votes}')
print(Correy)
print(f'Li:, {Li/total_votes}')
print(Li)
print(f'OTooley:, {OTooley/total_votes}')
print(OTooley)

txtpath = os.path.join('analysis', 'Khan.main.txt')
txtfile = open(txtpath, "w")
text1 = ["Candidate Khan:  "]
text2 = str(Khan)
text3 = [";  Percent:  "]
text4 = str(Khan/total_votes)
txtfile.writelines(text1)
txtfile.writelines(text2)
txtfile.writelines(text3)
txtfile.writelines(text4)

txtpath = os.path.join('analysis', 'Correy.main.txt')
txtfile = open(txtpath, "w")
text1 = ["Candidate Correy:  "]
text2 = str(Correy)
text3 = [";  Percent:  "]
text4 = str(Correy/total_votes)
txtfile.writelines(text1)
txtfile.writelines(text2)
txtfile.writelines(text3)
txtfile.writelines(text4)

txtpath = os.path.join('analysis', 'Li.main.txt')
txtfile = open(txtpath, "w")
text1 = ["Candidate Li:  "]
text2 = str(Li)
text3 = [";  Percent:  "]
text4 = str(Li/total_votes)
txtfile.writelines(text1)
txtfile.writelines(text2)
txtfile.writelines(text3)
txtfile.writelines(text4)

txtpath = os.path.join('analysis', 'OTooley.main.txt')
txtfile = open(txtpath, "w")
text1 = ["Candidate OTooley:  "]
text2 = str(OTooley)
text3 = [";  Percent:  "]
text4 = str(Li/total_votes)
txtfile.writelines(text1)
txtfile.writelines(text2)
txtfile.writelines(text3)
txtfile.writelines(text4)
    




        