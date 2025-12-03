class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
    
    def calculate_salary(self):
        return 0
    
    def get_details(self):
        return f"ID: {self.emp_id} | Name: {self.name}"

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, emp):
        return self.employees.append(emp)
    
    def show_payroll(self):
        print(f"--- 💰 Payroll for {self.company_name} ---")
        total_payout = 0

        for emp in self.employees:
            details = emp.get_details()
            salary = emp.calculate_salary()
            print(f"{details} | เงินเดือน: {salary:,.2f} บาท")
            total_payout += salary

        print("-" * 30)
        print(f"ยอดจ่ายเงินเดือนรวมทั้งสิ้น: {total_payout} บาท")

if __name__ == "__main__":
    print(">>> เริ่มทดสอบระบบเงินเดือน <<<\n")

    my_company = Company("Tech Startup Inc.")

    dev = SalariedEmployee("E01", "Alice", 50000)

    freelance = HourlyEmployee("E02", "Bob", 500, 100)

    my_company.add_employee(dev)
    my_company.add_employee(freelance)

    my_company.show_payroll()