number=int(input("Please Enter a number : "))
if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
           print(number,": It is not a Prime Number.")
           break
    else:
        print(number,": It is a Prime Number.")
else:
    print(number,": It is not a Prime Number.")
