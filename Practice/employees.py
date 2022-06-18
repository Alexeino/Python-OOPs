class Employee:
    company_name = "ABC"
    address = "Silicon Valley, Vision Complex , USA"
    bonus_percentage = 50

    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    @classmethod # Class method
    def get_company_address(cls):
        return "{} - {}".format(cls.company_name,cls.address)

    # Instance method
    def emp_details(self):
        print("Name - ",self.name)
        print("Salary - ",self.salary)
        print("Department - ",self.department)

    @staticmethod
    def total_payout(salary,bonus):
        print(salary + (salary * (bonus/100)))


print(Employee.get_company_address())

emp1 = Employee("Manish",50000,"IT")
emp1.emp_details()
emp1.total_payout(emp1.salary,emp1.bonus_percentage)