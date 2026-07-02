n = int(input("Enter a number: "))
sum = 0

if n < 0 or n == 0:
    print("Please enter a valid number!")

else:

    for x in range(n):
        x+=1
        sum += x

print(f"The sum of first {n} numbers is {sum}.")