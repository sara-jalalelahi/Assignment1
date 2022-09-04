
default_list = []
for i in range(10):
    number = int(input("enter number = "))
    default_list.append(number)
print("first list  :",default_list)
for num in range(len(default_list)):
    for j in range(num+1,len(default_list)):
        if default_list[num] > default_list[j] :
            default_list[num],default_list[j] = default_list[j],default_list[num]
print("sorted list :",default_list)



