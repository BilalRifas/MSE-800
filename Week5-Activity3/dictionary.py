# This code demonstrates the use of dictionary comprehensions and merging dictionaries in Python.
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)

# Merging multiple dictionaries into one
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5, 'e': 6}

merged_dict = {**dict1, **dict2, **dict3}
print(merged_dict)

# Filtering and merging dictionaries based on specific conditions
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

merged_dict = {**{k:v for k, v in dict1.items() if k in 'aeiou'},
               **{k:v for k, v in dict2.items() if k in 'aeiou'}}
print(merged_dict)

# Activity with custom keys and values
Key1 = ['a', 'b', 'c', 'd','e','a']
Value1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]
Key2 = ['u', 'b', 'o', 'x', 'e', 'a']
Value2 = [200, 30, 10, 88, 55, 920]


# Create dictionaries from the provided keys and values
dict1_odd = {k: v for k, v in zip(Key1, Value1)
             if v % 2 == 1}
dict2_odd = {k: v for k, v in zip(Key2, Value2)
             if v % 2 == 1}

print("Key1 --- Value1 :")
print(dict1_odd)
print()
print("Key2 --- Value2 :")
print(dict2_odd)