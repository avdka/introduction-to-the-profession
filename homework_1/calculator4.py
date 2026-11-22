class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def devide(self, a, b):
        return a / b
    
    def math_operation(self):
        print()
        print("Введите первое число:")
        a = int(input())
        print("Введите второе число:")
        b = int(input())
        print("Введите нужную операцию:")
        c = input()
        print("Результат:")
        if c == "+":
            return(self.add(a, b))
        elif c == "-":
            return(self.subtract(a, b))
        elif c == "*":
            return(self.multiply(a, b))
        else:
            return(self.devide(a, b))     
        
    def IMT(self):
        print()
        print("Введите вес (кг):")
        m = float(input())
        print("Введите рост (м):")
        h = float(input())
        print("Результат:")        
        imt = round(self.devide(m, self.multiply(h, h)), 2)
        return imt
    
    def start(self):
        while True:
            print()
            print("Выберите калькулятор, введя соответствующее число: ")
            print("1 - стандартный калькулятор")
            print("2 - калькулятор ИМТ")
            choice = input()
            if choice == "1":
                print(self.math_operation())
            else:
                print(self.IMT())

calc = Calculator()
calc.start()