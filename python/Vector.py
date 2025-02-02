import math as m

class Vector:
    __count = 0

    # ---- magic methods -----
    def __init__(self, start, end):
        Vector.__check(start,end)
        self.__start = start
        self.__end = end
        Vector.__count+=1
        # adding attribute for vector as a single point (starting from [0;0])
        self.__update_vector()

    def __del__(self):
        Vector.__count-=1

    def __str__(self):
        return f"->[({self.start[0]}; {self.start[1]}), ({self.end[0]}; {self.end[1]})]"

    # adding vectors
    def __add__(self, other):
        a = self.end[0] + other.get_vector()[0]
        b = self.end[1] + other.get_vector()[1]
        end = [a,b]
        return Vector(self.start, end)

    # subtracting vectors
    def __sub__(self, other):
        a = self.end[0] - other.get_vector()[0]
        b = self.end[1] - other.get_vector()[1]
        end = [a, b]
        return Vector(self.start, end)

    # scalar multiplication
    def __mul__(self, other):
        a = self.get_vector()
        b = other.get_vector()
        return a[0]*b[0]+a[1]*b[1]

    # ------- static methods ---------
    @staticmethod
    def get_count():
        return Vector.__count

    # Check if vector length is 0
    @staticmethod
    def __check(start, end):
        if start == end:
            raise ValueError("The vector length can't be 0")
        return True

    # ---------- other methods ----------
    # adding presentation of the vector as single point
    def __update_vector(self):
        a = self.end[0] - self.start[0]
        b = self.end[1] - self.start[1]

        self.__vector=[a, b]

    def get_vector(self):
        return self.__vector

    def multiply_by_number(self, number):
        vector_by_num = [self.__vector[0]*number, self.__vector[1]*number]
        a = self.start[0]+vector_by_num[0]
        b = self.start[1]+vector_by_num[1]
        return Vector(self.start, [a, b])

    def get_length(self):
        return m.sqrt(pow(self.__vector[0],2)+pow(self.__vector[1],2))

    # ----- encapsulation -------
    # start point
    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value):
        Vector.__check(value, self.end)
        self.__start = value
        self.__update_vector()

    # end point
    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value):
        Vector.__check(self.start, value)
        self.__end = value
        self.__update_vector()