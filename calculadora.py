def calculadora():
    print("Calculadora Básica en Python")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("\nIngresa el número de la operación que deseas realizar (1-5): "))
            if opcion == 5:
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break
            
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == 1:
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcion == 2:
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcion == 3:
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcion == 4:
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Error: No se puede dividir entre cero.")
            else:
                print("Opción no válida. Por favor selecciona una opción del 1 al 5.")
        except ValueError:
            print("Error: Por favor ingresa un número válido.")

calculadora()
