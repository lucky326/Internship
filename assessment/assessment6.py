def filter_even_numbers(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def filter_odd_numbers_from_dict(num_dic):
    odd_numbers = []
    for value in num_dic.values():
        if value % 2 != 0:
            odd_numbers.append(value)
    return odd_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dic = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

even_numbers_result = filter_even_numbers(numbers)
odd_numbers_result = filter_odd_numbers_from_dict(dic)

print("List of even numbers:", even_numbers_result)
print("List of odd numbers from the dictionary:", odd_numbers_result)
