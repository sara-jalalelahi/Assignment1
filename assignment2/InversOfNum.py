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
    
