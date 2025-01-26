from Employees import Employees as emp

emp.add_department("Dept_A")
emp.add_department("Dept_B")

emp1 = emp("Tom",1)
emp2 = emp("Amy", 2)
emp3 = emp("Bob", 3)

emp.show_info()