a=0
b=1
c=0
sum = 0
while a<4000000:
    if a%2 == 0:
        sum+=a
    c = a + b
    a = b
    b = c
print(sum)