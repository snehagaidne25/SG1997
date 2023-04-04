import json

class Employee:
    def _init_(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def _repr_(self):
        return f"Employee(name={self.name}, dob={self.dob}, height={self.height}, city={self.city}, state={self.state})"

# read JSON data from file
with open('employees.json') as f:
    data = json.load(f)

# create list of Employee objects
employees = []
for emp in data['employees']:
    emp_obj = Employee(emp['name'], emp['dob'], emp['height'], emp['city'], emp['state'])
    employees.append(emp_obj)

# print list of Employee objects
print(employees)




   

