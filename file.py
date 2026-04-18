def sum_two_numbers(first_num, second_num):
    if not isinstance(first_num, (int, float)) or not isinstance(second_num, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return first_num + second_num

if __name__ == "__main__":
    try:
        print("Sum of two numbers:", sum_two_numbers(10, 20))
    except ValueError as e:
        print("Error:", e)