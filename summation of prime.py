import time
start=time.clock()
i=int(input('please enter  an integer:'))
#创建一个空list
Sum = 0
r=list()
NumPrime = 0
#添加元素2
r.append(2)
#从3开始挨个筛选
for a in range(3,i):
    b=False

#用a除以小于a的质数b
    for b in r:
        if a%b==0:
            b=False
            break
        else:
            b=True
    if b==True:
        r.append(a)
        NumPrime +=1
        Sum += a
    if a >= 2000000:
        break

print (r)
print(NumPrime)
print(Sum)
t=(time.clock()-start)
print (t)