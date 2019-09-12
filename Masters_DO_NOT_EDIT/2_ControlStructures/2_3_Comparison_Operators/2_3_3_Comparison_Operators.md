# 2_3_3_Comparison_Operators

Comparison operators can also be used in variable assignments! In this example, `height` and `height_requirement` are both float variables, and `can_ride_roller_coaster` is a boolean variable whose value is the result of a comparison expression. `can_ride_roller_coaster` can then be used in an if statement to make the program print different things depending on how `height` compared to `height_requirement`.
```python
height = 5.5
height_requirement = 5.0

# You must be at least 5.0 feet tall to
# ride the roller coaster.
can_ride_roller_coaster = height >= height_requirement

if can_ride_roller_coaster:
    print("You are tall enough to ride this roller coaster!")
else:
    print("Sorry, you aren't tall enough.")
```
