def calculate(input):
    DIVISOR = [1, 1, 0, 1, 0, 1]
    dividend = input + [0] * (len(DIVISOR) - 1)

    for i in range(len(input)):
        if dividend[i] == 0:
            continue
        for j, k in enumerate(DIVISOR):
            dividend[i+j] = k ^ dividend[i+j]

    return input + dividend[len(input):]


ONE = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]
CODEWORD = calculate(ONE)
print("Codeword: ", CODEWORD)
