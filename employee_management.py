class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.attendance = []
        self.tasks = []

    def record_attendance(self, date, status):
        self.attendance.append({"date": date, "status": status})

    def assign_task(self, task):
        self.tasks.append(task)

    def get_monthly_salary(self):
        return self.salary

    def display_employee_info(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

class EmployeeManagement:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.employee_id] = employee

    def update_employee(self, employee_id, name=None, department=None, salary=None):
        employee = self.employees.get(employee_id)
        if employee:
            if name:
                employee.name = name
            if department:
                employee.department = department
            if salary:
                employee.salary = salary

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]

    def generate_payroll_report(self):
        for employee in self.employees.values():
            print(f"{employee.name} - {employee.get_monthly_salary()}")
