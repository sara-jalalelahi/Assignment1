first_list=[]
for i in range(10):
 container=int(input('enter numbers:'))
 first_list.append(container)
print(first_list)
for num in range (1,len(first_list)):
    if first_list[num-1] < first_list[num]  :  
      sequence=True 
      if first_list[num-1] > first_list[num]:
        sequence==1
        break
    elif  first_list[num-1] > first_list[num]:
      if first_list[num-1] < first_list[num]  : 
        sequence==1
        break
      sequence=False
      break
    else:
      sequence=1  
if sequence==True:
    print('yes,soodi')       
elif sequence==False:
    print('yes,nzooli')    
elif sequence==1:
    print('no')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# first_list=[]
# for i in range(10):
#  container=int(input('enter numbers:'))
#  first_list.append(container)
# print(first_list)
# for num in range (1,len(first_list)):
#     if first_list[num-1] < first_list[num]  :  
#       sequence=True 
#       if first_list[num-1] > first_list[num]:
#         sequence==1
#         break
#     elif  first_list[num-1] > first_list[num]:
#       if first_list[num-1] < first_list[num]  : 
#         sequence==1
#         break
#       sequence=False
#       break
#     for num in first_list:
#      if  first_list[num-1] > first_list[num] and first_list[num] <first_list[num+1] or first_list[num-1] < first_list[num] and first_list[num] >first_list[num+1]  :
#       sequence=1  
#       break
# if sequence==True:
#     print('yes,soodi')       
# elif sequence==False:
#     print('yes,nzooli')    
# elif sequence==1:
#     print('no')