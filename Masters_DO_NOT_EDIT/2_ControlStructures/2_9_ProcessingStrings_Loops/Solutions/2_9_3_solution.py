cat_count = 0
dog_count = 0

my_string = input("Enter a string: ")

for i in range(len(my_string) - 2):
    if my_string[i: i + 3] == "cat":
        cat_count += 1
    elif my_string[i: i + 3] == "dog":
        dog_count += 1

if cat_count == dog_count:
    print(True)
else:
    print(False)