from mini_uber_system.models import *

def main():
    # creating payment methods for user to have and use
    cash1 = Cash()
    credit_card1 = CreditCard()
    bank_transfer1 = BankTransfer()

    cash2 = Cash()
    credit_card2 = CreditCard()
    bank_transfer2 = BankTransfer()
    payment_methods_2 = [cash2, credit_card2, bank_transfer2]

    bank_transfer3 = Cash()


    # creating passengers
    p1 = Passenger('Abdulrahman', 5573825798, credit_card_method=credit_card1)
    p2 = Passenger('Mahmut', 7329563278)
    p3 = Passenger('Ali', 3828653923)


    # registring payment methods for passengers in different ways and scenarious:

    # - scenario 1: registering a payment method while creating the passenger and adding other payment methdos later
    p1.register_payment_method(cash1)
    p1.register_payment_method(bank_transfer1)

    # - scenario 2: registering all of the payment methods after creating the passenger
    for payment_method in payment_methods_2:
        p2.register_payment_method(payment_method)

    # - scenario 3: registering only one payment method to the passenger
    p3.register_payment_method(bank_transfer3)


    # creating Drivers
    d1 = Driver('Selim', 2378648732)
    d2 = Driver('Henry', 2384793232, Vehicle.create_vehicle('standart_car'))
    d3 = Driver('Steve', 4789128402)


    # creating vehicles
    v1 = Vehicle.create_vehicle('premium_car')
    v3 = Vehicle.create_vehicle('motorcycle')


    # register vehicles for drivers
    d1.register_vehicle(v1)
    d3.register_vehicle(v3)


    # paseengers make ride requests
    r1 = p1.make_ride_request(
        'Tabanca', 
        'Levent', 
        3, 
        'premium_car', 70)
    
    r2 = p2.make_ride_request(
        'Fatih', 
        'Ikitelli', 
        3, 
        'standart_car', 
        50)
    
    r3 = p3.make_ride_request(
        'Aksaray', 
        'Esenler', 
        1, 
        'motorcycle', 
        80)


    # drivers accepts rides
    d1.accept_ride(r1)
    d2.accept_ride(r2)
    d3.accept_ride(r3)


    # drivers start rides
    d1.start_ride()
    d2.start_ride()
    d3.start_ride()


    # drivers complete their rides
    d1.complete_ride()
    d2.complete_ride()
    d3.complete_ride()
    print()

    # passengers pays their rides
    p1.pay_ride(1850, cash1)
    print()
    p2.pay_ride(800, credit_card2)
    print()
    p3.pay_ride(830, bank_transfer3)
    print()


    # display the information of the rides
    r1.display()
    r2.display()
    r3.display()
    print()


    # display passenger history
    p1.view_ride_history()
    p2.view_ride_history()
    p3.view_ride_history()
    print()


    # display driver history
    d1.view_ride_history()
    d2.view_ride_history()
    d3.view_ride_history()
    print()




if __name__ == '__main__':
    main()