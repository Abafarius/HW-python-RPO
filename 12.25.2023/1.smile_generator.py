def generate_smiley_string(num_smileys):
    return "😊" * num_smileys


def test_generate_smiley_string():
    assert generate_smiley_string(3) == "😊😊😊"
    assert generate_smiley_string(5) == "😊😊😊😊😊"
    assert generate_smiley_string(0) == ""
    assert generate_smiley_string(1) == "😊"
    print('done.')

test_generate_smiley_string()

data = input("Enter ineger number: ")
try:
    num = int(data)
except ValueError:
    print("Wrong value!")
    exit()

print(generate_smiley_string(num))
