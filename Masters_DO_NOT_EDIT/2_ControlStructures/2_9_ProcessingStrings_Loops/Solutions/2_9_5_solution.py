word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()

# using a loop, we can walk backwards from the end of both strings and compare the last 3 characters
match = True

for i in range(-1, -4, -1):
    if word1[i] != word2 [i]:
        match = False

print(match)

# technically you don't need a loop, you can just use indexing
print(word1[-3:]) == word2[-3:]



