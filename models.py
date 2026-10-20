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
        raise NotImplementedError

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return the items in the given category."""
        raise NotImplementedError


class Order:
    """A single transaction grouping selected items. Starts empty."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a selected item to the order."""
        raise NotImplementedError

    def compute_total(self) -> float:
        """Return the sum of item prices, rounded to 2 decimals."""
        raise NotImplementedError


class Customer:
    """A user whose purchase history is used to verify they are real."""

    def __init__(self, name: str, purchase_history: list[Order] | None = None) -> None:
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def is_verified(self) -> bool:
        """Return True if the customer has at least one past order."""
        raise NotImplementedError
