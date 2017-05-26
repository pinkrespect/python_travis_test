from crc import crc_check


def test(input, expected_output):
    if crc_check(input) == expected_output:
        print(" SUCCESS ")
    else:
        print(" FAILED ")

