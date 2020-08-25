try:
    denominator = 0
    numerator = int(input("Enter the numerator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Input a valid integer")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# A value error will occur when the value entered is not an integer or a value isn't entered at all
# When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur when the denominator is entered as 0 because the function will then
# divide the numerator by 0
