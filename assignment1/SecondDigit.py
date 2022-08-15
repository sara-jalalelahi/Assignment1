number=input('please enter number:')
reversnum=(number)[::-1]
first2dig=int(reversnum)%100
reversfirst2dig=str(first2dig)[::-1]
secdig=int(reversfirst2dig)%10
print(secdig)
