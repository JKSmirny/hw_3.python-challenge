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

with open("poll.main.txt", "w") as txtfile:
    txtpath = os.path.join('analysis', 'poll.main.txt')       
    txtfile.writelines("Election date analysis\n")
    txtfile.writelines("Total number of votes: {}\n".format(total_votes))
    txtfile.writelines("Candidate Khan:  {}\n".format(Khan))
    txtfile.writelines("Candidate Correy:  {}\n".format(Correy))
    txtfile.writelines("Candidate Li:  {}\n".format(Li))
    txtfile.writelines("Candidate OTooley:  {}\n".format(OTooley))
    txtfile.close()

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
                        winner = "OTooley" 
                elif Li > Correy:
                        winner = "Li"
                elif Correy > Khan:
                        winner = "Correy"
                elif Khan > OTooley:
                        winner = "Khan"
                print(winner)

with open("poll.main.txt", "w") as txtfile:
    txtpath = os.path.join('analysis', 'poll.main.txt')       
    txtfile.writelines("Election date analysis\n")
    txtfile.writelines("Total number of votes: {}\n".format(total_votes))
    txtfile.writelines("Candidate Khan:  {}\n".format(Khan))
    txtfile.writelines("Candidate Correy:  {}\n".format(Correy))
    txtfile.writelines("Candidate Li:  {}\n".format(Li))
    txtfile.writelines("Candidate OTooley:  {}\n".format(OTooley))
    txtfile.writelines("The winner is: " {}\n".format(winner))
    txtfile.close()
   

    




        