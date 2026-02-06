# smallest number divisible by the first 20 numbers 

x = 1

while True:
    divisible = True

    for i in range (1,21):
        if x % i != 0: 
            divisible = False
            break
    if divisible :
        print (x)
        break

    x += 1 

        


