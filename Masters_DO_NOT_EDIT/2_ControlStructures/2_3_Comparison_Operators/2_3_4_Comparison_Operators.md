# 2_3_4_Comparison Operators

Here is an example of an if-elif-else statement. It is similar to an if-else statement, except that it provides more than two courses of action for the program.

Note that a particular branch of an if-elif-else statement only gets run if the condition of every `if` or `elif` before it has evaluated to `False`.



```python
age = 33

# Note that each branch below only gets
# reached IF every prior branch had
# a condition that evaluated to False.
if age < 18:
    print("0 - 17")
elif age < 26:
    print("18 - 25")
elif age < 36:
    print("26 - 35")
elif age < 46:
    print("36 - 45")
elif age < 56:
    print("46 - 55")
elif age < 66:
    print("56 - 65")
else:
    print("66+")
```