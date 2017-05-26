class Encoder:
    def __init__(self, array):
        self.divisor = [1, 1, 0, 1, 0, 1]
        self.dividend = list(array) + [0] * (len(self.divisor) - 1)
        self.array = list(array)

    @staticmethod
    def XOR(number1, number2):
        return 0 if number1 is number2 else 1

    def calculate(self):
        dividend = list(self.dividend)
        codeword = [0] * len(self.array)

        for i in range(len(self.array)):
            if dividend[i] is 1:
                for j in range(len(self.divisor)):
                    dividend[i+j] = Encoder.XOR(self.divisor[j], dividend[i+j])

        for i in range(len(self.array)):
            codeword[i] = self.array[i]

        for i in range(len(self.divisor) - 1):
            codeword.append(dividend[i + len(self.array)])

        print(len(codeword))
        return codeword


data = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]
encoder = Encoder(data)
CODEWORD = encoder.calculate()
print("Codeword: ", CODEWORD)

