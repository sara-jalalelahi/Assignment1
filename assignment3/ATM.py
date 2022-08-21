default_pass=1234
password=int(input('enter your password:'))
container=password
invers=4321

if container==default_pass :
      print('wellcom')

elif container==invers:
       print('Inform the FATA police')
       
else:
    for i in range (3):
     nextPass=int(input('enter your password again:'))
     if nextPass==default_pass:
       print('wellcom')
       break
    else:
       print('your account has been locked')
        

