a =[3, 5 , 6 , 9, 'banana']
b = [10]
c = [15, 20, 25]
a[4] = b[0]
a[5:6] = c
print(a)

a.remove(3)
a.append(True)
print(a)

a.pop()
print(a)
