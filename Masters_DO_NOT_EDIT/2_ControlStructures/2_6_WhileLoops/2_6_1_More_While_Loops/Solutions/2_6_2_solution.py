number = int(input("Enter a number:"))

count = 2

while number % count != 0:
    count += 1

print(count)