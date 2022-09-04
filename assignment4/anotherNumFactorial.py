vroodi=int(input('enter a number:'))
result=1
for i in range (1,vroodi-1) :
   vroodi=vroodi/i
   if  vroodi==1:
       result = True
       break
   else:
        result = False
        continue
    
if result == True:
    print('this number is another numbers factorial')

else:
    print('this number is not another numbers factorial')
