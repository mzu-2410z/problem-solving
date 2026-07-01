number = int(input("Enter a number: "))

if number == 0:
    print(f"{number} is zero.")
elif number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("Invalid Input")