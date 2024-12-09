class Node:
    """Class to represent a node in the linked list."""
    def __init__(self, prn, name):
        self.prn = prn
        self.name = name
        self.next = None

class Club:
    """Class to represent the Pinnacle Club using a singly linked list."""
    def __init__(self):
        self.head = None
        self.tail = None

    def add_member(self, prn, name):
        """Add a new member to the club."""
        new_node = Node(prn, name)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_member(self, prn):
        """Delete a member from the club by PRN."""
        current = self.head
        previous = None
        while current is not None:
            if current.prn == prn:
                if previous is None:  # Deleting the head
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        print(f"Member with PRN {prn} not found.")

    def compute_total_members(self):
        """Compute the total number of members in the club."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def display_members(self):
        """Display all members of the club."""
        current = self.head
        if current is None:
            print("No members in the club.")
            return
        print("Members of the Pinnacle Club:")
        while current is not None:
            print(f"PRN: {current.prn}, Name: {current.name}")
            current = current.next

    def concatenate(self, other_club):
        """Concatenate another club's members to this club."""
        if self.head is None:
            self.head = other_club.head
        else:
            self.tail.next = other_club.head
        if other_club.tail is not None:
            self.tail = other_club.tail

# Example usage
if __name__ == "__main__":
    # Create two clubs for two divisions
    club_a = Club()
    club_b = Club()

    # Add members to club A
    club_a.add_member("123", "Alice")
    club_a.add_member("124", "Bob")

    # Add members to club B
    club_b.add_member("125", "Charlie")
    club_b.add_member("126", "David")

    # Display members of both clubs
    print("Club A:")
    club_a.display_members()
    print("\nClub B:")
    club_b.display_members()

    # Concatenate club B to club A
    club_a.concatenate(club_b)

    # Display members after concatenation
    print("\nMembers after concatenation:")
    club_a.display_members()

    # Compute total members
    total_members = club_a.compute_total_members()
    print(f"\nTotal members in the club: {total_members}")

    # Delete a member
    club_a.delete_member("124")
    print("\nMembers after deleting PRN 124:")
    club_a.display_members()
