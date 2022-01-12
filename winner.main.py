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

with open(election_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
                if OTooley > Li:
                        print("Winner is OTooley")
                elif Li > Correy:
                        print("Winner is Li")
                elif Correy > Khan:
                        print("Winner is Correy")
                elif Khan > OTooley:
                        print("Winner is Khan")



    




        