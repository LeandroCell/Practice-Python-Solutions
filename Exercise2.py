number = int(input("Enter a number: "))


if number % 4 == 0:
    print(f"{number} is divisible by 4.")
elif number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

num = int(input("Enter a number: "))
check = int(input("Enter a number to check divisibility: "))

if num % check == 0:
    print(f"{num} is divisible by {check}.")
else:
    print(f"{num} is not divisible by {check}.")
