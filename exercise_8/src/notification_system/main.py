from models import User, Channel, Notification, PushNotification, Email, SMS

def main():
    u1 = User(name='Hakan', email='hakan@gmail.com', phone_number='905075981232', password='Hkkn123', device_id='Hakan Galaxy A12')
    u2 = User(name='Omer', email='omr2004@gmail.com', phone_number='905075993847', password='X_omr_X', device_id='Omer iphone')
    u3 = User(name='Hasan', email='hasan_aydin@gmail.com', phone_number='909493202147', password='H_X_S_X_N', device_id='Hasan Redmi 12')
    u4 = User(name='Ali', email='ali_1995@gmail.com', phone_number='905093845847', password='ALI_1995', device_id='Ali xiaomi')


    object_1 = '3 books'

    u1.place_order(object_1)
    print()
    u1.cancel_order(object_1)
    print()
    print()

    u2.place_order(object_1)
    print()
    u2.pay_order(object_1)
    print()
    print()


    message1 = "did this email reach you?"
    message2 = "the email reached me but i can't reply back"

    u3.send_email(message1, u4)
    print()
    u4.send_message(message2, u3)
    print()
    print()


    u3.change_password('I Love Miami')

if __name__ == "__main__":
    main()