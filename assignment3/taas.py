
import random
container=0
tass=random.randint(1,6)
if tass==6:
    print('6')
    print('jam=6')
else :
  while tass!= 6:
     tass=random.randint(1,6)
     print('tass=',tass)
     container +=tass
  print('jam=',container)



