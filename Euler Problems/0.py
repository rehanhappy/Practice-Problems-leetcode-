#We’re summing odd square numbers among the first 893,000 square numbers.

n=893000
total = 0 
for i in range (1,n):
    if i % 2 == 1:
        total = total + (i*i)
print(total)