#fabonacci series
num = input("Enter a number: ")
a = int(0)
b = int(1)
sum = 0
count = 1
print("Fibonacci sequence:")
while int(count) <= int(num):
    print(sum)
    count += 1
    a = b
    b = sum
    sum = a + b