
def XOR(number1, number2):
    return 0 if number1 is number2 else 1


def calculate(data):
    divisor = [1, 1, 0, 1, 0, 1]
    dividend = list(data) + [0] * (len(divisor) - 1)
    array = list(data)
    codeword = [0] * len(array)

    for i in range(len(array)):
        if dividend[i] is 1:
            for j, k in enumerate(divisor):
                dividend[i+j] = XOR(k, dividend[i+j])

    for i, j in enumerate(array):
        codeword[i] = j

    for i in range(len(divisor) - 1):
        codeword.append(dividend[i + len(array)])

    print(len(codeword))
    return codeword


one = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]
CODEWORD = calculate(one)
print("Codeword: ", CODEWORD)

