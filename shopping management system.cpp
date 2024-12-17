#include <iostream>
using namespace std;

// Define a Product structure to represent items in the shop
struct Product {
    string name;
    float price;
};

// Define a Shopping structure to manage the items and the total cost
struct Shopping {
    Product shopping[10];  // Maximum 10 items in the shopping list
    int quantities[10];    // Store quantities of each product
    int itemCount;

    Shopping() {
        itemCount = 0;
    }

    void addItem(Product p, int quantity) {
        if (itemCount < 10) {
            shopping[itemCount] = p;
            quantities[itemCount] = quantity;
            itemCount++;
        } else {
            cout << "Shopping list is full!" << endl;
        }
    }

    void displayShopping() {
        if (itemCount == 0) {
            cout << "Your shopping list is empty." << endl;
        } else {
            float total = 0;
            cout << "\nItems in your shopping list:\n";
            for (int i = 0; i < itemCount; i++) {
                cout << shopping[i].name << " (x" << quantities[i] 
                     << ") - $" << shopping[i].price 
                     << " each, Total: $" << shopping[i].price * quantities[i] << endl;
                total += shopping[i].price * quantities[i];
            }
            cout << "Total: $" << total << endl;
        }
    }

    float calculateTotal() {
        float total = 0;
        for (int i = 0; i < itemCount; i++) {
            total += shopping[i].price * quantities[i];
        }
        return total;
    }
};

int main() {
    // Creating some sample products
    Product p1 = {"Laptop", 800.00};
    Product p2 = {"Smartphone", 600.00};
    Product p3 = {"Headphones", 50.00};
    Product p4 = {"Smart Watch", 120.00};

    // Creating a shopping object
    Shopping shoppingList;

    int choice;
    do {
        // Display available products and menu options
        cout << "\n   Hubaal Electronic Online Shop!\n";
        cout << "1. View Products\n";
        cout << "2. Add Product to Shopping List\n";
        cout << "3. View Shopping List\n";
        cout << "4. Checkout\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                // Display available products
                cout << "\nAvailable Products:\n";
                cout << "1. " << p1.name << " - $" << p1.price << endl;
                cout << "2. " << p2.name << " - $" << p2.price << endl;
                cout << "3. " << p3.name << " - $" << p3.price << endl;
                cout << "4. " << p4.name << " - $" << p4.price << endl;
                break;
            }
            case 2: {
                // Add product to the shopping list
                int productChoice, quantity;
                cout << "\nEnter product number to add to shopping list (1-4): ";
                cin >> productChoice;
                cout << "Enter quantity: ";
                cin >> quantity;

                switch (productChoice) {
                    case 1:
                        shoppingList.addItem(p1, quantity);
                        cout << quantity << " " << p1.name << "(s) added to the shopping list.\n";
                        break;
                    case 2:
                        shoppingList.addItem(p2, quantity);
                        cout << quantity << " " << p2.name << "(s) added to the shopping list.\n";
                        break;
                    case 3:
                        shoppingList.addItem(p3, quantity);
                        cout << quantity << " " << p3.name << "(s) added to the shopping list.\n";
                        break;
                    case 4:
                        shoppingList.addItem(p4, quantity);
                        cout << quantity << " " << p4.name << "(s) added to the shopping list.\n";
                        break;
                    default:
                        cout << "Invalid product number!\n";
                }
                break;
            }
            case 3: {
                // View shopping list
                shoppingList.displayShopping();
                break;
            }
            case 4: {
                // Checkout and calculate total
                float total = shoppingList.calculateTotal();
                cout << "\nYour total is: $" << total << endl;
                cout << "Thank you for shopping!\n";
                return 0;
            }
            case 5: {
                cout << "Exiting the shop.\n";
                break;
            }
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 5);

    return 0;
}
