import pytest

from models import Customer, FoodItem, Menu, Order


@pytest.fixture
def menu() -> Menu:
    """A small menu with items in three categories."""
    return Menu([
        FoodItem("Spicy Burger", 8.99, "Entrees", 4.5),
        FoodItem("Large Soda", 2.49, "Drinks", 3.8),
        FoodItem("Chocolate Cake", 4.25, "Desserts", 4.7),
        FoodItem("Iced Tea", 1.99, "Drinks", 4.1),
    ])


def names(items: list[FoodItem]) -> list[str]:
    return [item.name for item in items]


# --- Order totals ---

# A $10 burger and a $5 soda should total $15.
def test_calculate_total_with_multiple_items():
    order = Order()
    order.add_item(FoodItem("Burger", 10.00, "Entrees", 4.0))
    order.add_item(FoodItem("Soda", 5.00, "Drinks", 3.5))
    assert order.compute_total() == 15.00


# An order with nothing in it should total $0.00 (as a float), not crash.
def test_order_total_is_zero_when_empty():
    total = Order().compute_total()
    assert total == 0.0
    assert isinstance(total, float)


# Adding the same item twice should count its price twice.
def test_order_total_counts_duplicate_items():
    soda = FoodItem("Soda", 2.49, "Drinks", 3.5)
    order = Order()
    order.add_item(soda)
    order.add_item(soda)
    assert order.compute_total() == 4.98


# Totals should be rounded to 2 decimals, hiding float error like 0.1 + 0.2.
def test_order_total_rounds_to_two_decimals():
    order = Order()
    order.add_item(FoodItem("A", 0.10, "Test", 0))
    order.add_item(FoodItem("B", 0.20, "Test", 0))
    assert order.compute_total() == 0.30


# --- Filtering ---

# Filtering by "Drinks" should return only drink items.
def test_filter_by_category_returns_only_matching_items(menu):
    assert names(menu.filter_by_category("Drinks")) == ["Large Soda", "Iced Tea"]


# Category matching should ignore case.
def test_filter_by_category_is_case_insensitive(menu):
    assert names(menu.filter_by_category("drinks")) == ["Large Soda", "Iced Tea"]


# A category with no items should return an empty list, not raise.
def test_filter_by_unknown_category_returns_empty_list(menu):
    assert menu.filter_by_category("Pizza") == []


# --- Sorting ---

# Sorting by price should list the cheapest item first by default.
def test_sort_by_price_cheapest_first(menu):
    assert names(menu.sort_by_price()) == ["Iced Tea", "Large Soda", "Chocolate Cake", "Spicy Burger"]


# Sorting by popularity should list the highest-rated item first by default.
def test_sort_by_popularity_most_popular_first(menu):
    assert names(menu.sort_by_popularity()) == ["Chocolate Cake", "Spicy Burger", "Iced Tea", "Large Soda"]


# Sorting should return a new list and leave the menu's own order unchanged.
def test_sorting_does_not_change_menu(menu):
    original = names(menu.items)
    menu.sort_by_price(descending=True)
    assert names(menu.items) == original


# --- Customer verification ---

# A customer with no purchase history should not be verified.
def test_new_customer_is_not_verified():
    assert Customer("Alex").is_verified() is False


# A customer with at least one past order should be verified.
def test_customer_with_past_order_is_verified():
    assert Customer("Sam", [Order()]).is_verified() is True
