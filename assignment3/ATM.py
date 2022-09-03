default_pass=int(1234)
password=int(input('enter your password:'))
container=password
invers=int(4321)
count=0
while password!=0:
      count+=1
      password//=10
count_digit=count
print(count)

while count_digit!=4:
   tedad=0
   digit= int(input('enter 4 digit pass:'))
   if digit==default_pass :
       print('wellcom')
       break
   elif digit==invers :
       print('Inform the FATA police')
       break
   while digit!=0:
       tedad+=1
       digit//=10
   count_digit=tedad
   
      
if container==default_pass :
      print('wellcom')

elif container==invers :
       print('Inform the FATA police')
       
elif count_digit==4 and   password!= default_pass and invers  :
    for i in range (3):
     nextPass=int(input('enter your password again:'))
     if nextPass==default_pass:
       print('wellcom')
       break
     if nextPass==invers:
       print('Inform the FATA police')
       break

    else:
       print('your account has been locked')
       

      

