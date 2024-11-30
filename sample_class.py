class Processing():
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def shori_add(self):
        self.num3 = self.num1 + self.num2
        return self.num1 + self.num2
    
    def shori_sub(self):
        return self.num1 - self.num2
    
    def shori_mul(self):
        return self.num1 * self.num2
    
    def shori_div(self):
        return self.num3 / self.num2
    
    def __secret(self):
        return self.num1 + self.num2 * self.num3
    
    def run(self):
        return self.__secret()
    

test1 = Processing(10, 5)

print(test1.shori_add())
print(test1.shori_sub())
print(test1.shori_mul())
print(test1.shori_div())
print(test1.run())
print("test3:", test1.num3)
