# STRING MINI PROJECT Adarsh 
# Date: Practice for string topic
# I created this small program to practice Python string operations.
# At first I only understood upper() and lower(), but while practicing
# I realized there are many useful string functions.
# So I wrote this small analyzer to understand strings better.


# Taking input from the user
text = input("Adarsh's String Analyzer - Enter a sentence: ")


# Finding the length of the sentence
print("Total characters in sentence:", len(text))


# Converting text to uppercase
print("Uppercase version:", text.upper())


# Converting text to lowercase
print("Lowercase version:", text.lower())


# Splitting sentence into words
words = text.split()
print("Number of words:", len(words))


# Counting vowels in the sentence
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)


# Checking if sentence starts with capital letter
if text[0].isupper():
    print("Sentence starts with a capital letter")
else:
    print("Sentence does not start with a capital letter")


# Reversing the string
reversed_text = text[::-1]
print("Reversed sentence:", reversed_text)


# If we want to modify a string, Python actually creates a new string.


print("String analysis completed by Adarsh.")