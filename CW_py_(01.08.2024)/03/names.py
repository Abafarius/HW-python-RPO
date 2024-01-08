def get_names(numbers):
    result = []
    for num in numbers:
        match num:
            case 1:
                result += ["one"]
            case 2:
                result += ["two"]
            case 3:
                result += ["three"]
            case 4:
                result += ["four"]
            case 5:
                result += ["five"]
            case 6:
                result += ["six"]
            case 7:
                result += ["seven"]
            case 8:
                result += ["eight"]
            case 9:
                result += ["nine"]
            case 10:
                result += ["ten"]
            case _:
                result += [""]
    return result 
        

def test_get_names():
    assert get_names([3,5,1]) == ["three", "five", "one"]
    assert get_names([3,11]) == ["three", ""]
    assert get_names([]) == []
    print("done.")

test_get_names()