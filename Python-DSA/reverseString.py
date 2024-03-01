class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

def reverse_string(string):
    stack = Stack()
    reversed_string = ""
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

def main():
    string = input("Enter a string to reverse: ")
    reversed_str = reverse_string(string)
    print("Reversed string:", reversed_str)

if __name__ == "__main__":
    main()
