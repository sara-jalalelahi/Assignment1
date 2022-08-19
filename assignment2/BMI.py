weight=float(input('enter weight (kg):'))
height_cm=float(input('enter height (cm):'))
height_m=height_cm/100
bmi=(weight/(height_m)**2)
if bmi<18.5:
    print('kambud vazn')
elif 18.5<bmi<24.9  :
    print('vazn mamoli')
elif 25<bmi<29.9 :
    print('vazn bala')
elif 30<bmi<34.9 : 
    print('ezafeh vazn')
elif(bmi>35) :
    print('chagh')            
