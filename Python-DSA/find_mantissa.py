def find_mantissa(num):
    # Convert the number to a string
    num_str = str(num)

    # Find the index of the decimal point
    decimal_index = num_str.find('.')

    # If there is no decimal point, return 0 as mantissa
    if decimal_index == -1:
        return 0

    # Extract the mantissa part from the string
    mantissa_str = num_str[decimal_index + 1:]

    # Convert the mantissa string back to a float
    mantissa = float("0." + mantissa_str)

    return mantissa

def main():
    num = float(input("Enter a floating-point number: "))
    mantissa = find_mantissa(num)
    print("Mantissa:", mantissa)

if __name__ == "__main__":
    main()
