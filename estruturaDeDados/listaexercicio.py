lst = ['!','u','o','t','r','e','c','a']
for i in range(5):
 troca = lst[i]
 print(lst[i])
 print(troca)
 lst[i] = lst[7-i]
 lst[7-i] = troca
 
print(lst)
