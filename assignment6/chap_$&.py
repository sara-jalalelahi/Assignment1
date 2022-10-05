# row=int(input('enter the row:'))
# column=int(input('enter the column:')) 
# counter=0
# # board=[]

# for i in range(0,row):
#     for j in range(0,column+1):
#         if counter%2==0:
#           print('$ &',end=' ')
#         #   counter+=1
#         # if counter%2!=0:
#         #   print('& $',end=' ')
#         #   counter+=1
#     print()      


# for i in range(1,row+1):
#     for j in range(1,column+1):
#         if counter%2!=0:
#           print('& $',end=' ')
#           counter+=1
#     print()  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
def m_n():
 n=int(input("please enter rows: "))
 m=int(input("please enter columns: "))
 for i in range(n):#satr

        if i % 2 == 0: 

            print("$&"*((m//2)))#stun
    
        else:
            
            print("&$"*((m//2)))#stun
 print(m_n)
 
m_n()

      