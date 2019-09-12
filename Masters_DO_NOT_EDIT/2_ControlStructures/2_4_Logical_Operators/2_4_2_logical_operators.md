# 2_4_2_Logical_Operators

In college, I noticed a sign on the wall of one of my classrooms that read **“NO FOOD OR DRINK”**. Now, the spirit of this sign is to prevent people from entering the classroom if they have any food or beverage. However, if you try to write this literally as a Python boolean expression, this isn’t quite the policy it enforces.

Try running this example program with different values of `has_food` and `has_drink`. Then, see if you can make as small of a change as possible to the program so that it only says you are allowed if both variables are `False`

```python
has_food = False
has_drink = True

# The line below isn't quite right...
if not has_food or has_drink:
    print("You can come into the classroom.")
else:
    print ("You cannot come into the classroom.")
```