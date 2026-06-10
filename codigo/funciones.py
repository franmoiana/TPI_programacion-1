import csv

# ------------------- CARGA Y GUARDADO CSV ---------------------------
def cargar_csv(ruta):
    paises = []
    try:
        with open(ruta, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })
    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    return paises


def guardar_csv(paises, ruta):
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)

# ---------------------- AGREGAR PAIS ------------------------------
def agregar_pais(paises):
    nombre = input("Ingrese el nombre del país: ").strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return

    poblacion = input("Ingrese la población del país: ").strip()

    if not poblacion.isdigit():
        print("Error: la población debe ser un número entero.")
        return

    superficie = input("Ingrese la superficie del país en km²: ").strip()

    if not superficie.isdigit():
        print("Error: la superficie debe ser un número entero.")
        return

    continente = input("Ingrese el continente del país: ").strip()

    if continente == "":
        print("Error: el continente no puede estar vacío.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
    }

    paises.append(nuevo_pais)

    print(f"País '{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()

    pais_encontrado = None

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais_encontrado = pais
            break

    if not pais_encontrado:
        print(f"No se encontró el país '{nombre}'.")
        return

    print("\n¿Qué dato desea actualizar?")
    print("1. Población")
    print("2. Superficie")
    print("3. Población y superficie")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        nueva_poblacion = input(f"Nueva población (actual: {pais_encontrado['poblacion']}): ").strip()

        if nueva_poblacion.isdigit():
            pais_encontrado["poblacion"] = int(nueva_poblacion)
            print(f"Población de '{pais_encontrado['nombre']}' actualizada correctamente.")
        else:
            print("Error: la población debe ser un número entero.")

    elif opcion == "2":
        nueva_superficie = input(f"Nueva superficie (actual: {pais_encontrado['superficie']} km²): ").strip()

        if nueva_superficie.isdigit():
            pais_encontrado["superficie"] = int(nueva_superficie)
            print(f"Superficie de '{pais_encontrado['nombre']}' actualizada correctamente.")
        else:
            print("Error: la superficie debe ser un número entero.")

    elif opcion == "3":
        nueva_poblacion = input(f"Nueva población (actual: {pais_encontrado['poblacion']}): ").strip()
        nueva_superficie = input(f"Nueva superficie (actual: {pais_encontrado['superficie']} km²): ").strip()

        if nueva_poblacion.isdigit() and nueva_superficie.isdigit():
            pais_encontrado["poblacion"] = int(nueva_poblacion)
            pais_encontrado["superficie"] = int(nueva_superficie)
            print(f"País '{pais_encontrado['nombre']}' actualizado correctamente.")
        else:
            print("Error: población y superficie deben ser números enteros.")

    else:
        print("Opción inválida.")

# ----- BUSQUEDA DE PAIS ----

def buscar_por_nombre(paises, texto_busqueda):
    resultados = []

    for pais in paises:
        if texto_busqueda.lower() in pais["nombre"].lower():
            resultados.append(pais)

    return resultados


def mostrar_paises(paises):
    if len(paises) == 0:
        print("No se encontraron países.")
    else:
        for pais in paises:
            print("-------------------------")
            print("Nombre:", pais["nombre"])
            print("Población:", pais["poblacion"])
            print("Superficie:", pais["superficie"], "km²")
            print("Continente:", pais["continente"])

# ---- FILTROS ----

def filtrar_paises(paises):
    print()
    print("¿Cómo desea filtrar los países?")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")

    opcion = input("\nIngrese una opción: ").strip()

    if opcion == "1":
        continente = input("Ingrese el continente: ").strip()
        resultados = filtrar_por_continente(paises, continente)
        mostrar_paises(resultados)

    elif opcion == "2":
        minimo = input("Ingrese población mínima: ").strip()
        maximo = input("Ingrese población máxima: ").strip()

        if minimo.isdigit() and maximo.isdigit():
            resultados = filtrar_por_rango_poblacion(paises, int(minimo), int(maximo))
            mostrar_paises(resultados)
        else:
            print("Error: los valores de población deben ser números enteros.")

    elif opcion == "3":
        minimo = input("Ingrese superficie mínima: ").strip()
        maximo = input("Ingrese superficie máxima: ").strip()

        if minimo.isdigit() and maximo.isdigit():
            resultados = filtrar_por_rango_superficie(paises, int(minimo), int(maximo))
            mostrar_paises(resultados)
        else:
            print("Error: los valores de superficie deben ser números enteros.")

    else:
        print("Opción inválida.")

# ---- ORDENAMIENTOS ---- 

def ordenar_paises(paises):
    print()
    print("¿Por qué criterio desea ordenar?")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion_criterio = input("\nIngrese una opción: ").strip()

    if opcion_criterio == "1":
        criterio = "nombre"
    elif opcion_criterio == "2":
        criterio = "poblacion"
    elif opcion_criterio == "3":
        criterio = "superficie"
    else:
        print("Opción inválida.")
        return

    print()
    print("¿En qué orden desea mostrar los países?")
    print("1. Ascendente")
    print("2. Descendente")

    opcion_orden = input("\nIngrese una opción: ").strip()

    if opcion_orden == "1":
        descendente = False
    elif opcion_orden == "2":
        descendente = True
    else:
        print("Opción inválida.")
        return

    paises_ordenados = ordenar_segun_criterio(paises, criterio, descendente)

    mostrar_paises(paises_ordenados)

# ---- ESTADISTICAS ----

# Min y Max poblacion

def estadistica_mayor_poblacion(paises):
    pais_mayor = max(paises, key=lambda pais: pais["poblacion"])
    return pais_mayor


def estadistica_menor_poblacion(paises):
    pais_menor = min(paises, key=lambda pais: pais["poblacion"])
    return pais_menor


# Promedio poblacion y superficie

def promedio_poblacion(paises):
    total = 0

    for pais in paises:
        total += pais["poblacion"]

    promedio = total / len(paises)

    return promedio


def promedio_superficie(paises):
    total = 0

    for pais in paises:
        total += pais["superficie"]

    promedio = total / len(paises)

    return promedio


# Cantidad de paises por continente

def paises_por_continente(paises):
    continentes = {}

    for pais in paises:
        continente = pais["continente"]

        if continente not in continentes:
            continentes[continente] = 1
        else:
            continentes[continente] += 1

    return continentes


# Mostrar estadisticas generales

def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay países cargados para calcular estadísticas.")
        return

    mayor_poblacion = estadistica_mayor_poblacion(paises)
    menor_poblacion = estadistica_menor_poblacion(paises)
    promedio_pob = promedio_poblacion(paises)
    promedio_sup = promedio_superficie(paises)
    continentes = paises_por_continente(paises)

    print()
    print("----- ESTADÍSTICAS -----")
    print(f"País con mayor población: {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']} habitantes)")
    print(f"País con menor población: {menor_poblacion['nombre']} ({menor_poblacion['poblacion']} habitantes)")
    print(f"Promedio de población: {promedio_pob:.2f} habitantes")
    print(f"Promedio de superficie: {promedio_sup:.2f} km²")

    print()
    print("Cantidad de países por continente:")

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")
