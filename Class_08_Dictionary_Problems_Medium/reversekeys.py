import enum


test_dict = {'B' : 4, 'Y' : 2, 'U' : 5}

# def reverse(dict):
#     for key, value in enumerate(dict):
#         dict[value]=key
#     return dict

# print(reverse(test_dict))


def reverse2(dict):
    results={value: key for (key, value) in dict.items()}
    return results

print(reverse2(test_dict))