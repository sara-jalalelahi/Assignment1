win=0
lose=0
equal=0
conter=1
for i in range (8):
  print('enter the result (win=w  ,  equal=e  ,  lose=l)')
  team=input('enter the result of match:')
  if team=='w' :
    win+=1
  elif team=='e':
    equal=equal+1
  elif team=='l':
    lose=lose+1
  conter=conter+1
  finalscore=(win*3)+equal
print('final score=',finalscore,'win=',win,'equal=',equal,'lose=',lose)
