import csv 

def carga_paises_desde_csv(): #Carga los países desde el archivo CSV y devuelve una lista de diccionarios con la información de cada país @Eva Lecuona
    lista_paises = []
    
    try:
        with open("paises.csv", mode="r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if len(lineas) <= 1:
                return lista_paises

            for i in range(1, len(lineas)):
                limpiar_linea = lineas[i].strip()
                if not limpiar_linea:
                    continue
                datos = limpiar_linea.split(",")
                nuevo_pais = {
                    "nombre": datos[0],
                    "poblacion": int(datos[1]),
                    "superficie": int(datos[2]),
                    "continente": datos[3]
                }
                lista_paises.append(nuevo_pais)
                
        print(f"Se cargaron {len(lista_paises)} países desde el archivo")
        
    except FileNotFoundError:
        print("No se encontró el archivo 'paises.csv'. Se inicia con el sistema vacío")
        
    return lista_paises

def pedir_y_validar_texto(texto): #Valida que el campo de texto no esté vacío @Eva Lecuona
    while True:
        campo = input(texto).strip()
        if campo != "": 
            return campo 
        print("Error: Un campo obligatorio no puede estar vacío")


def pedir_y_validar_numero(numero): #Valida que el campo de número sea un entero positivo @Eva Lecuona
    while True:
        try:
            campo = input(numero)
            numero = int(campo)
            if numero > 0:
                return numero
            print("Error: El número debe ser mayor a cero")
        except ValueError:
            print("Error: Ingresa un número entero válido")

def agregar_pais(lista_paises): #Pide al usuario los datos de un nuevo país, los valida y los agrega a la lista de países @Eva Lecuona
    nombre = pedir_y_validar_texto("Ingresa el nombre del país: ")
    continente = pedir_y_validar_texto("Ingresa el continente: ")
    poblacion = pedir_y_validar_numero("Ingresa la población: ")
    superficie = pedir_y_validar_numero("Ingresa la superficie (en km2): ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista_paises.append(nuevo_pais)
    print(f"\nEl país {nombre} se agregó correctamente a la lista")



def actualizar_poblacion(pais): #Pide al usuario la nueva población para un país, la valida y actualiza el valor en el diccionario @Eva Lecuona
    print(f"\nPoblación actual de {pais['nombre']}: {pais['poblacion']}")
    nueva_poblacion = pedir_y_validar_numero("Ingresa la nueva población: ")

    pais["poblacion"] = nueva_poblacion
    print("Población modificada con éxito!")

def actualizar_superficie(pais): #Pide al usuario la nueva superficie para un país, la valida y actualiza el valor en el diccionario @Eva Lecuona
    print(f"Superficie actual de {pais['nombre']}: {pais['superficie']} km2")
    nueva_superficie = pedir_y_validar_numero("Ingresa la nueva superficie (en km2): ")

    pais["superficie"] = nueva_superficie
    print("Superficie modificada con éxito")

    
def buscar_pais_por_nombre(lista_paises): #Pide al usuario un nombre, lo busca en la lista de países y muestra los datos de los países que coincidan con la búsqueda @Eva Lecuona
    busqueda = pedir_y_validar_texto("Ingresa el nombre a buscar: ").lower()
    contador_coincidencia = 0

    for pais in lista_paises:
        if busqueda in pais["nombre"].lower():
            print(f"{pais['nombre']},Continente: {pais['continente']},Población: {pais['poblacion']},Superficie: {pais['superficie']} km2")
            contador_coincidencia += 1
    if contador_coincidencia == 0:
        print("No se encontraron países que coincidan con la búsqueda")





def actualizar_datos_pais(lista_paises): #Pide al usuario el nombre, lo busca en la lista de países y si lo encuentra, actualiza su población y superficie @Eva Lecuona
    nombre_buscar = pedir_y_validar_texto("Ingresa el nombre del país a modificar: ").lower()
    pais_encontrado = None

    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar.lower():
            pais_encontrado = pais
            break

    if pais_encontrado != None:
        print(f"\nPaís encontrado: {pais_encontrado['nombre']}")
        actualizar_poblacion(pais_encontrado)
        actualizar_superficie(pais_encontrado)
        
        print(f"\nLos datos de {pais_encontrado['nombre']} se actualizaron correctamente")
    else:
        print("No se encontró ningún país con ese nombre en el sistema")



def menu_principal(): #Muestra el menú principal @Eva Lecuona
    print("\n--- SISTEMA DE GESTIÓN MUNDIAL ---")
    print("1. Agregar un nuevo país")
    print("2. Actualizar población y superficie de un país")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países (Continente / Población / Superficie)")
    print("5. Ordenar países [Compañero]")
    print("6. Mostrar estadísticas generales")
    print("7. Guardar y Salir")


def ejecutar_menu(): #Ejecuta el menú principal y maneja las opciones seleccionadas por el usuario @Eva Lecuona
    lista_paises = carga_paises_desde_csv()
    
    while True:
        menu_principal()
        opcion = input("").strip()
        
        if opcion == "1":
            print("")
            agregar_pais(lista_paises)
        elif opcion == "2":
            print("")
            actualizar_datos_pais(lista_paises)
        elif opcion == "3":
            print("")
            buscar_pais_por_nombre(lista_paises)
        elif opcion == "4":
            print("")
            
        elif opcion == "5":
            print("")
            
        elif opcion == "6":
            print("")
            
        elif opcion == "7":
            print("")
            break
        else:
            print("\nOpción inválida. Elegí un número del 1 al 7")

# Inicia el programa:
if __name__ == "__main__":
    ejecutar_menu()

