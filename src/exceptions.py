x = 0
try:
    # print(x / 0)
    if not isinstance(x, str):
        # raising an error manually
        raise TypeError("'x' must be a string")
except NameError as e:
    # print("Variable 'x' is not defined")
    print(e)
except ZeroDivisionError as e:
    # print("Dividing by zero is not defined")
    print(e)
except Exception as e:
    # print("An error occurred:", e)
    print(e)
else:
    print("Division successful")
finally:
    print("The 'finally' block always executes ea qarw ergtrg asf wetwerw sdfsdf werwer")