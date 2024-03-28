from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter employee name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f'Employee {name} not found')


def find_employee_by_id():
    id_ = input('Enter employee id: ')
    employee = Employee.find_by_id(id_)
    if employee:
        print(employee)
    else:
        print(f'Employee {id_} not found')


def create_employee():
    name = input('Enter employee name: ')
    job_title = input('Enter employee job title: ')
    department_id = input('Enter department id: ')
    try:
        new_employee = Employee.create(name, job_title, int(department_id))
        print(f'Success: {new_employee}')
    except Exception as exc:
        print(f'Invalid employee information: {exc}')


def update_employee():
    id_ = input('Enter employee id: ')
    if employee := Employee.find_by_id(id_):
        try:
            name = input('Enter NEW employee name: ')
            if name != '':
                employee.name = name
            job_title = input('Enter NEW job title: ')
            if job_title != '':
                employee.job_title = job_title
            department_id = input('Enter NEW department id: ')
            if department_id != '':
                employee.department_id = department_id
            print(f'Success: {employee}')
        except Exception as exc:
            pass
    else:
        print(f'Employee {id_} not found')



def delete_employee():
    id_ = input('Enter employee id: ')
    employee = Employee.find_by_id(id_)
    if employee:
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    id_ = input('Enter department id: ')
    department = Department.find_by_id(id_)
    if department:
        for employee in department.employees():
            print(employee)
    else:
        print(f'Department {id_} not found')