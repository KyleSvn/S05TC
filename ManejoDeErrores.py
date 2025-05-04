def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Ambos valores deben ser numeros.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None

# Programa principal
print("***Calculadora de Division***")

try:
    num1 = float(input("Ingrese el numerador: "))
    num2 = float(input("Ingrese el denominador: "))
    resultado = dividir(num1, num2)

    if resultado is not None:
        print(f"Resultado: {resultado}")
    else:
        print("No se pudo calcular el resultado.")
except ValueError:
    print("Error: Entrada inválida. Debe ingresar números.")
