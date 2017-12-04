import os
csvpath = 'budget_data_1.csv'

import csv

print('Financial Analysis')
print('------------------')

revenue = []
period = []
revchange = []
revchange1 = []
date =[]

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)

    data = list(csvreader)
    row_count =len(data)
    
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)
    
    total=0
    total1=0

    for row in csvreader:
        
        total = int(total) + int(row[1])
        total1 = int(total1) + abs(int(row[1]))

        date.append(row[0])
        revenue.append(row[1])
        least=min(revenue)
        most=max(revenue)


    for i in range(2):
        
        revchange1.append(int(revenue[i]))

    print(revchange1)

    for i in range(1,len(revenue)):
        
        revchange.append(int(revenue[i])-int(revenue[i-1]))
        
    avgrev=(sum(revchange)/len(revenue))

    maxdate=str(date[revchange.index(max(revchange))])
    mindate=str(date[revchange.index(min(revchange))])
        
average=(total1/row_count) 

print(str("Total Months: ") + str(len(revenue)))
print(str('Total Revenue: $') + str(total))
print(str('Average Revenue Change: ')+str(avgrev))
print(str('Greatest Increase in Revenue: ')+ maxdate +str('($')+str(max(revchange))+str(')'))
print(str('Greatest Decrease in Revenue: $')+mindate+str('($')+str(min(revchange))+str(')'))

#f=open("file.txt", "w")
#print >>f, str("Total Months: ") + str(len(revenue))

#with open(“Output.txt”, “w”) as text_file:
    #text_file.write(”Purchase Amount: “.format(avgrev))


f=open("main.py.txt","w")
f.write(str('Financial Analysis'))
f.write("\n")
f.write(str("------------------"))
f.write("\n")
f.write(str("Total Months: ") + str(len(revenue)))
f.write("\n")
f.write(str('Total Revenue: $') + str(total))
f.write("\n")
f.write(str('Average Revenue Change: ')+str(avgrev))
f.write("\n")
f.write(str('Greatest Increase in Revenue: ')+ maxdate +str('($')+str(max(revchange))+str(')'))
f.write("\n")
f.write(str('Greatest Decrease in Revenue: $')+mindate+str('($')+str(min(revchange))+str(')'))