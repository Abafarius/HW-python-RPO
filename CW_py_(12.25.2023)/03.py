def get_result_list(user_list = None):
    if user_list == None:
        return None
    if type(user_list[0]) is str:
        res = ''
        res_list = []
        for i in range(len(user_list)):
            res += user_list[i]
            res_list.append(res) 
    else:
        res_list = []
        res = 0
        for i in range(len(user_list)):
            res += user_list[i]
            res_list.append(res) 
    return res_list
        

def test_result_list():
    assert get_result_list([1,2,3,5]) == [1,3,6,11]
    assert get_result_list() == None
    assert get_result_list(["a","b","c"]) == ["a","ab","abc"]
    assert get_result_list([]) == []
    assert get_result_list(5) == [5]
    print('done')
test_result_list()