# The function len can be used to find out the length of a string, among other things.
# The function returns the number of characters in a string.

# Some examples of how this works:

# word = "abcd"
# print(len(word))
#
# print(len("hi there"))
#
# word2 = "howdydoody"
# length = len(word2)
# print(length)
#
# empty_string = ""
# length = len(empty_string)
# print(length)

# 4
# 8
# 10
# 0

# Please write a program which asks the user for a word and then prints out the
# number of characters, if there was more than one typed in.

# Examples of expected behaviour:

# Please type in a word: hey
# There are 3 letters in the word hey
# Thank you!

# Please type in a word: banana
# There are 6 letters in the word banana
# Thank you!

# Please type in a word: b
# Thank you!

# Write your solution here
word = input("Please type in a word: ")
length = len(word)

if length > 1:
    print(f"There are {length} letters in the word {word}")

print("Thank you!")
