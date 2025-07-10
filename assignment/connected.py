num1 = input("Enter the num1: ")
num2 = input("Enter the num2: ")

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

def access_list_element(lst, index):
    try:
        value = lst[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the list!")

def access_object_attribute(obj):
    try:
        attribute_value = obj.attribute
        print(f"Attribute value: {attribute_value}")
    except AttributeError:
        print("Error: Object does not have the specified attribute!")

def perform_concatenation(str1, num):
    try:
        result = str1 + str(num)  # Convert the number to a string before concatenation
        print(f"Concatenated result: {result}")
    except TypeError as e:
        print(f"Error: {e}")

def calculate_average(nums):
    try:
        total = sum(nums)
        average = total / len(nums)
        print(f"Average of the numbers: {average}")
    except ZeroDivisionError:
        print("Error: Cannot calculate average of an empty list!")

# Logical error example (incorrect average calculation)
def calculate_correct_average(nums):
    try:
        total = sum(nums)
        if len(nums) > 0:
            average = total / len(nums)
            print(f"Average of the numbers: {average}")
        else:
            print("Error: Cannot calculate average of an empty list!")
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":  # Corrected the name of the special variable
    # NameError example
    try:
        print("undefined variable")
    except NameError:
        print("Error: Variable 'undefined_variable' is not defined!")

    # Index and Attribute errors
    my_list = [1, 2, 3]
    my_object = {}
    access_list_element(my_list, 3)  # IndexError
    access_object_attribute(my_object)  # AttributeError

    # Type and logical errors
    perform_concatenation("Hello, ", 123)  # TypeError
    nums = []
    calculate_average(nums)  # ZeroDivisionError (logical error)
    calculate_correct_average(nums)  # Correct average calculation