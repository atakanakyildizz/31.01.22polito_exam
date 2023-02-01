number1 = "C1A0"
number2 = "1010"


def question2(number_in_hex):
    decimalnumber1 = int(number_in_hex, 16)
    print(decimalnumber1)
    octnumber1 = oct(decimalnumber1)
    binarynumber1 = bin(decimalnumber1)
    print(f"The number = {number_in_hex}\n"
          f"Base 8 number = {octnumber1}\n"
          f"Base 2 number = {binarynumber1}\n"
          f"----------------------------------")


if __name__ == '__main__':
    question2(number1)
    question2(number2)
