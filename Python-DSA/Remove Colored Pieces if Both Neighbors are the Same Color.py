def remove_neighbors_same_color(s):
    if not s:
        return 0
    
    count = 0
    stack = []

    for color in s:
        if stack and color == stack[-1]:
            stack.pop()
            count += 2
        else:
            stack.append(color)
    
    return count

def main():
    s = input("Enter the colored pieces sequence: ")
    removed_count = remove_neighbors_same_color(s)
    print("Total number of removed pieces:", removed_count)

if __name__ == "__main__":
    main()
