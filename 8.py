class Node:
    """Class to represent a node in the linked list."""
    def __init__(self, name):
        self.name = name
        self.next = None

class IceCreamSet:
    """Class to represent a set of students using a singly linked list."""
    def __init__(self):
        self.head = None

    def add_student(self, name):
        """Add a new student to the set."""
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        """Convert linked list to a Python list for easier manipulation."""
        students = []
        current = self.head
        while current:
            students.append(current.name)
            current = current.next
        return students

def compute_sets(set_a, set_b):
    """Compute and display the required sets."""
    # Convert linked lists to sets for easier computation
    set_a_list = set_a.to_list()
    set_b_list = set_b.to_list()
    
    set_a_set = set(set_a_list)
    set_b_set = set(set_b_list)

    # a) Set of students who like both vanilla and butterscotch
    both = set_a_set.intersection(set_b_set)
    print("Students who like both Vanilla and Butterscotch:", both)

    # b) Set of students who like either vanilla or butterscotch, but not both
    either = set_a_set.symmetric_difference(set_b_set)
    print("Students who like either Vanilla or Butterscotch or not both:", either)

    # c) Number of students who like neither vanilla nor butterscotch
    total_students = set_a_set.union(set_b_set)
    all_students = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"}  # Example total students
    neither = all_students - total_students
    print("Number of students who like neither Vanilla nor Butterscotch:", len(neither))
    print("Students who like neither:", neither)

# Example usage
if __name__ == "__main__":
    # Create sets for Vanilla and Butterscotch lovers
    vanilla_set = IceCreamSet()
    butterscotch_set = IceCreamSet()

    # Add students to Vanilla set
    vanilla_set.add_student("Alice")
    vanilla_set.add_student("Bob")
    vanilla_set.add_student("Charlie")

    # Add students to Butterscotch set
    butterscotch_set.add_student("Charlie")
    butterscotch_set.add_student("David")
    butterscotch_set.add_student("Eve")

    # Compute and display the required sets
    compute_sets(vanilla_set, butterscotch_set)
