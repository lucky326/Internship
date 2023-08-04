def calculate_gcd(a, b):
    while b:
        remainder = a % b
        a = b
        b = remainder
    return a

def calculate_gcd_list(number_list):
    result = number_list[0]
    for num in number_list[1:]:
        result = calculate_gcd(result, num)
    return result

n = int(input())
if n < 2:
    print("Please enter 2 or more numbers.")
else:
    values = []
    for i in range(n):
        value = int(input("enter some values"))
        values.append(value)
    gcd_result = calculate_gcd_list(values)
    print(gcd_result)

