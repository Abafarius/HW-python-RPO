def sum2(num1,num2):
    if type(num1) in (int, float) and type(num2) in (int, float):
        return num1+num2
    return None
def test_sum2():
    assert sum2(1,2) == 3
    assert sum2(-1,1) == 0
    assert sum2(0.4, 6.8) == 0.4 + 6.8
    assert sum2("aa","bb") == None
    print("Test accomplished")

test_sum2()