def generate_smiley_string(num_smileys):
    return "😊" * num_smileys


def test_generate_smiley_string():
    assert generate_smiley_string(3) == "😊😊😊"
    assert generate_smiley_string(5) == "😊😊😊😊😊"
    assert generate_smiley_string(0) == ""
    assert generate_smiley_string(1) == "😊"
    print('done.')

test_generate_smiley_string()

def get_num_smileys_from_user():
    user_data = input("Enter the count of smiles: ")
    try:
        num_smileys = int(user_data)
        return num_smileys
    except ValueError:
        print("Please, enter an integer number.")
        return get_num_smileys_from_user()

if __name__ == "__main__":
    num_smileys = get_num_smileys_from_user()
    smiley_string = generate_smiley_string(num_smileys)
    print(smiley_string)    