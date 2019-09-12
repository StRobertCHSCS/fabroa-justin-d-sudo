number = int(input("Enter a number:"))

count = 0

while 2**count < number:
    count += 1

print("exponent:", count-1)
print("2**n:", 2**(count-1))

