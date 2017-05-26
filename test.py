def calculate(array):
    divisor = [1, 1, 0, 1, 0, 1]
    dividend = array + [0] * (len(divisor) - 1)

    for i in range(len(array)):
        if dividend[i] == 1:
            for j, k in enumerate(divisor):
                dividend[i+j] = 0 if k == dividend[i+j] else 1

    return array + dividend[len(array):]


one = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]
CODEWORD = calculate(one)
print("Codeword: ", CODEWORD)
