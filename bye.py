import csv
import operator
a = "Yes"

with open('Pre_Study.csv') as file:
  
    
 csv_reader = csv.reader(file, delimiter= ',')
 next(csv_reader)
 next(csv_reader)

 
 sort = sorted(csv_reader, key = operator.itemgetter(14))

 for eachline in sort:
    if eachline[14] == a:
      print(eachline[7], eachline[14], eachline[15])

 for eachline in sort:
     if eachline[14] == a:
      print(eachline[7].replace("2018argrewrite_",""))
      
