vroodi=int(input('enter number :'))
firstnum=vroodi
container=0
while vroodi>0:
  lastdig=vroodi%10
  container=((container*10)+lastdig)
  vroodi=vroodi//10
  
print('revers is:',container)
if firstnum==container:
    print('makoos adad ba adad barabar ast')
else:
    print('makoos adad ba adad na barabar ast')     








# num = int(float (input('enter the  oposit number : ')))
# number =num
# count = 0

# while (num > 0) :
#     temp = num % 10 # 432 % 10 = 2
#     count = (count * 10) + temp #2
#     num //= 10    #43

# if (number == count):
#     print('Yes')
# else:
#     print('NO')

# #tafrigh
# sum = number + count

# #jam
# taf = number - count

# print(sum,taf)
