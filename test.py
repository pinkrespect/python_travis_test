def XOR(number1, number2):
    return 0 if number1 is number2 else 1


def calculate(array):
    divisor = [1, 1, 0, 1, 0, 1]
    dividend = array + [0] * (len(divisor) - 1)
    codeword = [0] * len(array)

    for i in range(len(array)):
        if dividend[i] == 1:
            for j, k in enumerate(divisor):
                dividend[i+j] = XOR(k, dividend[i+j])

    codeword = list(array)

    for i in range(len(divisor) - 1):
        codeword.append(dividend[i + len(array)])

    return codeword


one = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]
CODEWORD = calculate(one)
print("Codeword: ", CODEWORD)
