def soma(a, b):
    return a + b
def sub(a, b):
    return a - b

if __name__ == "__main__":
    print("--- Calculadora Simples ---")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operador = input("Digite o operador (+, -): ")

        if operador == '+':
            resultado = soma(num1, num2)
        elif operador == '-':
            resultado = sub(num1, num2)
        else:
            resultado = "Operador inválido."

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, digite números.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")