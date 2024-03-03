def reverse_stack(stack):
    # Create an empty temporary stack
    temp_stack = []

    # Move all elements from the original stack to the temporary stack
    while stack:
        temp_stack.append(stack.pop())

    # Move all elements back to the original stack (reversing them)
    while temp_stack:
        stack.append(temp_stack.pop())

# Example usage:
stack = [1, 2, 3, 4, 5]
print("Original Stack:", stack)
reverse_stack(stack)
print("Reversed Stack:", stack)
