import random
container=[]
start=int(input('enter start of list:'))
finish=int(input('enter finish of list:'))
for i in range(int (input('enter len of list:'))):
    randomlist=random.randint(start,finish)
    if randomlist in container:
        continue
    container.append(randomlist)
print(container)



