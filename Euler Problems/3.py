n = 600851475143
divisor = 2
factors = []

while n > 1 :
    if n % divisor == 0:
        factors.append(divisor)
        n = n // divisor 
    divisor += 1
print(factors)
print (max(factors))

