def sum_two_numbers(first_number, second_number):
    if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
        raise ValueError("Both inputs must be numeric (int or float).")
    return first_number + second_number

x = 10

if __name__ == "__main__":
    try:
        print("Sum of")
        print("Two numbers: ", sum_two_numbers(10, "TEST"))
    except ValueError as e:
        print("Error:", e)
