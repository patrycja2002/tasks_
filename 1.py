a = [1,2,3,3,2,1,2,3]
print(set(a))
b = []
for z in a:
    if z not in b:
        b.append(z)
print(b)