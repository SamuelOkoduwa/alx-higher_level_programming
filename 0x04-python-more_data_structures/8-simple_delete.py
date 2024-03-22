#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary


# a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}

# # Delete an existing key
# new_dict = simple_delete(a_dictionary, 'track')
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)
# print("--")
# print("--")

# # Attempt to delete a non-existent key
# new_dict = simple_delete(a_dictionary, 'c_is_fun')
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)
