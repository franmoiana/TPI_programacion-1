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
