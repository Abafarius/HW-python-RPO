from datetime import datetime
from statistics import median


employees_db = []

def generate_employee_id():

    if not employees_db:
        return 1
    else:
        return max(employee['id'] for employee in employees_db) + 1

def newEmployee(fullName, birthDate, position, salary):
    try:

        firstName, lastName = fullName.split()


        birth_date = datetime.strptime(birthDate, "%Y-%m-%d")


        employee_id = generate_employee_id()


        employee = {
            'id': employee_id,
            'firstName': firstName,
            'lastName': lastName,
            'birthDate': birth_date,
            'hiredDate': datetime.now(),
            'firedDate': None,
            'position': position,
            'salary': salary
        }


        employees_db.append(employee)


        return {'id': employee_id, 'errorDescription': None}
    except ValueError as e:

        return {'id': -1, 'errorDescription': str(e)}

def fireEmployee(employee_id):
    try:

        employee = next((e for e in employees_db if e['id'] == employee_id), None)

        if employee:

            employee['firedDate'] = datetime.now()
            return {'id': employee_id, 'errorDescription': None}
        else:
            return {'id': -1, 'errorDescription': 'Employee not found'}
    except Exception as e:
        return {'id': -1, 'errorDescription': str(e)}

def getEmployeeId(name):
    try:

        employee = next((e for e in employees_db if name.lower() in e['firstName'].lower() or name.lower() in e['lastName'].lower()), None)

        if employee:
            return employee['id']
        else:
            return -1
    except Exception as e:
        return -1

def getEmployeeRecord(employee_id):
    try:

        employee = next((e for e in employees_db if e['id'] == employee_id), None)

        if employee:
            return employee
        else:
            return {'id': -1, 'errorDescription': 'Employee not found'}
    except Exception as e:
        return {'id': -1, 'errorDescription': str(e)}


new_employee_result = newEmployee("Dwight Shrute", "1987-12-11", "Salesman", 5000)
print(new_employee_result)

new_employee_result1 = newEmployee("Jim Halpert", "1987-05-04", "Salesman", 5000)
print(new_employee_result1)

new_employee_result2 = newEmployee("Oscar Menendes", "1985-10-06", "Accountant", 7000)
print(new_employee_result2)

new_employee_result3 = newEmployee("Pam Beesely", "1989-07-07", "Receptionist", 4000)
print(new_employee_result3)

new_employee_result4 = newEmployee("Ryan Wednesday", "1993-01-01", "Temp", 1000)
print(new_employee_result4)

new_employee_result5 = newEmployee("Angela Bauer", "1988-01-01", "Accountant", 7000)
print(new_employee_result5)

fire_employee_result = fireEmployee(1)
print(fire_employee_result)

get_employee_id_result = getEmployeeId("Dwight")
print(get_employee_id_result)

get_employee_record_result = getEmployeeRecord(1)
print(get_employee_record_result)



def getFiredEmployees():

    return [employee for employee in employees_db if employee['firedDate'] is not None]

def getSalaryStats():

    salaries = [employee['salary'] for employee in employees_db if employee['firedDate'] is None]
    
    if not salaries:
        return {
            'totalSalary': 0,
            'minSalary': 0,
            'maxSalary': 0,
            'avgSalary': 0,
            'medianSalary': 0
        }

    total_salary = sum(salaries)
    min_salary = min(salaries)
    max_salary = max(salaries)
    avg_salary = total_salary / len(salaries)
    median_salary = median(salaries)

    return {
        'totalSalary': total_salary,
        'minSalary': min_salary,
        'maxSalary': max_salary,
        'avgSalary': avg_salary,
        'medianSalary': median_salary
    }


fired_employees = getFiredEmployees()
print("Fired employee:")
for employee in fired_employees:
    print(f"{employee['id']} - {employee['firstName']} {employee['lastName']}")

salary_stats = getSalaryStats()
print("\nSalary stats:")
print(f"Total salary: {salary_stats['totalSalary']}")
print(f"Min salary: {salary_stats['minSalary']}")
print(f"Max salary: {salary_stats['maxSalary']}")
print(f"Average salary: {salary_stats['avgSalary']}")
print(f"Median salary: {salary_stats['medianSalary']}")