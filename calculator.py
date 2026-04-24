def sum_two_number(first_num, num_second):
    if not isinstance(first_num, (int, float)) or not isinstance(num_second, (int, float)):
        raise ValueError("Both inputs must be numeric.")
    return first_num + num_second

x = 10

if __name__ == "__main__":
    print("Sum of two numbers:")
    try:
        print("Result: ", sum_two_number(10, 20))
    except ValueError as e:
        print("Error:", e)
