def sum_two_number(first_num, num_second):
    if not isinstance(first_num, (int, float)) or not isinstance(num_second, (int, float)):
        raise ValueError("Both inputs must be numeric.")
    return first_num + num_second

if __name__ == "__main__":
    try:
        print("Sum of two numbers:", sum_two_number(10, 20))
    except ValueError as e:
        print("Error:", e)
