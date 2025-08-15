def enter_number(prompt_message):
    """
    Prompt the user to enter a number (integer or float).

    Args:
        prompt_message (str): The message displayed to the user when asking for input.

    Returns:
        float: The valid number entered by the user (int values are converted to float).
    """
    while True:
        user_input = input(prompt_message).strip()
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 5, 3.14, -2.7).")

if __name__ == "__main__":
    num1 = enter_number("Please enter the first number: ")
    num2 = enter_number("Please enter the second number: ")
    print(f"\nThe sum of {num1} and {num2} is: {num1 + num2}")
