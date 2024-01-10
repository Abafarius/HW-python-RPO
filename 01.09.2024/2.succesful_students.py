def get_succ_studs(students):
    
    result = ''
    result += students['name']
    return result

students = (
            {'name': 'Alex Novak', 'age': 21, 'course': 'Python', 'average_grade': 9.78},
            {'name': 'Peter Sullivan', 'age': 21, 'course': 'Python', 'average_grade': 9.00},
            {'name': 'Akane Tendo', 'age': 19, 'course': 'HTML', 'average_grade': 4.72},
            {'name': 'Hidetaka Miyadzaki', 'age': 23, 'course': 'Python', 'average_grade': 12.00},
            {'name': 'Ken Levin', 'age': 21, 'course': 'HTML', 'average_grade': 8.98},
            {'name': 'Kaya Scodelario', 'age': 20, 'course': 'Python', 'average_grade': 11.89},
            {'name': 'Nat King', 'age': 23, 'course': 'Python', 'average_grade': 6.25},
            {'name': 'Leya Argano', 'age': 23, 'course': 'Python', 'average_grade': 11.25}
            )

succesful_students = filter(lambda x: x['average_grade']>11, students)
print(tuple(succesful_students))