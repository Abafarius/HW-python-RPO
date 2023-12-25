def get_result_list(user_list):
    res_list = []
    res = 0
    for i in range(len(user_list)):
        res += user_list[0]
        res_list.append(res) 
    return res_list
        

def test_result_list():
    assert get_result_list([1,2,3]) == [1,3,6]
    assert get_result_list() == None
    assert get_result_list(["a","b","c"]) == ["a","ab","abc"]
    assert get_result_list([]) == []
    assert get_result_list(5) == [5]

test_result_list()