# Hotel Reservation System

A small object-oriented hotel reservation system built as a Python practice exercise. It demonstrates encapsulation, composition, association, properties, validation, state transitions, and object interaction.

## Requirements

- Python 3.10 or newer

## Run the scenario

From the project root:

```powershell
python -m hotel_reservation_system.main
```

Because the project uses a `src` layout, install it first when running from a fresh checkout:

```powershell
python -m pip install -e .
hotel-reservation-demo
```

The scenario creates five rooms, three guests, and reservations, then demonstrates pricing, cancellation, completion, room searches, an updated room price, and rejected invalid operations.

To run the tests:

```powershell
python -m pip install -e ".[test]"
python -m pytest
```

## Project layout

```text
src/
  hotel_reservation_system/
    main.py
    models/
      guest.py
      hotel.py
      reservation.py
      room.py
```
