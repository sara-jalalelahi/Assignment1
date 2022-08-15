number=int(input('enter 6 digit number:'))
secdig=(number%100)//10
print(secdig)
fifthDig=(number%100000)//10000
print(fifthDig)
print('sum of second and fifth digit is :',secdig+fifthDig)