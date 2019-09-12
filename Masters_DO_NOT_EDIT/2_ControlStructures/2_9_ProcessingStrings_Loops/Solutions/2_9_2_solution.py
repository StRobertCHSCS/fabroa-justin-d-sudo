my_string = input("Enter a string: ")

hi_count = 0

for i in range(len(my_string)-1):
    if my_string[i:i+2] == "hi":
        hi_count += 1

print(hi_count)
