
from itertools import count
number=int(input('enter number of names:'))
name_list=[]
seclist=[]
counter=1
for i in range (number):
    name=input('enter name:')
    name_list.append(name)
print(name_list)

for name in name_list:
    tedad=name_list.count(name)
    print(name,'=',tedad)
    