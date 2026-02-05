# sum sq of first 100 natural numbers 
l1 = []
for i in range (101):
    x = i*i
    l1.append(x)
s1 = sum(l1)
print(s1)

l2 = []
for j in range (11):
    l2.append(j)
s2 = sum(l2)
sq_2 = s2 ** 2
print(sq_2)

dif = sq_2 - s1
print(dif)