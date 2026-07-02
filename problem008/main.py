n = int(input("How many numbers? \t"))

largest_number = int(input("Enter number 1: \t"))

for i in range(2, n+1):
    x = int(input(f"Enter number {i}: \t"))
    if x > largest_number:
        largest_number = x
    else:
        continue

print(f"The largest number is {largest_number}")