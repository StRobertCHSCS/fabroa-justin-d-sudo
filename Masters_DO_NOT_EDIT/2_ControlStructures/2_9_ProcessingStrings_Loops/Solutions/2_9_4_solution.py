my_string = input("Enter a string: ")

code_count = 0

for i in range(len(my_string) - 2):
    if my_string[i:i + 2] == "co" and my_string[i+3] == "e":
        code_count += 1

print(code_count)