from crc import crc_check


def test(input, expected_output):
    if crc_check(input) == expected_output:
        print(" SUCCESS ")
    else:
        print(" FAILED ")
        exit(1)


test([1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0])
test([1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
     [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0])
test([1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1])
test([1], [1, 1, 0, 1, 0, 1])
