def find_same_last_names(employees):
    result_dict = {}
    for employee in employees:
        parts = employee.split()
        if len(parts) == 2:
            last_name = parts[1]
            first_name = parts[0]
            if last_name in result_dict:
                result_dict[last_name].append(first_name)
            else:
                result_dict[last_name] = [first_name]
    return result_dict


def test_find_same_last_names():
    assert find_same_last_names(["Michael Scott", "Jim Halpert", "Pam Beesly", "Dwight Schrute"]) == {"Scott": ["Michael"], "Halpert": ["Jim"], "Beesly": ["Pam"], "Schrute": ["Dwight"]}
    assert find_same_last_names(["Ryan Howard", "Angela Martin", "Oscar Martinez", "Stanley Hudson"]) == {"Howard": ["Ryan"], "Martin": ["Angela"], "Martinez": ["Oscar"], "Hudson": ["Stanley"]}
    assert find_same_last_names([]) == {}
    assert find_same_last_names(["Andy Bernard", "Kevin Malone", "Kelly Kapoor"]) == {"Bernard": ["Andy"], "Malone": ["Kevin"], "Kapoor": ["Kelly"]}
    print("done.")
test_find_same_last_names()


data = input("Put the names, split them by comma and space: ")
employees = data.split(", ")

print(find_same_last_names(employees))
