from .notification import Notification
from .email import Email
from .push_notification import PushNotification
from .sms import SMS


class User:
    def __init__(self, name, email, phone_number, password, device_id):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.device_id = device_id

        self.orders = []

        self.channel_list = {
            'email': Email(self.email),
            'push_notification': PushNotification(self.device_id),
            'sms': SMS(self.phone_number)
            }

    def notify(self, channel_list, message, user=None):
        notification = Notification(channel_list, message, user)
        notification.send()

    def place_order(self, order):
        if order in self.orders:
            raise ValueError("you already ordered this order")

        self.orders.append(order)
        message = f"your order: {order} has been successfully placed"

        channel_list = [self.channel_list['email'],
                        self.channel_list['push_notification'], 
                        self.channel_list['sms']]

        self.notify(channel_list, message)


    def cancel_order(self, order):
        if order not in self.orders:
            raise ValueError("you don't have this order")

        self.orders.remove(order)
        message = f"your order: {order} has been successfully removed"

        channel_list = [self.channel_list['email'],
                        self.channel_list['push_notification'], 
                        self.channel_list['sms']]

        self.notify(channel_list, message)



    def pay_order(self, order):
        if order not in self.orders:
            raise ValueError("you don't have this order")
        
        self.orders.remove(order)
        message = f"thank you very much for paying for your order: {order}"
        
        channel_list = [self.channel_list['email'],
                        self.channel_list['push_notification'], 
                        self.channel_list['sms']]
        
        self.notify(channel_list, message)


    def send_email(self, message, user):
        channel_list = [user.channel_list['email']]
        
        user.notify(channel_list, message, user)


    def send_message(self, message, user):
        channel_list = [user.channel_list['sms']]
                        
        user.notify(channel_list, message, user)


    def change_password(self, new_password):
        if new_password == self.password:
            raise ValueError("new password can't be the same as the old one")

        self.password = new_password
        message = 'your password has been changed successfully'

        channel_list = [self.channel_list['sms'], self.channel_list['email']]

        self.notify(channel_list, message)

    def __repr__(self):
        return f'{self.name}'