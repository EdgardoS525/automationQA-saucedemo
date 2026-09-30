def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    else:
        return a / b

def calculadora():
    try:
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))

        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")

        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                resultado = suma(numero1,numero2)
            case "2":
                resultado = resta(numero1,numero2)
            case "3":
                resultado = multiplicacion(numero1,numero2)
            case "4":
                resultado = division(numero1,numero2)

            case _:
                print("Opcion invalida")

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: Debe ingresar numeros validos")

    except ZeroDivisionError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    calculadora()
