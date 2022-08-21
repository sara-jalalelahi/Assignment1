import random
tekrar=0
my_num=21
while True:
  computer_guess=random.randint(0,99)
  print( computer_guess)
  if computer_guess==my_num:
     print('well done')
     break
 
  elif computer_guess >= my_num:
     print('lower') 
     tekrar+=1 
     continue

  else:
      print('higher')
      tekrar+=1
      continue
  
print('number of guesses=',tekrar)    
 