adad=(input('enter number :'))
odd=0
even=0
while adad !=0 :
    lastdig=int(adad)%10
    if lastdig%2==0:
        even=even+1
    else : 
        odd=odd+1 
    adad=int(adad)//10
print('even digit(s) :',even, '  and  ' ,'odd digit(s) :',odd)        

if even > odd:
    print('even digits are more')
else:
      print('odd digits are more')   


