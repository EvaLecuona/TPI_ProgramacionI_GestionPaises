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

    
def buscar_pais_coincidencia_parcial(lista_paises):#Busca países con coincidencias parciales @Eva Lecuona
    busqueda = pedir_y_validar_texto("Ingresa el nombre a buscar: ").lower()
    contador_coincidencia = 0

    for pais in lista_paises:
        if busqueda in pais["nombre"].lower():
            print(f"{pais['nombre']},Continente: {pais['continente']},Población: {pais['poblacion']},Superficie: {pais['superficie']} km2")
            contador_coincidencia += 1
    if contador_coincidencia == 0:
        print("No se encontraron países que coincidan con la búsqueda")

def buscar_pais_coincidencia_exacta(lista_paises): #Busca un país con coincidencia exacta @Eva Lecuona
    busqueda = pedir_y_validar_texto("Ingresa el nombre exacto del país a buscar: ").lower()
    contador_coincidencia = 0

    for pais in lista_paises:
        if busqueda == pais["nombre"].lower():
            print(f"{pais['nombre']}, Continente: {pais['continente']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']} km2")
            contador_coincidencia += 1
            break
            
    if contador_coincidencia == 0:
        print("No se encontró ningún país con ese nombre exacto")


def menu_busqueda_por_nombre(lista_paises): #Muestra un submenú para elegir entre búsqueda por coincidencia parcial o exacta @Eva Lecuona
    print("\nIngresa el tipo de búsqueda por nombre que deseas realizar:")
    print("1. Búsqueda por coincidencia parcial")
    print("2. Búsqueda por coincidencia exacta")

    opcion = input("Selecciona una opción: ").strip()
    while opcion != "1" and opcion != "2":
        print("Opción inválida: Ingresa 1 o 2")
        opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        buscar_pais_coincidencia_parcial(lista_paises)
    else:
        buscar_pais_coincidencia_exacta(lista_paises)

def buscar_objeto_pais(lista_paises, nombre_buscar): #Busca un país por nombre y devuelve el diccionario completo del país encontrado. Si no lo encuentra, lanza una excepción @Eva Lecuona
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar.lower():
            return pais
    raise ValueError("No se encontró ningún país con ese nombre en el sistema")

def actualizar_datos_pais(lista_paises): #Actualiza la población y superficie de un país encontrado por nombre. Si no encuentra el país, muestra un mensaje de error y vuelve a pedir el nombre @Eva Lecuona
    while True:
        nombre_buscar = pedir_y_validar_texto("Ingresa el nombre del país a modificar: ")
        
        try:
            pais_encontrado = buscar_objeto_pais(lista_paises, nombre_buscar)
            print(f"\nPaís encontrado: {pais_encontrado['nombre']}")
            actualizar_poblacion(pais_encontrado)
            actualizar_superficie(pais_encontrado)

            print(f"\nLos datos de {pais_encontrado['nombre']} se actualizaron correctamente")
            break
            
        except ValueError as e:
            print(f"Error: {e}.Intenta de nuevo\n")


def filtrar_pais_por_continente(lista_paises): #Filtra los países por continente @Eva Lecuona
    continente_buscar = pedir_y_validar_texto("Ingresa el continente a filtrar: ").lower()
    contador_paises = 0
    
    print(f"\nPaíses en el continente '{continente_buscar.capitalize()}':")
    for pais in lista_paises:
        if pais["continente"].lower() == continente_buscar:
            print(f"- {pais['nombre']},Población: {pais['poblacion']},Superficie: {pais['superficie']} km2")
            contador_paises += 1
            
    if contador_paises == 0:
        print("No se encontraron países en ese continente")

def filtrar_pais_por_rango_poblacion(lista_paises): #Filtra los países por un rango de población ingresado por el usuario @Eva Lecuona
    minimo = pedir_y_validar_numero("Ingresa la población Mínima: ")
    maximo = pedir_y_validar_numero("Ingresa la población Maxima: ")

    while minimo > maximo:
        print("Error: La población mínima no puede ser mayor a la máxima")
        minimo = pedir_y_validar_numero("Ingresa la población Mínima nuevamente: ")
        maximo = pedir_y_validar_numero("Ingresa la población Maxima nuevamente: ")

    contador = 0
    for pais in lista_paises:
        if minimo <= pais["poblacion"] <= maximo:
            print(f"- {pais['nombre']},Continente: {pais['continente']},Población: {pais['poblacion']}")
            contador += 1
            
    if contador == 0:
        print("No se encontraron países en ese rango de población")


def filtrar_pais_por_rango_superficie(lista_paises): #Filtra los países por un rango de superficie ingresado por el usuario @Eva Lecuona
    minimo = pedir_y_validar_numero("Ingresa la superficie Minima (en km²): ")
    maximo = pedir_y_validar_numero("Ingresa la superficie Máxima (en km²): ")

    while minimo > maximo:
        print("Error: La superficie mínima no puede ser mayor a la máxima")
        minimo = pedir_y_validar_numero("Ingresa la superficie Minima nuevamente: ")
        maximo = pedir_y_validar_numero("Ingresa la superficie Máxima nuevamente: ")

    contador = 0
    for pais in lista_paises:
        if minimo <= pais["superficie"] <= maximo:
            print(f"- {pais['nombre']} ,Continente: {pais['continente']},Superficie: {pais['superficie']} km2")
            contador += 1
            
    if contador == 0:
        print("No se encontraron países en ese rango de superficie")


def menu_filtros_por_rango(lista_paises): #Muestra un submenú para elegir entre filtrar por población o superficie @Eva Lecuona
    print("\nIngresa la opción de filtro por rango que deseas aplicar:")
    print("1. Filtrar por rango de Población")
    print("2. Filtrar por rango de Superficie")

    opcion = input("Selecciona una opción: ").strip()
    while opcion != "1" and opcion != "2":
        print("Opción inválida: Ingresa 1 o 2")
        opcion = input("Selecciona una opción: ").strip()
    if opcion == "1":
        filtrar_pais_por_rango_poblacion(lista_paises)
    else:
        filtrar_pais_por_rango_superficie(lista_paises)




def menu_principal(): #Muestra el menú principal @Eva Lecuona
    print("\n--- SISTEMA DE GESTIÓN MUNDIAL ---")
    print("1. Agregar un nuevo país")
    print("2. Actualizar población y superficie de un país")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países (Continente / Población / Superficie)")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas generales")
    print("7. Guardar y Salir")

def menu_filtros(lista_paises): #Submenú de filtros: continente, población o superficie @Nieves Sofia Macarena
    print("\nSelecciona el tipo de filtro:")
    print("1. Filtrar por Continente")
    print("2. Filtrar por rango de Población")
    print("3. Filtrar por rango de Superficie")

    opcion = input("Selecciona una opción: ").strip()
    while opcion not in ("1", "2", "3"):
        print("Opción inválida. Ingresa 1, 2 o 3")
        opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        filtrar_pais_por_continente(lista_paises)
    elif opcion == "2":
        filtrar_pais_por_rango_poblacion(lista_paises)
    else:
        filtrar_pais_por_rango_superficie(lista_paises)


def elegir_direccion(): #Pregunta al usuario si quiere orden ascendente o descendente @Nieves Sofia Macarena
    print("¿En qué orden?")
    print("1. Ascendente")
    print("2. Descendente")

    opcion = input("Selecciona una opción: ").strip()
    while opcion not in ("1", "2"):
        print("Opción inválida. Ingresa 1 o 2")
        opcion = input("Selecciona una opción: ").strip()

    return opcion == "2"


def mostrar_lista_ordenada(lista_ordenada): #Imprime en consola la lista de países ya ordenada @Nieves Sofia Macarena
    for pais in lista_ordenada:
        print(f"- {pais['nombre']}, Continente: {pais['continente']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']} km2")


def ordenar_por_nombre(lista_paises): #Ordena los países por nombre asc o desc @Nieves Sofia Macarena
    descendente = elegir_direccion()
    lista_ordenada = sorted(lista_paises, key=lambda p: p["nombre"].lower(), reverse=descendente)
    direccion = "descendente" if descendente else "ascendente"
    print(f"\nPaíses ordenados por nombre ({direccion}):")
    mostrar_lista_ordenada(lista_ordenada)


def ordenar_por_poblacion(lista_paises): #Ordena los países por población asc o desc @Nieves Sofia Macarena
    descendente = elegir_direccion()
    lista_ordenada = sorted(lista_paises, key=lambda p: p["poblacion"], reverse=descendente)
    direccion = "descendente" if descendente else "ascendente"
    print(f"\nPaíses ordenados por población ({direccion}):")
    mostrar_lista_ordenada(lista_ordenada)


def ordenar_por_superficie(lista_paises): #Ordena los países por superficie asc o desc @Nieves Sofia Macarena
    descendente = elegir_direccion()
    lista_ordenada = sorted(lista_paises, key=lambda p: p["superficie"], reverse=descendente)
    direccion = "descendente" if descendente else "ascendente"
    print(f"\nPaíses ordenados por superficie ({direccion}):")
    mostrar_lista_ordenada(lista_ordenada)


def menu_ordenamiento(lista_paises): #Submenú de ordenamiento: nombre, población o superficie @Nieves Sofia Macarena
    if not lista_paises:
        print("No hay países cargados para ordenar")
        return

    print("\nOrdenar países por:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Selecciona una opción: ").strip()
    while opcion not in ("1", "2", "3"):
        print("Opción inválida. Ingresa 1, 2 o 3")
        opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        ordenar_por_nombre(lista_paises)
    elif opcion == "2":
        ordenar_por_poblacion(lista_paises)
    else:
        ordenar_por_superficie(lista_paises)


def pais_mayor_poblacion(lista_paises): #Devuelve el país con mayor población @Nieves Sofia Macarena
    return max(lista_paises, key=lambda p: p["poblacion"])


def pais_menor_poblacion(lista_paises): #Devuelve el país con menor población @Nieves Sofia Macarena
    return min(lista_paises, key=lambda p: p["poblacion"])


def promedio_poblacion(lista_paises): #Calcula el promedio de población @Nieves Sofia Macarena
    total = sum(p["poblacion"] for p in lista_paises)
    return total / len(lista_paises)


def promedio_superficie(lista_paises): #Calcula el promedio de superficie @Nieves Sofia Macarena
    total = sum(p["superficie"] for p in lista_paises)
    return total / len(lista_paises)


def cantidad_por_continente(lista_paises): #Cuenta cuántos países hay por continente @Nieves Sofia Macarena
    conteo = {}
    for pais in lista_paises:
        continente = pais["continente"]
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1
    return conteo


def mostrar_estadisticas(lista_paises): #Muestra todas las estadísticas generales @Nieves Sofia Macarena
    if not lista_paises:
        print("No hay países cargados para mostrar estadísticas")
        return

    mayor = pais_mayor_poblacion(lista_paises)
    menor = pais_menor_poblacion(lista_paises)
    prom_pob = promedio_poblacion(lista_paises)
    prom_sup = promedio_superficie(lista_paises)
    por_continente = cantidad_por_continente(lista_paises)

    print("\n--- ESTADÍSTICAS GENERALES ---")
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']} habitantes)")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']} habitantes)")
    print(f"Promedio de población:    {prom_pob:,.0f} habitantes")
    print(f"Promedio de superficie:   {prom_sup:,.0f} km2")
    print("\nCantidad de países por continente:")
    for continente, cantidad in por_continente.items():
        print(f"  - {continente}: {cantidad} país/es")


def guardar_paises_en_csv(lista_paises): #Guarda todos los países en el archivo CSV @Nieves Sofia Macarena
    try:
        with open("paises.csv", mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            escritor.writeheader()
            escritor.writerows(lista_paises)
        print("Los datos se guardaron correctamente en 'paises.csv'")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

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
            menu_busqueda_por_nombre(lista_paises)
        elif opcion == "4":
            print("")
            menu_filtros(lista_paises)
        elif opcion == "5":
            print("")
            menu_ordenamiento(lista_paises)
        elif opcion == "6":
            print("")
            mostrar_estadisticas(lista_paises)
        elif opcion == "7":
            print("")
            guardar_paises_en_csv(lista_paises)
            break
        else:
            print("\nOpción inválida. Elegí un número del 1 al 7")

# Inicia el programa:
if __name__ == "__main__":
    ejecutar_menu()

