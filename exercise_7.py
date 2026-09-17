'''
Build a Hotel Reservation System.

The goal of this exercise is to practice:

- Encapsulation
- Composition
- Association
- Properties
- Object interaction
- Separation of responsibilities
- State management
- Inheritance
- Method overriding

--------------------------------------------------
CLASSES
--------------------------------------------------

The system must support four main classes:

1. Hotel
2. Room
3. Guest
4. Reservation


--------------------------------------------------
ROOM
--------------------------------------------------

Every Room has:

- Room number
- Room type
- Price per night
- Availability status

Supported room types:

- Single
- Double
- Suite

A Room must:

- Have a positive room number.
- Have a non-negative price.
- Have a valid room type.
- Be either available or unavailable.
- Become unavailable when reserved.
- Become available when its active reservation is cancelled.


--------------------------------------------------
GUEST
--------------------------------------------------

Every Guest has:

- Guest ID
- Name
- Email
- A collection of reservations

A Guest:

- Can have multiple reservations.
- Should keep track of their reservations.


--------------------------------------------------
RESERVATION
--------------------------------------------------

Every Reservation represents:

- A Guest
- A Room
- Check-in date
- Check-out date
- Reservation status

Supported statuses:

- Confirmed
- Cancelled
- Completed

A Reservation must:

- Have a check-out date after the check-in date.
- Calculate the number of nights.
- Calculate the total price.
- Be cancellable only if it has not been completed.
- Not be completed if it was cancelled.
- Preserve the room price from the moment the reservation was created.

Example:

Room price when reserved = $100/night

Room price later changes = $150/night

Existing reservation should still use:

$100/night


--------------------------------------------------
HOTEL
--------------------------------------------------

The Hotel must store:

- Rooms
- Guests
- Reservations

The Hotel must be able to:

- Add rooms.
- Register guests.
- Create reservations.
- Cancel reservations.
- Complete reservations.
- Find rooms by type.
- Find available rooms.


--------------------------------------------------
BUSINESS RULES
--------------------------------------------------

1. A room cannot have two active reservations for overlapping dates.

2. A guest cannot reserve the same room twice for overlapping dates.

3. Check-out must be after check-in.

4. Cancelled reservations cannot be completed.

5. Completed reservations cannot be cancelled.

6. A room's current price changing must not modify
   the price stored in existing reservations.

7. Invalid operations must not corrupt the hotel state.

8. A reservation must preserve the relationship between
   its specific Guest and Room.

9. A cancelled reservation should release the room
   when appropriate.

10. A reservation should only be considered active while
    its status allows it to occupy the room.


--------------------------------------------------
OOP REQUIREMENTS
--------------------------------------------------

Your implementation must demonstrate:

- Encapsulation
- Composition
- Association
- Properties
- Object interaction
- Separation of responsibilities
- State management
- Inheritance
- Method overriding

Use inheritance and method overriding in a meaningful way.
Do not add inheritance just for the sake of having it.


--------------------------------------------------
TESTING REQUIREMENTS
--------------------------------------------------

Create at least:

- 5 rooms
- 3 guests
- 5 reservations

Demonstrate:

- Creating reservations.
- Calculating reservation prices.
- Calculating the number of nights.
- Cancelling a reservation.
- Completing a reservation.
- Changing a room's price after a reservation.
- Finding available rooms.
- Finding rooms by type.
- Attempting to reserve an unavailable/overlapping room.
- Attempting to cancel a completed reservation.
- Attempting to complete a cancelled reservation.
- At least 5 invalid operations.


--------------------------------------------------
IMPORTANT
--------------------------------------------------

Invalid operations should raise appropriate exceptions
and should not leave the system in a partially modified
or inconsistent state.

Try to keep each class responsible for its own state,
while the Hotel coordinates interactions between Rooms,
Guests, and Reservations.

Do not unnecessarily modify or duplicate state that
already belongs to another object.
'''

from datetime import date

class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def register_guest(self, guest):
        self.guests.append(guest)

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def complete_reservation(self, reservation):
        for r in self.reservations:
            if reservation == r:
                r.change_status('completed')

    def cancell_reservation(self, reservation):
        for r in self.reservations:
            if reservation == r:
                r.change_status('cancelled')

        r.room.available = True
        

    def find_room_type(self, type):
        for r in self.rooms:
            if r.type == type:
                return r

    def find_room_available(self):

        available_rooms = []

        for r in self.rooms:
            if r.available == True:
                available_rooms.append(r)

        return available_rooms

class Room(Hotel):

    valid_types = ['single', 'double', 'suit']

    def __init__(self, room_number, room_type, price, status):

        if price < 0:
            raise ValueError("room price shouldn't be negative")

        if room_number < 0:
            raise ValueError("room number shouldn't be negative")

        if room_type not in Room.valid_types:
            raise ValueError("this is not a valid type for a room")

        self.room_number = room_number
        self.room_type = room_type
        self._price = price
        self._status = status
        self.available = True


class Guest(Hotel):
    def __init__(self, guest_id, name, email):
        self.guest_id = guest_id
        self.name = name
        self.email = email

        self.reservations = []


class Reservation(Hotel):

    valid_status = ['confirmed', 'cancelled', "completed"]

    def __init__(self, guest, room, check_in_date, check_out_date):

        if check_out_date < check_in_date:
            raise ValueError("check-out date should be after check-in date")

        room.available = False
        self.guest = guest
        self.room = room
        self._price = room._price
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self._status = 'confirmed'
        room.available = False
        guest.reservations.append(self)


    def calculate_nights(self):
        return self.check_out_date - self.check_in_date

    def calculate_price(self):
        return self.room._price * self.calculate_nights()

    def change_status(self, status):
        if status not in Reservation.valid_status:
            raise ValueError("this not a valid status for a reservation")

        if self._status == 'completed' and status == 'cancelled':
            raise ValueError("completed reservations can not be cancelled")

        if self._status == 'cancelled' and status == 'completed':
            raise ValueError("cancelled reservations can not be completed")

        self._status = status

        