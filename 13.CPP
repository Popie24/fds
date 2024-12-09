#include <iostream>
#define MAX 5 // Maximum number of orders

class PizzaParlor {
private:
    int orders[MAX];
    int front;
    int rear;
    int size;

public:
    PizzaParlor() {
        front = -1;
        rear = -1;
        size = 0;
    }

    // Check if the queue is full
    bool isFull() {
        return size == MAX;
    }

    // Check if the queue is empty
    bool isEmpty() {
        return size == 0;
    }

    // Place a new order in the queue
    void placeOrder(int order) {
        if (isFull()) {
            std::cout << "The order queue is full. Cannot accept more orders.\n";
            return;
        }
        if (isEmpty()) { // First order being placed
            front = 0;
        }
        rear = (rear + 1) % MAX; // Circular increment
        orders[rear] = order;
        size++;
        std::cout << "Order #" << order << " placed successfully.\n";
    }

    // Serve an order (remove it from the queue)
    void serveOrder() {
        if (isEmpty()) {
            std::cout << "No orders to serve. The queue is empty.\n";
            return;
        }
        std::cout << "Order #" << orders[front] << " served.\n";
        front = (front + 1) % MAX; // Circular increment
        size--;
        if (size == 0) { // Reset front and rear when queue becomes empty
            front = -1;
            rear = -1;
        }
    }

    // Display the current queue of orders
    void displayOrders() {
        if (isEmpty()) {
            std::cout << "No orders in the queue.\n";
            return;
        }
        std::cout << "Current orders in the queue: ";
        for (int i = 0, idx = front; i < size; ++i) {
            std::cout << orders[idx] << " ";
            idx = (idx + 1) % MAX; // Circular increment
        }
        std::cout << "\n";
    }
};

int main() {
    PizzaParlor pizzaParlor;
    int choice, order;

    do {
        std::cout << "\n--- Pizza Parlor Menu ---\n";
        std::cout << "1. Place Order\n";
        std::cout << "2. Serve Order\n";
        std::cout << "3. Display Orders\n";
        std::cout << "4. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter order number: ";
                std::cin >> order;
                pizzaParlor.placeOrder(order);
                break;

            case 2:
                pizzaParlor.serveOrder();
                break;

            case 3:
                pizzaParlor.displayOrders();
                break;

            case 4:
                std::cout << "Exiting program.\n";
                break;

            default:
                std::cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 4);

    return 0;
}
