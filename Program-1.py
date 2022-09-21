class Calculator:
    def __init__(self, a, b, operation):
        self.a = int(a)
        self.b = int(b)
        self.operation = operation

    def calculate(self):
        if(self.operation.lower() == 'addition'):
            return self.a + self.b
        if(self.operation.lower() == 'subtraction'):
            return self.a - self.b
        if(self.operation.lower() == 'multiplication'):
            return self.a * self.b
        if(self.operation.lower() == 'division'):
            return self.a/self.b

# User Inputs
print('Please enter the values')
a = input('Enter "a" value: ')
b = input('Enter "b" value: ')
operation = input('Enter type of operation: ')


obj = Calculator(a, b, operation)
ans = obj.calculate()
print('{0} operation answer => {1}'.format(operation, ans))



        
