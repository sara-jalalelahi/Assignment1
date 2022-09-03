
defaultpass=1234
defaultuser='user'

password=int(input('enter password :'))
user=input('enter username :')
if (defaultpass==password)and(defaultuser==user):
        print('welcom')
else:
    for i in  range(2):
        password=int(input('enter password  :'))
        user=input('enter username :')
    print('acount loke')
