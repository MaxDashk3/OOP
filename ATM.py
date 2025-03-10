import random
from abc import ABCMeta, abstractmethod
from collections.abc import Sequence

class CreditCard:
    def __init__(self, number, pin, money):
        self.__number = number
        self.__pin = pin
        self.money = money

    def get_pin(self): return self.__pin

    def get_number(self): return self.__number

class Collector:
    def __init__(self, name, bills):
        self.name = name
        self.bills = bills

class ATM(metaclass=ABCMeta):

    _bill_numbers = [1000, 500, 200, 100, 50]

    def __init__(self, name, bills=[0,0,0,0,0]):
        self._blocked = False
        self.bills = bills
        self.name = name

    @property
    def bills(self):
        return self._bills

    @bills.setter
    def bills(self, value):
        for i in value:
            if i < 0:
                raise ValueError('Bill amount cannot be negative')
        if len(value) == len(ATM._bill_numbers):
            self._bills = value
        else:
            raise ValueError(f"There has to be {len(ATM._bill_numbers)} numbers in the list")
        if value == [0,0,0,0,0] and not self._blocked:
            print("No bills available! Blocking ATM...")
            self._blocked = True
        if value != [0,0,0,0,0] and self._blocked:
            print("Unlocking ATM")
            self._blocked = False

    @abstractmethod
    def authenticate(self, card):
        pass


    def get_bills(self, card: CreditCard):
        if self._blocked:
            print("ATM blocked!!!")
            return
        print(f"Hello from {self.name}! Welcome!")

        if not self.authenticate(card):
            return

        print("Available amount: ", card.money)
        amount = int(input("Enter amount to withdraw: "))
        if card.money < amount:
            print("Not enough money on card")
            return

        withdraw_bills = self._calculate_bills(amount)
        could_withdraw = self._get_bill_sum(withdraw_bills)
        if could_withdraw != amount:
            choice = input(f"Couldn't withdraw {amount}, withdraw {could_withdraw} instead? y/n: ")
            if choice not in ['y', 'Y']:
                print("Withdraw cancelled!")
                return
        card.money -= could_withdraw
        print("Withdraw successful!")
        print("Your bills:")
        new_bills = []
        for i in range(len(withdraw_bills)):
            if withdraw_bills[i] != 0:
                print(f"{withdraw_bills[i]} bills for {self._bill_numbers[i]}")

            new_bills.append(self.bills[i] - withdraw_bills[i])
        self.bills = new_bills
        print()

    def _calculate_bills(self, number):
        return_bills = []

        for i in range(len(self.bills)):
            if number // ATM._bill_numbers[i] > self.bills[i]:
                return_bills.append(self.bills[i])
            else:
                return_bills.append(number // ATM._bill_numbers[i])
            number -= return_bills[i] * ATM._bill_numbers[i]

        return return_bills

    @staticmethod
    def _get_bill_sum(bills):
        result = 0
        for i in range(len(bills)):
            result += bills[i] * ATM._bill_numbers[i]
        return result

    def get_replenished(self, collector: Collector):
        new_bills = []
        for i in range(len(self.bills)):
            new_bills.append(self.bills[i] + collector.bills[i])
            collector.bills[i] = 0
        self.bills = new_bills

    def __str__(self):
        return_str = f"name: {self.name}, bills: "
        for i in range(len(self.bills)):
            return_str += f"{self.bills[i]} bills for {self._bill_numbers[i]}, "
        return_str += f"state: {"blocked" if self._blocked else "unlocked"}"
        return return_str

class BasicATM(ATM):

    def authenticate(self, card):
        pin = int(input("Enter pincode: "))
        if pin != card.get_pin():
            print("Wrong pin!!!")
            return False
        else: return True

    def __str__(self):
        return super().__str__() + ", type: Basic ATM"


class ProtectedATM(ATM):
    def authenticate(self, card):
        pin = int(input("Enter pincode: "))
        if pin != card.get_pin():
            print("Wrong pin!!!")
            return False

        print("Enter the code from SMS")
        sms_code = ProtectedATM.__generate_code()
        print(f"New Message - {self.name}: Your code is {sms_code}, don't tell anyone!")
        sms_code_input = input()
        if sms_code_input != sms_code:
            print("You have one more try before the ATM blocks!")
            sms_code_input = input()
            if sms_code_input != sms_code:
                self._blocked = True
                print("ATM blocked!!!")
                return False

        return True

    @staticmethod
    def __generate_code():
        result = ''
        for i in range(4):
            result = result + str(random.randint(0,9))
        return result

    def __str__(self):
        return super().__str__() + ", type: Protected ATM"

class Bank(Sequence):
    def __init__(self, atms = None):
        self._ATMs = []
        self.add(atms)

    def __len__(self):
        return len(self._ATMs)

    def __getitem__(self, key):
        return self._ATMs[key]

    def __setitem__(self, key, value):
        self._ATMs[key] = value

    def __delitem__(self, key):
        del self._ATMs[key]

    def __iter__(self):
        # for i in self._ATMs:
        #     yield i
        return iter(self._ATMs)

    def add(self, other):
        if isinstance(other, list):
            for i in other:
                if isinstance(i, ATM):
                    self._ATMs.append(i)

        elif isinstance(other, Bank):
            for i in other:
                self._ATMs.append(i)

        elif isinstance(other, ATM):
            self._ATMs.append(other)

    def info(self):
        index = 1
        for i in self._ATMs:
            print(f"ATM {index}:\n{i}")
            index += 1
