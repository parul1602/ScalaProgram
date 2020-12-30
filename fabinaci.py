num = []
a = 0
b = 1
num.append(a)
num.append(b)
for i in range(0, 10):
    c = a + b
    num.append(c)
    a=b
    b=c
print(num)

