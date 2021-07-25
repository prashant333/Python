# Using lambda function to sort a given dictionary.

model_varient = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]


def sort_dictionary(dic):
    sorted_model = sorted(dic, key=lambda x: x['color'])
    return sorted_model


print(sort_dictionary(model_varient))
