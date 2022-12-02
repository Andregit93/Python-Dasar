class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

num1 = ComplexNumber(2, 3)

num1.get_data()

num2 = ComplexNumber(5)
num2.attr = "10"

print((num2.real, num2.imag, num2.attr))
