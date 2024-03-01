# Newton's First Law of Motion
def newtons_first_law():
    print("Newton's First Law of Motion:")
    print("An object at rest stays at rest and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force.")

# Newton's Second Law of Motion
def newtons_second_law():
    print("\nNewton's Second Law of Motion:")
    print("The acceleration of an object as produced by a net force is directly proportional to the magnitude of the net force, in the same direction as the net force, and inversely proportional to the mass of the object.")

# Newton's Third Law of Motion
def newtons_third_law():
    print("\nNewton's Third Law of Motion:")
    print("For every action, there is an equal and opposite reaction.")

# Main function
def main():
    print("Welcome to the Newton's Laws of Motion Explorer!")
    choice = input("Enter '1' for Newton's First Law, '2' for Newton's Second Law, '3' for Newton's Third Law, or 'q' to quit: ")

    while choice != 'q':
        if choice == '1':
            newtons_first_law()
        elif choice == '2':
            newtons_second_law()
        elif choice == '3':
            newtons_third_law()
        else:
            print("Invalid choice. Please enter a valid option.")

        choice = input("\nEnter '1' for Newton's First Law, '2' for Newton's Second Law, '3' for Newton's Third Law, or 'q' to quit: ")

    print("Goodbye!")

if __name__ == "__main__":
    main()
