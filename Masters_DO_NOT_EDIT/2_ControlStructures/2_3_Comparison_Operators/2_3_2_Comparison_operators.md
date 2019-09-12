# 2_3_2_Comparison_operators

Comparison operators can be used in if statements. This allows the program to do different things depending on the value of a variable or an expression.

```python

"""
Can Yelena clear the bar in the high jump
event? Find out using an if statement and
a comparison operator!
"""

# Set the bar
height_of_bar = 1.9
print("The bar is " + str(height_of_bar) + " meters off the ground.")

# Yelena jumps!
yelena_jump = 2.0
print("Yelena's jump: " + str(yelena_jump) + " meters.")

if yelena_jump > height_of_bar:
    print("Yelena cleared the bar!")
else:
    print("Yelena didn't clear the bar.")
```