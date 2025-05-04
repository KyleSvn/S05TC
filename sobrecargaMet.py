class Calculadora:
    def sumar(self, a, b=0, c=0):
        return a + b + c

# Creacion de la clase
calc = Calculadora()

# Sobrecarga
print("Suma de 1 número:", calc.sumar(5))         
print("Suma de 2 números:", calc.sumar(5, 3))      
print("Suma de 3 números:", calc.sumar(5, 3, 2))   