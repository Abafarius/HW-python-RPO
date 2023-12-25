def is_same_type(array = None):
    if not array:
        return False
    for item in array:
        if not type(array[0]) is type(item):
            return False
    return True

def test_is_same_type():
    assert is_same_type([1, 1, 2, 3]) == True
    assert is_same_type(["asdasd", 'asadw', 'asdasdfg']) == True
    assert is_same_type([True, False, True]) == True
    assert is_same_type(['asdasd', 43, 'asdfgg']) == False
    assert is_same_type([True, "asdghbx", 55]) == False
    assert is_same_type([]) == False
    assert is_same_type(["asdfcxv"]) == True
    assert is_same_type([123]) == True
    assert is_same_type([(), ()]) == True
    assert is_same_type() == False
    print("done")
test_is_same_type()