
import math
for i in range(int(input('time to use?'))):
 choice=int(input('choose your desired calculator:\n basic calculator=1\n advanced calculator=2 \n '))
 if choice==1 :
    vroodi_b=int(input('choose your desired operation:\n addition=1\n subtraction=2\n multiplication=3\ndivision=4 \n'))
    if vroodi_b==1  :
        for i in range(int(input('how many times do you want to use the operator?'))):
          x=float(input('enter number:'))
          x+=x
        print('sum of numbers =',x)
        
    elif vroodi_b==2:
        for i in range(int(input('how many times do you want to use the operator?'))):
          x=float(input('enter number:'))
          x-=x
        print('subtraction of numbers =',x)
        break
    elif vroodi_b==3:
        javab=1
        for i in range(int(input('how many times do you want to use the operator?'))):
          x=float(input('enter number:'))
          x1=1 
          x2=x*x1
          javab*=x2
        print('multiplication of numbers =',javab)
        break
    elif vroodi_b==4:
        # javab=1
        # for i in range(int(input('how many times do you want to use the operator?'))):
          x=float(input('enter number:'))
          y=float(input('enter number:'))
          # x1=1 
          # x2=x/x1
          javab=x/y
          print('division of numbers =',javab)
          break
if choice==2:
    vroodi_a=int(input('choose your desired operation:\n sin=1\n cos=2\n tan=3\n pow=4\n radians to degree=5\n square root=6\n degree to radian=7\n correct devision=8\nmod=9\nabsolute value=10\n power2=11\n prime=12\n')) 
    if vroodi_a==1:
       x=math.sin(float(input('enter number:')))
       print('sin of the dsired number=',x)
    elif vroodi_a==2:
       x=math.cos(float(input('enter number:')))
       print('cos of the dsired number=',x)
    elif vroodi_a==3:
       x=math.tan(float(input('enter number:')))
       print('tan of the dsired number=',x) 
    elif vroodi_a==4:
       a=float(input('enter your desired number:'))
       b=float(input('enter your desired pow:'))
       x=math.pow(a,b)
       print(a,'to the power of',b,'=',x) 
    elif vroodi_a == 5:   
       a=float(input('enter the angle in degree:'))
       b=math.radians(a)
       print(a,'degree to radians =',b)  
    elif vroodi_a==6:
       a=float(input('enter the number:'))
       b=math.sqrt(a)
       print('the square root of',a,'=',b)
    elif vroodi_a==7:
       a=float(input('enter the angle in radians:'))
       b=math.degrees(a)
       print(a,'radians to degree =',b)
    elif vroodi_a==8:
       a=float(input('enter number:'))
       b=float(input('enter number:'))
       print(a,'//',b,'=',a//b)
    elif vroodi_a ==9:
       a=float(input('enter number:'))
       b=float(input('enter number:'))
       print(a,'%',b,'=',a%b)
    elif vroodi_a ==10:
       a=float(input('enter number:'))
       b=math.fabs(a)
       print('absolute value=',b)
    elif vroodi_a==11:
       a=float(input('enter number:'))
       b=math.pow(a,2)
       print('the power of tow =',b)
    elif vroodi_a==12:
        num=int(input('enter num:'))
        if num>1:
           for i in range(2,num//2):
             if num%i==0:
               print(num,'is not a prime number')
               break
             else:
              print(num,'is a prime number')
        else :
          print(num,'is not a prime number')