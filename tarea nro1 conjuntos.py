#ejercicio nro1

def dividir():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    except ValueError:
        print("Error: Debe ingresar un número válido")


dividir()

#ejercicio nro 2

def sumar():
    try:
        num = input("Ingrese un número: ")
        cad = input("Ingrese una cadena: ")
        resultado = int(num) + cad
        print("El resultado de la suma es:", resultado)
    except TypeError:
        print("Error: No se puede sumar un número y una cadena")
    except ValueError:
        print("Error: Debe ingresar un número válido")


sumar()

#ejercicio nro 3

def acceder_diccionario():
    try:
        diccionario = {"nombre": "Juan", "edad": 30}
        clave = input("Ingrese una clave: ")
        valor = diccionario[clave]
        print("El valor de la clave es:", valor)
    except KeyError:
        print("Error: La clave no existe en el diccionario")


acceder_diccionario()

#ejercico nro4

def abrir_archivo():
    try:
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print("El contenido del archivo es:", contenido)
    except FileNotFoundError:
        print("Error: El archivo no existe. Se creará un nuevo archivo.")
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Este es un archivo nuevo.")
            print("El archivo ha sido creado con éxito.")


abrir_archivo()

#ejercico nro5

def dividir():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    except ValueError:
        print("Error: Debe ingresar un número válido")


dividir()
