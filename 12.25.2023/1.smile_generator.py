def generate_smiley_string(num_smileys):
    return "😊" * num_smileys


def test_generate_smiley_string():
    assert generate_smiley_string(3) == "😊😊😊"
    assert generate_smiley_string(5) == "😊😊😊😊😊"
    assert generate_smiley_string(0) == ""
    assert generate_smiley_string(1) == "😊"

def get_num_smileys_from_user():
    try:
        num_smileys = int(input("Enter the count of smiles: "))
        return num_smileys
    except ValueError:
        print("Please, enter an integer number.")
        return get_num_smileys_from_user()

if __name__ == "__main__":
    num_smileys = get_num_smileys_from_user()
    smiley_string = generate_smiley_string(num_smileys)
    print(smiley_string)    