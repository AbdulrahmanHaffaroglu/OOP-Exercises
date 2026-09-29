from mini_uber_system.models import *

def main():
    cash = Cash()
    p1 = Passenger('Abdulrahman', 55738257987)

    p1.register_payment_method(cash)