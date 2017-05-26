def crc_check(input):
    """ crc_check(input)
    Cyclic Redundacy Check with fixed-number of divisor.
    Divisor array fixed 6 number.
    Input data: A array of 0s and 1s that longer then DIVISOR.
    Return data: A array consiste Input + Remainder.
    Calculate (dividend's length - divisor's length - 1) times.
    """
    DIVISOR = [1, 1, 0, 1, 0, 1]
    dividend = input + [0] * (len(DIVISOR) - 1)

    for i in range(len(input)):
        if dividend[i] == 0:  # No need to xor operation.
            continue
        for j, k in enumerate(DIVISOR):  # Need to xor operation.
            dividend[i+j] = k ^ dividend[i+j]

    return input + dividend[len(input):]  # return input + remainder.
