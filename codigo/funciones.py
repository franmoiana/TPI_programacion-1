import csv

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

# ---- Actualizar Pais -----
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

# ----- Actualizar poblacion -----


    nueva_poblacion = input(f"Nueva población (actual: {pais_encontrado['poblacion']}) [Enter para no cambiar]: ").strip()
    if nueva_poblacion.isdigit():
        pais_encontrado["poblacion"] = int(nueva_poblacion)

# ----- Actualizar superficie -----

    nueva_superficie = input(f"Nueva superficie (actual: {pais_encontrado['superficie']} km²) [Enter para no cambiar]: ").strip()
    if nueva_superficie.isdigit():
        pais_encontrado["superficie"] = int(nueva_superficie)

    print(f"País '{pais_encontrado['nombre']}' actualizado correctamente.")

# ----- BUSQUEDA DE PAIS ----

def buscar_pais(paises, texto_busqueda):
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

busqueda = input("Ingrese el nombre del país: ")

resultados = buscar_pais(paises, busqueda)

mostrar_paises(resultados)

# ---- FILTROS ----

def filtrar_por_continente(paises, busqueda_continente):
    resultados = []

    for pais in paises:
        if busqueda_continente.lower().strip() == pais["continente"].lower():
            resultados.append(pais)

    return resultados

def filtrar_por_rango_poblacion(paises, busqueda_poblacion_min, busqueda_poblacion_max ):
    resultados = []

    for pais in paises:
        if busqueda_poblacion_min <= pais["poblacion"] <= busqueda_poblacion_max:
            resultados.append(pais)

    return resultados

def filtrar_por_rango_superficie(paises, busqueda_superficie_min, busqueda_superficie_max ):
    resultados = []

    for pais in paises:
        if busqueda_superficie_min <= pais["superficie"] <= busqueda_superficie_max:
            resultados.append(pais)

    return resultados

# ---- ORDENAMIENTOS ---- 

def ordenar_segun_criterio(paises, criterio, descendente):

    if criterio == "nombre":
        orden_nombre = sorted(paises, key=lambda pais: pais["nombre"], reverse=descendente)
        return orden_nombre
    
    elif criterio == "poblacion":
        orden_poblacion = sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)
        return orden_poblacion
    
    elif criterio == "superficie":
        orden_superficie = sorted(paises, key=lambda pais: pais["superficie"], reverse=descendente)
        return orden_superficie
    
    else:
        print("Criterio incorrecto")
        return []

# ---- ESTADISTICAS ----

# Min y Max poblacion

def estadistica_mayor_poblacion(paises):
    pais_mayor = max(paises, key=lambda pais: pais["poblacion"])
    return pais_mayor

def estadistica_menor_poblacion(paises):
    pais_menor = min(paises, key=lambda pais : pais["poblacion"])
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
