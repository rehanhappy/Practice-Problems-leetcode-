#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
a = 1
b = 2
total = 0 
while a < 4000000:
    if a % 2 == 0:
        total = total + a 
    temp = a + b
    a = b 
    b = temp
print (total)