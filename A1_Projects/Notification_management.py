from abc import ABC, abstractmethod

class Notification(ABC):
    
    @abstractmethod
    def send_notification(self, message):
        pass
    
class EmailNotification(Notification):
    def send_notification(self, message):   
        return f"Sending Email: {message}"
    
class SMSNotification(Notification):
    def send_notification(self, message):
        return f"Sending SMS: {message}"
    
class PushNotification(Notification):
    def send_notification(self, message):
        return f"Sending Push Notification: {message}"

n1 = EmailNotification()
print(n1.send_notification("This is Email"))

n2 = SMSNotification()
print(n2.send_notification("This SMS"))

n3 = PushNotification()
print(n3.send_notification("This is push notification"))

class WhatsAppNotification(Notification):
    pass

w1 = WhatsAppNotification()

# p1 = Notification()
# p1.send_notification("Parent")
# does not instantiate abstract class without implementation of abstract method but why ?
# The send_notification() method contains only pass. It doesn't actually send an email, SMS, or push notification.

# The parent class doesn't know HOW to send notifications.

# That's why Python prevents you from creating an object of an abstract class that still has unimplemented abstract methods.

# Instead, Python raises a TypeError.
