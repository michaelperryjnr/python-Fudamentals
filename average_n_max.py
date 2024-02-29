def calculate_average(numbers):
    a = sum(numbers)
    average = sum(numbers) / len(numbers)
    return average
def find_maximum(numbers):
    maximum = max(numbers)
    return maximum
numbers = [float(x) for x in input("Enter your list of numbers separating each number with ',' \n").split(",")]
number_list = f"Your numbers are: {numbers}"
print(number_list)
final_average = f"The average is: {calculate_average(numbers)}"
print(final_average)
max_value = f"The maximum value is: {find_maximum(numbers)}"
print(max_value)
print("GoodBye Now")
print("Don't forget to star and contribute")