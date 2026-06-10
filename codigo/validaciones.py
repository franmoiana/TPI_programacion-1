def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("Error: el campo no puede estar vacío.")


def pedir_entero_positivo(mensaje):
    while True:
        valor = input(mensaje).strip()

        try:
            numero = int(valor)

            if numero > 0:
                return numero

            print("Error: el número debe ser mayor que cero.")

        except ValueError:
            print("Error: debe ingresar un número entero.")


def pedir_entero_no_negativo(mensaje):
    while True:
        valor = input(mensaje).strip()

        try:
            numero = int(valor)

            if numero >= 0:
                return numero

            print("Error: el número no puede ser negativo.")

        except ValueError:
            print("Error: debe ingresar un número entero.")


def pedir_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()

        if opcion in opciones_validas:
            return opcion

        print("Opción inválida.")


def pedir_rango_no_negativo(mensaje_minimo, mensaje_maximo):
    while True:
        minimo = pedir_entero_no_negativo(mensaje_minimo)
        maximo = pedir_entero_no_negativo(mensaje_maximo)

        if minimo <= maximo:
            return minimo, maximo

        print("Error: el valor mínimo no puede ser mayor que el máximo.")


def validar_fila_csv(fila):
    campos_requeridos = ["nombre", "poblacion", "superficie", "continente"]

    if None in fila:
        return None, "la cantidad de columnas no es correcta"

    for campo in campos_requeridos:
        if campo not in fila or fila[campo] is None:
            return None, f"falta el campo {campo}"

    nombre = fila["nombre"].strip()
    continente = fila["continente"].strip()

    if nombre == "" or continente == "":
        return None, "el nombre y el continente no pueden estar vacíos"

    try:
        poblacion = int(fila["poblacion"])
        superficie = int(fila["superficie"])

    except (TypeError, ValueError):
        return None, "la población y la superficie deben ser números enteros"

    if poblacion <= 0 or superficie <= 0:
        return None, "la población y la superficie deben ser mayores que cero"

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    return pais, None
