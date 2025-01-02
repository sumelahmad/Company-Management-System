from employee_management import Employee, EmployeeManagement
from product_management import Product, ProductManagement
from task_management import Task, TaskManagement
from financial_management import FinancialManagement
from client_vendor_management import ClientVendor, ClientVendorManagement

def main():
    # Employee Management Example
    emp1 = Employee(1, "Alice", "HR", 3000)
    emp2 = Employee(2, "Bob", "Finance", 4000)
    emp_mgmt = EmployeeManagement()
    emp_mgmt.add_employee(emp1)
    emp_mgmt.add_employee(emp2)
    emp_mgmt.generate_payroll_report()

    # Product Management Example
    prod1 = Product(101, "Laptop", "Electronics", 1000, 10)
    prod2 = Product(102, "Shirt", "Clothing", 20, 100)
    prod_mgmt = ProductManagement()
    prod_mgmt.add_product(prod1)
    prod_mgmt.add_product(prod2)
    prod_mgmt.generate_inventory_report()

    # Task Management Example
    task1 = Task(1001, "Complete Report", "2025-01-10")
    task_mgmt = TaskManagement()
    task_mgmt.add_task(task1)
    task_mgmt.generate_task_report()

    # Financial Management Example
    fin_mgmt = FinancialManagement()
    fin_mgmt.record_income(10000)
    fin_mgmt.record_expense(5000)
    fin_mgmt.generate_profit_loss_statement()

    # Client Vendor Management Example
    cv1 = ClientVendor(1, "Client A", "client")
    cv2 = ClientVendor(2, "Vendor B", "vendor")
    cv_mgmt = ClientVendorManagement()
    cv_mgmt.add_client_vendor(cv1)
    cv_mgmt.add_client_vendor(cv2)
    cv_mgmt.generate_client_vendor_report()

if __name__ == "__main__":
    main()
