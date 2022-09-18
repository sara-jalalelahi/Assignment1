import random 
#   sang=1, kaghaz=2, ghychi=3
counter1=0
counter2=0
round=int(input('enter games round :'))
chand_nafare=int(input('1 nafare=1 \n2 nafare=2 \nenter :'))
while counter1!=round or counter2!=round:

    if chand_nafare==2:
     print('sang=1,kaghaz=2,ghychi=3')
     user1=int(input('enter user1:'))
     user2=int(input('enter user2:'))
    #  if user1!=int(1 or 2 or 3) or user2!=int( 1 or 2 or 3): 
    #       print('enter 1 or 2 or 3  !!!')
    #       continue     
      
     if user1==user2:
         continue
     elif (user1==1 and user2==3) or (user1==2 and user2==1)or (user1==3 and user2==2):
        
         counter1+=1
         if counter1==round:
             print('user1 win')
           
     elif (user1==3 and user2==3) or (user1==1 and user2==2)or (user1==2 and user2==3):
        
         counter2+=1
         if counter2==round:
             print('user2 win')
         
     if counter1==round or counter2==round:
        
       break
    
    
    if chand_nafare==1:   

      list_default=[1,2,3]
      karbar=int(input('sang=1 , kaghaz=2, ghychi=3''\n''enter your choice :'))  
      compu=random.choice(list_default)
      print('computer=',compu)
      if karbar== compu:
          continue
      if (karbar==1 and compu==3)or(karbar==2 and compu==1)or(karbar==3 and compu==2):
          counter1+=1
          if counter1==round:
             print('you win')
             break    
      else:
    
          counter2+=1
          if counter2==round:
             print('computer win')
             break  
    
    
    
    
    
    
    