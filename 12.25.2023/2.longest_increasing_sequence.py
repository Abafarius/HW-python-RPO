def find_longest_increasing_sequence(numbers):
    if not numbers:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)

def test_find_longest_increasing_sequence():
    assert find_longest_increasing_sequence([1, 2, 3, 1, 2, 3, 4]) == 4
    assert find_longest_increasing_sequence([5, 4, 3, 2, 1]) == 1
    assert find_longest_increasing_sequence([1, 2, 3, 4, 5]) == 5
    assert find_longest_increasing_sequence([]) == 0
    assert find_longest_increasing_sequence([1, 2, 3, 2, 3, 4, 5]) == 4
    print("done.")