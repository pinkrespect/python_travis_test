
class Encoder:
    def __init__(self, array):
        # Divisor = 110101
        self.divisor = list()
        for index in range(6):
            if index in [0, 1, 3, 5]:
                self.divisor.append(1)
            else:
                self.divisor.append(0)

        self.dividend = [0 for x in range(len(array)
                                          + len(self.divisor) - 1)]

        for index in range(len(array)):
            self.dividend[index] = array[index]

        self.codeword = [0 for x in range(len(self.dividend))]

    def XOR(self, number1, number2):
        if number1 is number2:
            return 0
        return 1

    def calculate(self, array):
        for i in range(len(self.dividend)-len(self.divisor)):
            if self.dividend[i] is 1:
                for j in range(len(self.divisor)):
                    self.dividend[i+j] = self.XOR(self.divisor[j],
                                                  self.dividend[i+j])

        for i in range(len(array)):
            self.codeword[i] = array[i]

        for i in range(len(self.divisor) - 1):
            self.codeword.append(self.dividend[i + len(array)])

        return self.codeword


encoder = Encoder([1, 0, 1, 0, 0, 0, 1, 1, 0, 1])
CODEWORD = Encoder.calculate(encoder, [1, 0, 1, 0, 0, 0, 1, 1, 0, 1])
print("Codeword: ", CODEWORD)
