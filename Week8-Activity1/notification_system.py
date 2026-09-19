from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

#notification types
class Email(Notification):
    def send(self):
        print("Email!")

class SMS(Notification):
    def send(self):
        print("SMS!")

class PushNotification(Notification):
    def send(self):
        print("Push Notification!")


#factory method for notification
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass

#Separate factory classes
class EmailFactory(NotificationFactory):
    def create_notification(self):
        return Email()
    
class SMSFactory(NotificationFactory):
    def create_notification(self):
        return SMS()
    
class PushNotificationFactory(NotificationFactory):
    def create_notification(self):
        return PushNotification()
    
# trying to call each methods
factory = EmailFactory()
notification = factory.create_notification()
notification.send()

factory2 = SMSFactory()
notification2 = factory2.create_notification()
notification2.send()

factory3 = PushNotificationFactory()
notification3 = factory3.create_notification()
notification3.send()

