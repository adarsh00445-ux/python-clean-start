# Lists Practice - Adarsh


# Creating a list
numbers = [10, 20, 30, 40]

print("Original list:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Adding element
numbers.append(50)
print("After append:", numbers)

# Removing element
numbers.remove(20)
print("After removing 20:", numbers)

# Length of list
print("Length of list:", len(numbers))

# Loop through list
print("Looping through list:")

for num in numbers:
    print(num)
