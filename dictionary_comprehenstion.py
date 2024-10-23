squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)

fruits = ['apple', 'banana', 'cherry']
fruit_dict = {fruit: len(fruit) for fruit in fruits}
print(fruit_dict)

original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)

matrix = [[1, 2, 3], [4, 5, 6]]
dict_matrix = {i: {j: value for j, value in enumerate(row)} for i, row in enumerate(matrix)}
print(dict_matrix)