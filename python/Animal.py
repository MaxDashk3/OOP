class Animal:
    kind = "warm-blooded"
    __counter = 0

    def __init__(self, name, speed):
        self.__name = name
        self.speed = speed
        Animal.__counter += 1
        Animal.showCount()

    def __del__(self):
        Animal.__counter -= 1
        Animal.showCount()

    def sayHello(self):
        print("Hello, I am", self.__name, ", my speed is", self.speed)

    def speedUp(self, delta):
        self.speed += delta

    def speedDown(self, delta):
        if self.speed >= delta:
            self.speed = self.speed - delta

    def stop(self):
        self.speed = 0

    def __getName(self):
        return self.__name

    @staticmethod
    def showCount():
        print("Now", Animal.__counter,"animals exist")

an1 = Animal("Kitty", 1)
an2 = Animal("Puppy", 2)
an3 = Animal("Big dog", 5)

an3.sayHello()
an3.speedUp(20)
an3.speedDown(15)
an3.sayHello()

an2.stop()
an2.sayHello()

print(an1.__dict__)
print(Animal.__dict__)
print(an1._Animal__name)
print(an1._Animal__getName())
print(Animal._Animal__counter)

del an1
del an2
del an3

