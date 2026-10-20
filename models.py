# ByteBites models
#
# Customer - a user with a name and purchase history; history is used to verify they are real.
# FoodItem - an item for sale with a name, price, category, and popularity rating.
# Menu     - the full collection of food items; can be filtered by category.
# Order    - a single transaction grouping selected items and computing the total cost.

from __future__ import annotations


class FoodItem:
    """A single item for sale."""

    def __init__(self, name: str, price: float, category: str, popularity_rating: float) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """The full collection of food items."""

    def __init__(self, items: list[FoodItem] | None = None) -> None:
        self.items = items if items is not None else []

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the menu."""
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return the items in the given category (case-insensitive)."""
        target = category.lower()
        return [item for item in self.items if item.category.lower() == target]

    def sort_by_price(self, descending: bool = False) -> list[FoodItem]:
        """Return the items sorted by price, cheapest first by default."""
        return sorted(self.items, key=lambda item: item.price, reverse=descending)

    def sort_by_popularity(self, descending: bool = True) -> list[FoodItem]:
        """Return the items sorted by popularity rating, most popular first by default."""
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=descending)


class Order:
    """A single transaction grouping selected items. Starts empty."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a selected item to the order."""
        self.items.append(item)

    def compute_total(self) -> float:
        """Return the sum of item prices, rounded to 2 decimals."""
        return round(sum((item.price for item in self.items), 0.0), 2)


class Customer:
    """A user whose purchase history is used to verify they are real."""

    def __init__(self, name: str, purchase_history: list[Order] | None = None) -> None:
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def is_verified(self) -> bool:
        """Return True if the customer has at least one past order."""
        return len(self.purchase_history) > 0
