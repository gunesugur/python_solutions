number_1 = int(input("Please enter a number : "))
number_2 = int(input("Please enter one more number : "))
listt = []

for number in range(number_1, number_2+1):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                break
        else:
            listt.append(number)

print("Prime numbers from",number_1,"to", number_2,":",listt)
