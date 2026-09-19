def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def square(number):
    return number * number


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum_result = add(a, b)
product_result = multiply(a, b)
square_result = square(a)

print("Sum:", sum_result)
print("Product:", product_result)
print("Square of first number:", square_result)
