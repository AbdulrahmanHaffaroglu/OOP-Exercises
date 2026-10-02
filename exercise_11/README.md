# Mini Uber System

A small, in-memory ride-sharing simulation demonstrating object-oriented modeling of passengers, drivers, vehicles, rides, and payments. It does not connect to external services or persist data between runs.

## How It Works

Passengers register one or more payment methods and request rides by providing pickup and destination locations, passenger count, vehicle type, and distance. A request is accepted only when an available driver has a matching vehicle, and the passenger count must fit that vehicle.

Drivers register a vehicle, accept matching requests, and move rides through the lifecycle:

`Requested` -> `Accepted` -> `In_Progress` -> `Completed`

Requested or accepted rides can be cancelled. After a ride is completed, its passenger can pay using cash, a credit card, or a bank transfer. Partial payments are supported.

The fare is calculated as:

```text
base fare + (price per kilometer * distance)
```

| Vehicle type | Maximum passengers | Base fare | Price per kilometer |
| --- | ---: | ---: | ---: |
| `standart_car` | 4 | 50 | 15 |
| `premium_car` | 4 | 100 | 25 |
| `motorcycle` | 1 | 30 | 10 |

## Run the Demonstration

Requires Python 3.7 or newer.

From the project root, install the package and its test tools:

```bash
python -m pip install -e ".[test]"
```

Run the sample workflow:

```bash
python -m mini_uber_system.main
```

The demonstration creates passengers, drivers, vehicles, and payment methods; requests, accepts, starts, and completes rides; processes payments; and prints ride and history details.

## Run Tests

```bash
python -m pytest
```

Tests are grouped by domain under `tests/payments`, `tests/rides`, `tests/users`, and `tests/vehicles`.

## Project Layout

```text
src/mini_uber_system/
    main.py
    models/
        Payment_Methods/
        Rides/
        Users/
        Vehicles/
tests/
    payments/
    rides/
    users/
    vehicles/
```