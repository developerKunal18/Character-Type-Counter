text = input("Enter text: ")

letters = 0
digits = 0
spaces = 0
special = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special += 1

print("\nCharacter Count:")
print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)
