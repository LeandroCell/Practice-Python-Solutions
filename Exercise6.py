word = input("Enter a word: ")

reverse = word[::-1].title()

print("Reversed:", reverse)

if word == reverse:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
