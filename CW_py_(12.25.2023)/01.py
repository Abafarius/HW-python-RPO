def get_asquare (a=None,b=None):
    if b is None:
        b = a

    if not type(a) in (int, float) and not type(b) in (int, float):
        return None

    return a*b
    
def test_get_asquare():
    assert get_asquare(2,3) == 6
    assert get_asquare(3,0) == 0
    assert get_asquare(3) == 9
    assert get_asquare(4.5) == 4.5*4.5
    assert get_asquare("asddf") == None
    assert get_asquare() == None
    print("Test accomplished")

test_get_asquare()