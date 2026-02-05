x = int(input("Enter your number: "))

for i in range (2,x+1):
    is_Prime= True
    for j in range (2,i):
        if i % j == 0:
            is_Prime = False
    if is_Prime :
        print (i)
        
        
        