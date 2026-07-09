import operator
from pprint import pprint
from pathlib import Path

draft_3 = Path("/Users/t.abeba/Coding/ArgRewrite.V2/essays/Draft3 copy")

draft_3.glob("2018argrewrite_*.txt")

good_ids = [2,8,14,17,21,31,34,43,46,47,58,63,65,64,66,78,76]

x = list()
for a in draft_3.glob("2018argrewrite_*.txt"):
    for n in good_ids:
        
        if a.name == f"2018argrewrite_{n}.txt":
            x.append(a.name)
            x.sort()
            print((a.name))
     


"""
with open('draft1_2018argrewrite_.txt') as file:
      draftdata = draft_data(file)
      next(draftdata)
      next(draftdata)
#files of english learner
good_ids = [2,8,14,17,21,31,34,43,46,47,58,63,65,64,66,78,76]

sort = sorted(open, key = operator.itemgetter(1))
            
for eachdraft in sort:
      if eachdraft[14] == a:
       print(eachdraft)
"""