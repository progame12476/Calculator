import math
import os
os.system("color 0F")

while True:
    print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿ version march20 /2025 ⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")

    print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿  Welcome to my calculator ⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")

    try:
        first = float(input("What's the first number? "))
        second = float(input("What's the second number? "))
        operation = input("What should I do? (+, -, *, /) ")

        if operation == '+':
            result = first + second
        elif operation == '-':
            result = first - second
        elif operation == '*':
            result = first * second
        elif operation == '/':
            if second != 0:
                result = first / second
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operation"

        total_length = 31 
        buffer_length_for_first = total_length - len("First number:") - len(str(first))
        buffer = "=" * buffer_length_for_first
        buffer_length_for_second = total_length - len("Second number:") - len(str(second))
        second_buffer = "=" * buffer_length_for_second
        buffer_length_for_result = total_length - len("Result:") - len(str(result))
        result_buffer = "=" * buffer_length_for_result  

        print(f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
First number:{buffer}{first}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
Second number:{second_buffer}{second}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
Result: {result_buffer} {result}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")

    except ValueError:
        print("Error: Please enter valid numbers.")

    restart = input("Do you want to close the calculator? (yes/no): ").lower()
    if restart != "no":
        print("Bye!")
        break