from funciones import *

# ------- Estructura general del menu -----

def menu():
    while True:
        print("\n=== Gestión de Países ===")
        print("1. Agregar país")
        print("2. Actualizar poblacion o superficie")
        print("3. Buscar país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Estadísticas")
        print("0. Salir")

        opcion = input("\nIngrese una opción: ").strip()

        if opcion == "1":
            print()
            agregar_pais(paises)
            guardar_csv(paises, "paises.csv")
        elif opcion == "2":
            actualizar_pais(paises)
            guardar_csv(paises, "paises.csv")
        elif opcion == "3":
            texto_busqueda = input("Ingrese el nombre del país a buscar: ").strip()
            resultados = buscar_por_nombre(paises, texto_busqueda)
            mostrar_paises(resultados)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

paises = cargar_csv("paises.csv")
menu()