from abc import ABC, abstractmethod

# button classes
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class CheckBox(ABC):
    @abstractmethod
    def press(self):
        pass


# Concrete Products - Windows
class WindowsButton(Button):
    def click(self):
        print("Clicking windows button")


class WindowsCheckBox(CheckBox):
    def press(self):
        print("Pressing windows check box")


# Concrete Products - Mac
class MacButton(Button):
    def click(self):
        print("Clicking Mac button")


class MacCheckBox(CheckBox):
    def press(self):
        print("Pressing Mac check box")


# Abstract Main Factory Class
class OperatingSystemFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# Concrete Factories
class WindowsOSFactory(OperatingSystemFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckBox()


class MacOSFactory(OperatingSystemFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckBox()


# Client is using the Different Operating systems

# Windows User
windows_factory = WindowsOSFactory()
windows_button = windows_factory.create_button()
windows_checkbox = windows_factory.create_checkbox()

windows_button.click()
windows_checkbox.press()

print("------------------------------------------")

# Mac User
mac_factory = MacOSFactory()
mac_button = mac_factory.create_button()
mac_checkbox = mac_factory.create_checkbox()

mac_button.click()
mac_checkbox.press()
