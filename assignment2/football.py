win=0
lose=0
equal=0
conter=1
for i in range (8):
  print('enter the result (win=w  ,  equal=e  ,  lose=l)')
  result=input('enter the result of match:')
  
  if result=='w' :
    win+=1
  elif result=='e':
    equal=equal+1
  elif result=='l':
    lose=lose+1
  conter=conter+1
  finalscore=(win*3)+equal
  if result!= 'w'or'e'or'l':
    print('enter correct result!')
    break
print('final score=',finalscore,'win=',win,'equal=',equal,'lose=',lose)
