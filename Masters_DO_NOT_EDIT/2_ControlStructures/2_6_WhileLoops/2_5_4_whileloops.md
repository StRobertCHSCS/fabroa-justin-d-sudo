# 2_5_4_whileloops.py

Consider the code below that checks for divisibility. Change it so that instead of allowing the user to enter 0 for the denominator, your program repeatedly asks them to enter a number until the number they enter is not equal to zero.

```python
numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter denominator: "))

# Use a while loop here to repeatedly ask the user for
# a denominator for as long as the denominator is 0
# (or, put another way, until the denominator is not
# equal to 0).


if numerator / denominator * denominator == numerator:
    print("Divides evenly!")
else:
    print("Doesn't divide evenly.")

```
