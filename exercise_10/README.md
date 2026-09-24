# Restaurant Order System

An object-oriented Python restaurant ordering system. This README is the durable project documentation; `src/restaurant_order_system/main.py` contains the runnable example scenario.

## System Overview

Customers browse a restaurant menu, create orders, select dish extras or drink sizes, apply discounts, pay, and track order progress. Staff manage the order lifecycle from confirmation through delivery.

The project is intentionally an in-memory OOP exercise. It does not use a database, web API, user interface, or real payment provider.

## Requirements

### Menu

- Every menu item has an ID, name, description, price, and availability.
- Available items can be added to orders; unavailable items cannot.
- The menu supports listing items and looking up an item by ID.

### Menu item types

- `MainDish` has a base price and optional `Option` extras.
- `Drink` has required size options, with each size carrying its own price.
- `Dessert` has a fixed price and does not accept options.

### Orders

- A customer can create multiple orders.
- An order supports adding, removing, and changing item quantities.
- Each order line stores the selected options, so different configurations are priced independently.
- Quantities must be greater than zero.
- Paid orders cannot be modified.
- Orders expose subtotal, discount, final total, payment status, and lifecycle status.

### Order lifecycle

```text
PENDING -> CONFIRMED -> PREPARING -> READY -> DELIVERED
```

- Payment is required before confirmation.
- An order can be cancelled while `Pending` or `Confirmed`.
- An order cannot be cancelled after preparation begins.
- Invalid status transitions are rejected.

### Payments

The system simulates cash, credit-card, and bank-transfer payments.

- An order cannot be paid twice.
- Empty, zero-value, and cancelled orders cannot be paid.
- Payment failures leave the order unpaid and pending.
- A successful payment stores the payment method and freezes the final total.

### Discounts

- `PercentageDiscount` supports percentages from greater than 0 through 100.
- `FixedDiscount` supports positive fixed amounts.
- Discounts are applied before payment.
- The final total cannot become negative.
- A discount cannot be changed after payment.

## Architecture

- `models/the_menu/`: menu items, options, and menu lookup.
- `models/orders/`: order ownership, order lines, pricing, summaries, and cancellation.
- `models/payment/`: interchangeable payment strategies.
- `models/customer.py`: customer-facing order and payment operations.
- `models/restaurant.py`: menu access and staff-controlled status transitions.
- `utils/discounts.py`: reusable discount strategies.

## Features

- Menu management and item lookup
- Main dishes with optional extras
- Drinks with required, priced sizes
- Desserts with fixed prices
- Option-aware order lines and totals
- Quantity changes and availability validation
- Percentage and fixed discounts
- Cash, credit-card, and bank-transfer payment simulations
- Payment and final-total tracking
- Order cancellation and staff status transitions
- Order history and summaries

## Setup

Create a virtual environment and install the test dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .[test]
```

## Test

Run the complete test suite:

```powershell
python -m pytest -q
```

## Example

```python
from restaurant_order_system.models.customer import Customer
from restaurant_order_system.models.payment.cash import Cash
from restaurant_order_system.models.the_menu.desserts import Dessert
from restaurant_order_system.utils.discounts import PercentageDiscount

customer = Customer("Abdulrahman", "contact")
order = customer.create_order([Dessert("Cake", "", 120, True)])
customer.apply_discount(order, PercentageDiscount(10))
customer.pay_order(order, Cash(customer))
```

## Complete Scenario

Run the built-in workflow from the project root:

```powershell
python -m restaurant_order_system.main
```

The scenario creates a menu, orders a burger with extras, selects a large drink, adds dessert, applies a percentage discount, pays by credit card, and moves the order through delivery.

## Tests

The tests follow the supplied exercise test template and cover normal behavior, properties, invalid inputs, edge cases, discounts, payments, options, summaries, and status transitions.
