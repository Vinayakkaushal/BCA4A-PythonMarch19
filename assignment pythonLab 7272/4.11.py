# factorial of a number
num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print("Factorial of", num, "is", fact)