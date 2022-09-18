vroodi=(input('enter word:'))
sedadar=['a','e','i','o','u']
for j in range (len(vroodi)):
 for i in vroodi:
   if i in sedadar:
      output=vroodi. replace (i,"?")
      vroodi=output
print(output)   
