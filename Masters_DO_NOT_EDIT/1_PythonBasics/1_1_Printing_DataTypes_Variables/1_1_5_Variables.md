# 1_1_5_variables.py

This example has two problems:

One of the variables is used before it is given a value.
Another of the variables isn’t given a value at all!
Try to run this program, and see what happens. Then, see if you can fix it!

Solve the first problem by moving the assignment statement for the variable to the beginning of the program.
Solve the second problem by giving the variable the value 50 before the variable is used.

```python
a = 10
print a

b = c
print b

c = 20
print c

d = a + b
print d

e = f + d
print e
```

When you are done, the program should print the following:

```
10
20
20
30
80
```