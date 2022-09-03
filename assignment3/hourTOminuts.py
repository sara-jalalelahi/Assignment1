print('select the desired convertion :')
choice=int(input('second to hour=1 and hour to second=2 :'))

if choice==1:
  number=int(input('enter second:'))
  hour=number//3600
  minute=(number%3600)//60
  second=(number%3600)%60
  print('%.2d :%.2d :%.2d'%(hour,minute,second))

elif choice==2:
  hou=int(input('enter hour :'))
  min=int(input('enter minute:'))
  sec=int(input('enter second:'))
  hou_in_sec=hou*3600
  min_in_sec=min*60
  print('time in second:',hou_in_sec+min_in_sec+sec)
  
