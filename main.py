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


    




        