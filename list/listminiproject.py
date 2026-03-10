# Mini Project - Shopping List
# Practicing lists by creating a small shopping list program.

shopping_list = []

# Adding items
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")

print("Shopping list:", shopping_list)

# Removing an item
shopping_list.remove("Bread")

print("Updated shopping list:", shopping_list)

# Display items one by one
print("Items to buy:")

for item in shopping_list:
    print("-", item)

