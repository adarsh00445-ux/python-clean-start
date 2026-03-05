# STRING PRACTICE
# First time I thought strings behave like lists, but they are immutable.
# I practiced again to understand methods properly.


text = "DevOps Engineer"

print("Original text:", text)


# 1. Length
print("Length:", len(text))


# 2. Upper and Lower
print("Upper:", text.upper())
print("Lower:", text.lower())


# 3. Replace
new_text = text.replace("Engineer", "Student")
print("After replace:", new_text)


# 4. Split
words = text.split(" ")
print("Split into words:", words)


# 5. String slicing
print("First 6 characters:", text[:6])
print("Last word:", text[7:])


# Important:
# Strings cannot be modified directly.
# I tried changing a character like text[0] = 'X' but it gave error.
# That is because strings are immutable.