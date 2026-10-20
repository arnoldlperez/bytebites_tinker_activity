Client Feature Request
We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

## Candidate Classes
- Customer
- FoodItem
- Menu
- Order

## Class Diagram
See [bytebites_classes.puml](bytebites_classes.puml) (UML, PlantUML format).

Assumptions not stated in the feature request:
- `Customer.is_verified()` returns true when the customer has at least one past order. The spec says purchase history is used for verification but not how.
- `add_item()` on Menu and Order is implied (a collection needs a way to add items) but not explicitly requested.
- Order does not reference its Customer; the spec doesn't require it.
- Category is a plain string attribute, not a separate class.