
for i in range (10):
    vroodi=list(input('enter word:'))
    a=vroodi.pop(0).upper()
    vroodi.insert(0,a)
    b=''.join(vroodi)
    print(b)
