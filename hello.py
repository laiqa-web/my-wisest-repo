import csv
import operator

with open('Pre_Study.csv') as file:
  
    
 csv_reader = csv.reader(file, delimiter= ',')
 next(csv_reader)
 next(csv_reader)

 
 sort = sorted(csv_reader, key = operator.itemgetter(14))

 for eachline in sort:
     print(eachline[7], eachline[14], eachline[15])


     
