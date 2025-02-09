from random import random

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def check_battery(self):
        print(f'Capacity: {self.capacity} mAh')

class Phone:
    def __init__(self, battery_capacity, name, os):
        self.battery = Battery(battery_capacity)
        self.name = name
        self.os = os
        self.turned_on = False

    def call(self, Phone):
        if self.turned_on:
            if Phone == self:
                print("You just tried to call yourself")
            else:
                print(f"{self.name} is calling {Phone.name}")
                Phone.receive_call(self.name)
        else:
            print(f'{self.name} is turned off')

    def receive_call(self, name):
        if self.turned_on:
            print(f"{self.name} is getting a call from {name}")
        else:
            print(f'{self.name} is turned off')

    def turn_on(self):
        self.turned_on = True
        print(f"{self.name} is turned on and ready to make a call")

    def turn_off(self):
        self.turned_on = False
        print(f"{self.name} is turned off")

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"OS: {self.os}")
        print(f"Battery capacity: {self.battery.capacity} mAh")
        print(f"State: {('On' if self.turned_on else 'Off')}")

class ButtonPhone(Phone):
    def __init__(self, battery_capacity, name, os):
        super().__init__(battery_capacity, name, os)

    def show_info(self):
        super().show_info()
        print(f"Button phone")

    def press_some_buttons(self):
        if self.turned_on:
            print(f"You have pressed something on your {self.name}")
            if random() >= 0.5: print('Music started playing...')
            else: print('You almost called someone')

class Smartphone(Phone):

    def __init__(self, battery_capacity, name, os):
        super().__init__(battery_capacity, name, os)
        self.internet_connection = False
        self.installed_apps = ["Camera","Instagram","Messages","Twitter"]

    def connect_to_internet(self):
        if self.turned_on:
            self.internet_connection = True
            print("Connected!")
        else:
            print(f'{self.name} is turned off')

    def disconnect_from_internet(self):
        if self.turned_on:
            self.internet_connection = False
            print("Disconnected!")
        else:
            print(f'{self.name} is turned off')

    def download_app(self, app_name):
        if self.turned_on:
            if self.internet_connection:
                if not self.installed_apps.__contains__(app_name):
                    self.installed_apps.append(app_name)
                    print(app_name, "installed")
                else:
                    print(app_name, "already installed")
            else: print("No Internet connection!!")
        else: print(f"{self.name} is turned off")

    def uninstall_app(self, app_name):
        if self.turned_on:
            if self.installed_apps.__contains__(app_name):
                self.installed_apps.remove(app_name)
            else: print("No such app installed")
        else: print(f"{self.name} is turned off")

    def show_info(self):
        super().show_info()
        print("Internet connection:", ("On" if self.internet_connection else "Off"))
        print("Installed apps:", self.installed_apps)
        print(f"Smartphone")

class FoldablePhone(Smartphone):
    def __init__(self, battery_capacity, name, os, fold_direction):
        Smartphone.__init__(self, battery_capacity, name, os)
        self.fold_direction = fold_direction

    def fold(self):
        print(f'Folding {self.name} {self.fold_direction}ly')

    def show_info(self):
        Phone.show_info(self)
        print("Internet connection:", ("On" if self.internet_connection else "Off"))
        print("Installed apps:", self.installed_apps)
        print(f"Fold direction: {self.fold_direction}")
        print('Foldable phone')
