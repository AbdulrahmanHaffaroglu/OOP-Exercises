# Ride-Sharing Platform Backend

## Project Overview

This project defines the functional and business requirements for a simulated ride-sharing platform backend. The platform coordinates passengers, drivers, vehicles, ride requests, pricing, payments, and ride histories through a defined set of workflows and state transitions.

The implementation is expected to model these interacting responsibilities with a maintainable object-oriented design. The requirements specify system behavior without prescribing a class structure, inheritance hierarchy, or particular use of composition and polymorphism.

---

## 1. Business Context

The system supports a ride-sharing service in which passengers request transportation and drivers accept and complete rides.

A passenger provides a pickup location and destination. The system calculates the fare, identifies an available driver with a compatible vehicle, and manages the ride through completion or cancellation.

The application also handles:

* Different vehicle types
* Different ride types
* Different payment methods
* Ride pricing
* Driver availability
* Ride status
* Passenger and driver information
* Ride history

The scope is limited to a Python simulation. A user interface, database, GPS, map API, and live payment provider are out of scope.

All distance and payment operations are simulated.

---

## 2. User Roles

The system has two types of users:

### Passenger

A passenger profile includes:

* ID
* Name
* Phone number
* Ride history
* Payment methods

A passenger must be able to:

* Request a ride
* Cancel a ride when allowed
* View the current ride
* View previous rides
* Pay for a completed ride

---

### Driver

A driver profile includes:

* ID
* Name
* Phone number
* Vehicle
* Availability status
* Ride history

A driver must be able to:

* Become available
* Become unavailable
* Accept a ride
* Start a ride
* Complete a ride
* View previous rides

A driver with an active ride cannot accept another ride.

---

## 3. Vehicle Types and Rates

The platform supports three vehicle types:

### Standard Car

* Maximum passengers: `4`
* Base fare: `50 TL`
* Price per kilometer: `15 TL`

### Premium Car

* Maximum passengers: `4`
* Base fare: `100 TL`
* Price per kilometer: `25 TL`

### Motorcycle

* Maximum passengers: `1`
* Base fare: `30 TL`
* Price per kilometer: `10 TL`

The vehicle type affects the ride price.

For example, a 10 km ride with a standard car:

```text
50 + (10 × 15)
= 200 TL
```

A 10 km ride with a premium car:

```text
100 + (10 × 25)
= 350 TL
```

---

## 4. Ride Requests

A ride request must include:

* Pickup location
* Destination
* Number of passengers
* Requested vehicle type

The system creates a ride request containing these details.

Example:

```text
Passenger: Abdulrahman
Pickup: Istanbul Airport
Destination: Taksim
Passengers: 2
Vehicle type: Standard
```

For this simulation, the distance is supplied by the calling program or test.

Geographical distance calculation is out of scope.

For example:

```text
Distance: 25 km
```

can simply be provided when creating the ride request.

---

## 5. Passenger Capacity Validation

The selected vehicle must have sufficient capacity for the requested number of passengers.

For example:

```text
Motorcycle + 1 passenger    Valid
Motorcycle + 2 passengers   Invalid

Standard Car + 4 passengers Valid
Standard Car + 5 passengers Invalid
```

Requests that exceed vehicle capacity must be rejected.

---

## 6. Driver Matching

When a passenger requests a ride, the system searches for an available driver with a compatible vehicle.

For example:

```text
Drivers:

Ali       → Standard Car → Available
Mehmet    → Premium Car → Busy
Ahmet     → Motorcycle   → Available
```

A passenger requesting a Premium Car should not receive Ali or Ahmet.

A passenger requesting a Standard Car should be able to receive Ali.

If no suitable driver is available, the request remains unassigned. Assignment does not imply driver acceptance.

---

## 7. Ride Lifecycle

After a suitable driver is assigned, the driver may accept the ride.

The ride then moves through these states:

```text
REQUESTED
    ↓
ACCEPTED
    ↓
IN_PROGRESS
    ↓
COMPLETED
```

A ride can also become:

```text
REQUESTED → CANCELLED
ACCEPTED  → CANCELLED
```

But once the ride has started:

```text
IN_PROGRESS → CANCELLED (not permitted)
```

Cancellation after the ride has started is not allowed.

---

## 8. Starting a Ride

A driver may start a ride only after accepting it.

For example:

```text
Ride #1001
Status: ACCEPTED

Driver starts ride

Status: IN_PROGRESS
```

The system should not allow:

```text
REQUESTED → IN_PROGRESS (not permitted)
```

The driver must accept the ride first.

---

## 9. Completing a Ride

When the passenger reaches the destination, the driver completes the ride.

The ride becomes:

```text
COMPLETED
```

The driver becomes available again.

For example:

```text
Before:
Driver → Busy

Complete ride

After:
Driver → Available
```

Completed rides remain in both the passenger's and driver's ride histories.

---

## 10. Fare Calculation

The ride price is calculated based on:

* Vehicle type
* Distance

Use:

```text
final price = base fare + (distance × price per km)
```

For example:

```text
Standard Car
Distance: 20 km

50 + (20 × 15)
= 350 TL
```

The fare is determined when the ride is created.

Once the ride has started, its base fare must remain unchanged.

---

## 11. Ride Categories

The application supports three ride types:

### Standard Ride

Uses the normal vehicle pricing.

### Premium Ride

Requires a Premium Car.

It uses Premium Car pricing.

### Motorcycle Ride

Requires a Motorcycle.

It uses Motorcycle pricing.

The ride type determines which vehicles are appropriate and how the ride is priced.

---

## 12. Payment Methods

The passenger must pay for a completed ride.

The application supports:

* Credit Card
* Cash
* Bank Transfer

Each payment method follows its own simulated processing behavior:

For example:

```text
Credit Card
→ Process card payment
→ Payment successful

Cash
→ Record cash payment
→ Payment successful

Bank Transfer
→ Verify transfer
→ Payment successful
```

All payment operations are simulated.

No real financial services or payment processing are in scope.

---

## 13. Payment Controls

The system must reject the following:

* Paying for a ride that hasn't been completed.
* Paying for a cancelled ride.
* Paying twice for the same ride.
* Paying zero or negative amounts.

Example:

```text
Ride: IN_PROGRESS

Passenger attempts payment

→ Rejected
```

After:

```text
Ride: COMPLETED
```

payment becomes possible.

---

## 14. Ride Cancellation

Passengers may cancel a ride while it is in either of these states:

```text
REQUESTED
```

or:

```text
ACCEPTED
```

Cancellation is not permitted after the ride reaches:

```text
IN_PROGRESS
```

the passenger cannot cancel it.

If an accepted ride is cancelled:

```text
Ride → CANCELLED
Driver → Available
```

Cancelled rides remain in the passenger's history.

---

## 15. Driver Availability

Each driver has an availability state:

For example:

```text
AVAILABLE
BUSY
OFFLINE
```

A driver may be assigned a ride only when:

```text
AVAILABLE
```

A driver who is:

```text
BUSY
```

cannot accept another ride.

A driver who is:

```text
OFFLINE
```

cannot be assigned a ride.

When a completed ride or cancelled accepted ride releases the driver, the driver returns to the available state.

---

## 16. Ride History

Passengers and drivers can access their respective ride histories.

For a passenger:

```text
Ride #1001
Standard Car
20 km
350 TL
COMPLETED

Ride #1007
Premium Car
15 km
475 TL
CANCELLED
```

For a driver:

```text
Ride #1001
Passenger: Abdulrahman
20 km
350 TL
COMPLETED
```

The same ride is represented consistently in both histories.

---

## 17. Ride Summary

The system provides a summary containing the relevant ride, participant, vehicle, fare, and payment details.

For example:

```text
Ride #1001

Passenger: Abdulrahman
Driver: Ali

Vehicle: Standard Car
Pickup: Istanbul Airport
Destination: Taksim

Passengers: 2
Distance: 25 km

Price: 425 TL

Payment: Credit Card
Payment Status: Paid

Ride Status: COMPLETED
```

---

## 18. Validation and Error Handling

The system must reject invalid operations, including:

```text
Passenger requests a ride for 5 people using a motorcycle
        Rejected

Passenger requests Premium but no Premium driver is available
        Rejected

Unavailable driver accepts a ride
        Rejected

Driver accepts two rides simultaneously
        Rejected

Driver starts a ride that wasn't accepted
        Rejected

Passenger cancels an IN_PROGRESS ride
        Rejected

Driver completes a ride that hasn't started
        Rejected

Passenger pays before the ride is completed
        Rejected

Passenger pays for the same ride twice
        Rejected

Passenger tries to use another passenger's ride
        Rejected
```

These cases must be handled explicitly so that invalid operations cannot leave the system in an inconsistent state.

---

## 19. End-to-End Ride Workflow

A normal ride could go through the following workflow:

```text
Passenger requests ride
        ↓
System validates passenger count
        ↓
System calculates price
        ↓
System searches for suitable available driver
        ↓
Driver is assigned
        ↓
Driver accepts
        ↓
Ride becomes ACCEPTED
        ↓
Driver starts ride
        ↓
Ride becomes IN_PROGRESS
        ↓
Driver reaches destination
        ↓
Driver completes ride
        ↓
Ride becomes COMPLETED
        ↓
Driver becomes AVAILABLE
        ↓
Passenger pays
        ↓
Payment succeeds
        ↓
Ride appears in both histories
```

---

## 20. Operational Acceptance Scenario

The implementation must support an end-to-end scenario that performs the following operations:

```text
Create passengers
Create drivers
Create different vehicles
Register drivers with vehicles

Make drivers available

Passenger requests a ride

System finds an appropriate driver

Driver accepts

Driver starts the ride

Driver completes the ride

Passenger pays

Display the completed ride

Display passenger history

Display driver history
```

Invalid operations must also be testable and rejected with appropriate outcomes.

---
