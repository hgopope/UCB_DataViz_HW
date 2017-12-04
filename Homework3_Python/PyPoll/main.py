import os
csvpath = 'election_data_2.csv'

import csv

f=open("main.py.txt","w")

print('Election Results')
print('------------------')

votes = []
candidate =[]
name =[]
holder =[]

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)

    for row in csvreader:
        votes.append(row[0])
        name.append(row[2])
    
        if row[2] not in candidate:
            candidate.append(row[2])

    print(str("Total Votes: ") + str(len(votes)))
    print('------------------')


    f.write(str('Election Results'))
    f.write("\n")
    f.write(str('------------------'))
    f.write("\n")
    f.write(str("Total Votes: ") + str(len(votes)))
    f.write("\n")
    f.write(str('------------------'))
    f.write("\n")

    for i in range(0,len(candidate)):

        print(candidate[i]+str(": ")+str(round(name.count(candidate[i])*100/len(name),1))+str('% ')+str('(')+str(name.count(candidate[i]))+str(')'))
        f.write(str(candidate[i]+str(": ")+str(round(name.count(candidate[i])*100/len(name),1))+str('% ')+str('(')+str(name.count(candidate[i]))+str(')')))
        f.write("\n")
def winner(name):
         st = set(name)
         mx = -1
         for each in st:
             temp = name.count(each)
             if mx < temp:
                 mx = temp 
                 h = each 
         return h

print('------------------')
print("Winner:"+winner(name))
print('------------------')

f.write(str('-------------------'))
f.write("\n")
f.write(str("Winner:"+winner(name)))