number = int(input("Please enter one more number : "))
listt = []

for x in range(2, number+1):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        listt.append(x)

print("Result : ",listt)
