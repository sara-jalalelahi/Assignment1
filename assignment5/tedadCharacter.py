
counter_hroof=0
counter_char=0
counter_point=0
counter_kalame=0
counter_comma=0
counter_space=0
counter_spce=0


default_vroodi=input('enter your text:')
default_vroodi.lower
for i in default_vroodi:
    counter_char+=1
    if i=='.':
       counter_point+=1
    if i=="'":
       counter_comma+=1  
    if i==" ":
       counter_space+=1
    if i=='a' or 'b'or 'c'or 'd'or 'e'or 'f'or'g'or 'h'or 'i'or 'j'or 'k'or 'l'or 'm'or 'n'or 'o'or 'p'or 'q'or 'r'or 's'or 't'or 'u'or 'v'or 'w'or 'x'or 'y'or 'z':
         counter_hroof+=1
 
word=default_vroodi.strip()
for i in word:
    if i==' ':
        counter_spce+=1
print('word=',counter_spce+1)       
print('charachter=',counter_char)    
print('hroof=',counter_hroof)
print('noghte=',counter_point)
print('comma=',counter_comma)
print('space=',counter_space)
    


