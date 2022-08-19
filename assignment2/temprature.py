# tabdil dama

vroodi=int(input('\nfahrenheit to celisius=1 \n celisius to kelvin=2 \n kelvin to celisius=3\n celisius to fahrenheit=4\n fahrenheit to kelvin=5 \n kelvin to fahrenheit=6\nplease enter your desired conversion:'))
if vroodi== 1:
    fahrenheit= input('fahrenheit=')
    c=(float(fahrenheit)-32) / 1.8
    print(fahrenheit ,'fahrenheit is',c,'celisius')

elif vroodi== 2:
    celisius= input('celisius:') 
    k= float(celisius)+273.15
    print(celisius,'celisius is',k,'kelvin')

elif vroodi== 3:
    kelvin=input('kelvin:')
    c=float(kelvin)-273.15
    print(kelvin,'kelvin is',c,'celisius')

elif vroodi==4:
    celisius=input('celisius:')
    f=(float(celisius)*1.8)+32
    print(celisius,'celisius is',f,'fahrenheit')
   
elif vroodi==5:
    fahrenheit=input('fahrenheit:')
    k=(float(fahrenheit)+459.67)/1.8
    print(fahrenheit,'fahrenheit is',k,'kelvin')
    
elif vroodi==6:
    kelvin=input('kelvin:')
    f=(float(kelvin)*1.8)-459.67  
    print(kelvin,'kelvin is',f,'fahrenheit')  
       

     
     