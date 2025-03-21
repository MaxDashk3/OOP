def instance_limit(limit: int):
    # checking if the number is appropriate
    if type(limit) != int:
        raise TypeError("Limit must be an integer")
    if limit < 0:
        raise ValueError("Limit cannot be negative")

    def decorator(cls):
        # setting current instance count
        cls._instance_amount = 0

        # replacing the __new__ method
        old_new = cls.__new__
        def updated_new(class_, *args, **kwargs):
            if cls._instance_amount >= limit:
                raise Exception(f"Can't create more than {limit} instances")
            else:
                cls._instance_amount += 1
                return old_new(class_)

        cls.__new__ = updated_new

        # replacing the __del__ method
        old_del = getattr(cls, "__del__", None)
        def updated_del(class_, *args, **kwargs):
            cls._instance_amount -= 1
            if old_del:
                return old_del(class_)
        cls.__del__ = updated_del

        return cls
    return decorator

@instance_limit(3)
class ExampleObject:
    def __init__(self, name):
        self.name = name

# testing object creation
obj1 = ExampleObject("Object 1")
# checking if arguments are passed correctly
print(obj1.name)

obj2 = ExampleObject("Object 2")
obj3 = ExampleObject("Object 3")

#checking object deletion
del obj3
obj4 = ExampleObject("Object 4")
obj5 = ExampleObject("Object 5") # has to raise an exception
