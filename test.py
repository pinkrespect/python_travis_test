
class Encoder:
    def __init__(self, array):
        self.divisor = [1, 1, 0, 1, 0, 1]
        self.dividend = list(array) + [0] * (len(self.divisor) - 1)
    
    @staticmethod
    def XOR(number1, number2):
        return 0 if number1 is number2 else 1

    def calculate(self, array):
        codeword = [0] * len(self.dividend)
        for i in range(len(self.dividend)-len(self.divisor)):
            if self.dividend[i] is 1:
                for j in range(len(self.divisor)):
                    self.dividend[i+j] = Encoder.XOR(self.divisor[j],
                                                     self.dividend[i+j])

        for i in range(len(array)):
            codeword[i] = array[i]

        for i in range(len(self.divisor) - 1):
            codeword.append(self.dividend[i + len(array)])

        return codeword


encoder = Encoder([1, 0, 1, 0, 0, 0, 1, 1, 0, 1])
CODEWORD = encoder.calculate([1, 0, 1, 0, 0, 0, 1, 1, 0, 1])
print("Codeword: ", CODEWORD)

