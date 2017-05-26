from test import crc_check

ONE = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]
CODEWORD = crc_check(ONE)
print("Codeword: ", CODEWORD)
