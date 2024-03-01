class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def semiconductor_simulation():
    print("Simulating a simple semiconductor circuit...")
    print("Voltage source connected to a diode -> Diode -> Resistor -> Ground")

    # Creating a linked list representing the circuit
    circuit = LinkedList()
    circuit.append("Voltage Source")
    circuit.append("Diode")
    circuit.append("Resistor")
    circuit.append("Ground")

    print("Circuit components:")
    circuit.display()

def main():
    print("Welcome to the Python DSA and Semiconductor Simulator!")
    choice = input("Enter '1' to learn about data structures and algorithms, or '2' to simulate a semiconductor circuit: ")

    if choice == '1':
        print("Let's learn about data structures and algorithms!")
        # You can add your DSA topics and explanations here.
    elif choice == '2':
        semiconductor_simulation()
    else:
        print("Invalid choice. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()
