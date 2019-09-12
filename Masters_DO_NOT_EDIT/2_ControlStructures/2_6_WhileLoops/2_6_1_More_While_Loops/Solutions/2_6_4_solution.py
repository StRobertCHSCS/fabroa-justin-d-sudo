starting_distance = float(input("Enter the starting distance: "))
target_distance = float(input("Enter the target distance: "))

total = starting_distance
day_count = 1

while total <= target_distance:
    total = total + total*0.1
    day_count += 1

print("You will be ready to run " + str(target_distance)+"km in " + str(day_count) + " days.")