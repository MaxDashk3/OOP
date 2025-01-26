class Employees:
    employees = []
    employee_count = 0
    departments = {}
    department_count = 0

    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id
        self.id = Employees.employee_id_generator()
        Employees.employees.append(self)
        Employees.employee_count+=1

    def __del__(self):
        Employees.employee_count-=1

    @staticmethod
    def employee_id_generator():
        employee_amount=Employees.employee_count
        if employee_amount == 0:
            result = 1
        else:
            result = Employees.employees[employee_amount-1].id+1
        return result

    @staticmethod
    def department_id_generator():
        dept_keys = Employees.departments.keys()
        dept_amount = Employees.department_count
        if dept_amount == 0:
            result = 1
        else:
            result = max(dept_keys)+1
        return result

    @staticmethod
    def add_department(name):
        Employees.departments[Employees.department_id_generator()]=name
        Employees.department_count += 1

    @staticmethod
    def delete_department():
        Employees.departments.pop(id)
        Employees.department_count-=1

    @staticmethod
    def show_info():
        print("Departments:\n"
              f"Amount: {Employees.department_count}\n")
        for i in Employees.departments.keys():
            print(f"Id: {i}\n"
                  f"Name: {Employees.departments[i]}\n")

        print("Employees:\n"
              f"Amount: {Employees.employee_count}")
        for i in Employees.employees:
            print(f"Id: {i.id}\n"
                  f"Name: {i.name}")

            print(f"Department: {Employees.departments[i.department_id]}\n"
                  if Employees.departments.keys().__contains__(i.department_id)
                  else
                  "Department missing\n")