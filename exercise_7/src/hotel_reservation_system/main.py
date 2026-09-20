
from datetime import date

from .models import Guest, Hotel, Room


def run_scenario():
   hotel = Hotel()

   rooms = [
      Room(101, "single", 80),
      Room(102, "single", 90),
      Room(201, "double", 120),
      Room(202, "double", 140),
      Room(301, "suite", 220),
   ]
   for room in rooms:
      hotel.add_room(room)

   guests = [
      Guest("G001", "Ada Lovelace", "ada@example.com"),
      Guest("G002", "Grace Hopper", "grace@example.com"),
      Guest("G003", "Alan Turing", "alan@example.com"),
   ]
   for guest in guests:
      hotel.register_guest(guest)

   stay_start = date(2026, 10, 1)
   stay_end = date(2026, 10, 4)
   ada_reservation = hotel.create_reservation(
      guests[0], rooms[0], stay_start, stay_end
   )
   grace_reservation = hotel.create_reservation(
      guests[1], rooms[1], stay_start, stay_end
   )
   alan_reservation = hotel.create_reservation(
      guests[2], rooms[2], stay_start, stay_end
   )

   print("Hotel reservation scenario")
   print("=" * 27)
   print(
      f"Ada's reservation: {ada_reservation.calculate_nights()} nights, "
      f"${ada_reservation.calculate_price()}"
   )

   rooms[0].price = 150
   print(
      f"Room 101 is now ${rooms[0].price}/night; "
      f"Ada's reservation remains ${ada_reservation.calculate_price()}"
   )

   hotel.cancel_reservation(grace_reservation)
   hotel.complete_reservation(alan_reservation)

   print("\nRoom searches")
   print("Available rooms:", [room.room_number for room in hotel.find_room_available()])
   print("Double rooms:", [room.room_number for room in hotel.find_rooms_by_type("double")])

   invalid_operations = [
      (
         "overlapping reservation",
         lambda: hotel.create_reservation(
            guests[1], rooms[0], date(2026, 10, 2), date(2026, 10, 5)
         ),
      ),
      (
         "cancel completed reservation",
         lambda: hotel.cancel_reservation(alan_reservation),
      ),
      (
         "complete cancelled reservation",
         lambda: hotel.complete_reservation(grace_reservation),
      ),
      ("invalid room type", lambda: Room(401, "penthouse", 500)),
      (
         "invalid date range",
         lambda: hotel.create_reservation(
            guests[1], rooms[3], date(2026, 10, 5), date(2026, 10, 5)
         ),
      ),
   ]

   print("\nRejected operations")
   for description, operation in invalid_operations:
      try:
         operation()
      except ValueError as error:
         print(f"- {description}: {error}")

   return hotel


if __name__ == "__main__":
   run_scenario()








