n = int(input("Enter a number: "))
odd_count = 0
even_count = 0
for i in range(1, n):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers from 1 to {n} are {even_count}.")
print(f"Odd numbers from 1 to {n} are {odd_count}.")