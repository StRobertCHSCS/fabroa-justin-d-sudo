# 2_7_3_LoopPatterns.py Solution

word = input("Enter a word: ")

#initialize the index variable
i = 0

# get the length of the word
word_len = len(word)

# initialize boolean variable to flag if x is found
x_found = False

# loop through the word searching for x
while i < word_len and not(x_found):
    if word[i] == 'x':
        # x found
        x_found = True
        print("x found at location", i)
    i = i + 1


if not(x_found):
    print("x not found")