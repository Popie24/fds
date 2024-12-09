#include <iostream>
#define MAX 10 // Maximum size of the deque

class Deque {
private:
    int arr[MAX];
    int front;
    int rear;
    int size;

public:
    Deque() {
        front = -1;
        rear = 0;
        size = 0;
    }

    // Check if the deque is full
    bool isFull() {
        return size == MAX;
    }

    // Check if the deque is empty
    bool isEmpty() {
        return size == 0;
    }

    // Add element to the front of the deque
    void addFront(int item) {
        if (isFull()) {
            std::cout << "Deque is full. Cannot add to the front.\n";
            return;
        }
        if (front == -1) { // First element being added
            front = 0;
            rear = 0;
        } else if (front == 0) {
            front = MAX - 1; // Wrap around
        } else {
            front--;
        }
        arr[front] = item;
        size++;
        std::cout << "Added " << item << " to the front.\n";
    }

    // Add element to the rear of the deque
    void addRear(int item) {
        if (isFull()) {
            std::cout << "Deque is full. Cannot add to the rear.\n";
            return;
        }
        if (front == -1) { // First element being added
            front = 0;
            rear = 0;
        } else if (rear == MAX - 1) {
            rear = 0; // Wrap around
        } else {
            rear++;
        }
        arr[rear] = item;
        size++;
        std::cout << "Added " << item << " to the rear.\n";
    }

    // Delete element from the front of the deque
    void deleteFront() {
        if (isEmpty()) {
            std::cout << "Deque is empty. Cannot delete from the front.\n";
            return;
        }
        std::cout << "Removed " << arr[front] << " from the front.\n";
        if (front == rear) { // Single element left
            front = -1;
            rear = -1;
        } else if (front == MAX - 1) {
            front = 0; // Wrap around
        } else {
            front++;
        }
        size--;
    }

    // Delete element from the rear of the deque
    void deleteRear() {
        if (isEmpty()) {
            std::cout << "Deque is empty. Cannot delete from the rear.\n";
            return;
        }
        std::cout << "Removed " << arr[rear] << " from the rear.\n";
        if (front == rear) { // Single element left
            front = -1;
            rear = -1;
        } else if (rear == 0) {
            rear = MAX - 1; // Wrap around
        } else {
            rear--;
        }
        size--;
    }

    // Display the current contents of the deque
    void displayDeque() {
        if (isEmpty()) {
            std::cout << "Deque is empty.\n";
            return;
        }
        std::cout << "Deque elements: ";
        int i = front;
        while (true) {
            std::cout << arr[i] << " ";
            if (i == rear) break;
            i = (i + 1) % MAX;
        }
        std::cout << "\n";
    }
};

int main() {
    Deque deque;
    int choice, value;

    do {
        std::cout << "\n--- Deque Menu ---\n";
        std::cout << "1. Add Front\n";
        std::cout << "2. Add Rear\n";
        std::cout << "3. Delete Front\n";
        std::cout << "4. Delete Rear\n";
        std::cout << "5. Display Deque\n";
        std::cout << "6. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter value to add to the front: ";
                std::cin >> value;
                deque.addFront(value);
                break;
            case 2:
                std::cout << "Enter value to add to the rear: ";
                std::cin >> value;
                deque.addRear(value);
                break;
            case 3:
                deque.deleteFront();
                break;
            case 4:
                deque.deleteRear();
                break;
            case 5:
                deque.displayDeque();
                break;
            case 6:
                std::cout << "Exiting program.\n";
                break;
            default:
                std::cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 6);

    return 0;
}
