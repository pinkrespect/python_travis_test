def crc_check(input):
    """ crc_check(input)
    Cyclic redundacy check with fixed-number of divisor.
    Input data: array, 1010001101
    Return data: array, 101000110101110 (Input data + Remainder)
    Operate (dividend's length - divisor's length - 1) times.
    """
    DIVISOR = [1, 1, 0, 1, 0, 1]
    dividend = input + [0] * (len(DIVISOR) - 1)

    for i in range(len(input)):
        if dividend[i] == 0:  # No need to xor operation.
            continue
        for j, k in enumerate(DIVISOR):  # Need to xor operation.
            dividend[i+j] = k ^ dividend[i+j]

    return input + dividend[len(input):]
