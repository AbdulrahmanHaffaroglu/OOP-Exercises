# Vehicle System

A small Python project for practicing object-oriented programming. It models cars, motorcycles, and trucks with registration, engine state, fuel, trips, and vehicle-specific behavior.

## Requirements

- Python 3.10 or newer
- pytest for the test suite

## Setup

Create and activate a virtual environment, then install the project with its test dependencies:

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

python -m pip install -e ".[test]"
```

## Usage

```python
from vehicle_system.models.car import Car
from vehicle_system.models.register import Register

car = Car("Toyota", "Corolla", 5)
Register.add(car)

car.refuel(20)
car.start_vehicle()
car.start_trip()
car.finish_trip()  # A car consumes 5% fuel per trip.
car.stop_vehicle()
car.show_details()
```

The other models are available from:

```python
from vehicle_system.models.motorcycle import Motorcycle
from vehicle_system.models.truck import Truck
```

Their trips consume `3%` and `10%` fuel respectively. A vehicle must be registered and have fuel before it can start. Vehicles cannot be refueled while running or on a trip.

## Run the Scenario

From the project root, run the scenario in `main.py` with:

```bash
python -m vehicle_system.main
```

This registers one car, motorcycle, and truck, runs a trip for each vehicle, and prints their final details.

## Run Tests

```bash
python -m pytest
```

The tests are in the `tests/` directory and cover creation, registration, lifecycle transitions, fuel behavior, details, and invalid operations.

## Project Layout

```text
src/vehicle_system/
    models/
        car.py
        engine.py
        motorcycle.py
        register.py
        truck.py
        vehicle.py
    utils/
tests/
```
