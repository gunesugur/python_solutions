a = 0
b = 1
c = 0
listt = []

for i in range(1,11):
    c = a + b
    b = a
    a = c
    listt.append(c)

print("Result :",listt)
