# import random
# tekrar=0
# my_num=21
# while True:
#   computer_guess=random.randint(0,99)
#   print( computer_guess)
#   if computer_guess==my_num:
#      print('well done')
#      break
 
#   elif computer_guess >= my_num:
#      print('lower') 
#      tekrar+=1 
#      continue

#   else:
#       print('higher')
#       tekrar+=1
#       continue
  
# print('number of guesses=',tekrar)    
 
 
 
 
 
 
 
 










import random
tekrar=0
while True:
 guess=random.randint(0,99)
 print('computer guess=',guess)
 tekrar+=1
 vroodi=int(input('1=greater\n2=lower\n3=yes ,its true\n'))
 if vroodi==1:
    guess1=random.randint(guess,99)
    print('computer gueses=',guess1)
    vroodi=int(input('1=greater\n2=lower\n3=yes ,its true\n'))
    guess=guess1
    print('guess1=',guess1)
    tekrar+=1
 if vroodi==2:
    guess2=random.randint(0,guess)
    print('computer guesss=',guess2)
    vroodi=int(input('1=greater\n2=lower\n3=yes ,its true\n'))
    guess=guess2
    print('guess2=',guess2)
    tekrar+=1
 if vroodi==3:
    print('well done!!!')
    break
print('guess',tekrar,'times')


  
 
 
