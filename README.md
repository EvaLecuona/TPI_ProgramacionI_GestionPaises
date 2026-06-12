# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**  
Tecnicatura Universitaria en Programación (TUP) — UTN a Distancia


## Descripción

Aplicación de consola en Python que permite gestionar un dataset de países cargado desde un archivo CSV. Implementa búsquedas, filtros, ordenamientos y estadísticas utilizando listas, diccionarios y funciones modulares.

## Integrantes

| Nombre | Legajo |
|--------|--------|
| Lecuona Gonzalez Eva | 612.507|
| Nieves Sofia Macarena| - |

## Estructura del proyecto

```
tpi_prog1/
├── TPI_Grupal_Prog-1.py          # Código fuente principal
├── paises.csv                    # Dataset base (50 países)
└── README.md                     # Este archivo
```

## Cómo ejecutar

**Requisitos:** Python

```bash
# Clonar el repositorio
git clone https://github.com/EvaLecuona/TPI_ProgramacionI_GestionPaises
cd [repositorio]

# Ejecutar el programa
python3 TPI_Grupal_Prog-1.py
```

## Menú de opciones

```
   GESTIÓN DE DATOS DE PAÍSES - TPI UTN TUP
1. Agregar un nuevo país
2. Actualizar población y superficie de un país
3. Buscar un país por nombre
4. Filtrar países (Continente / Población / Superficie)
5. Ordenar países
6. Mostrar estadísticas generales
7. Guardar y Salir
```

## Instrucciones de Ejecución

Para correr el programa, asegurarse de tener instalado Python 3 y seguir estos pasos desde la terminal:

1. **Descargar los archivos:** Asegurarse de tener en la misma carpeta el archivo principal (`TPI_Grupal_Prog-1.py`), el módulo de funciones y el archivo de datos `paises.csv`.
2. **Abrir la terminal:** Navegar hasta la carpeta del proyecto.
3. **Ejecutar el programa:** Correr el siguiente comando:
```bash
   python TPI_Grupal_Prog-1.py

```

## Guía de Opciones del Menú
El sistema cuenta con un menú interactivo validado para evitar ingresos erróneos. Se detalla qué incluye y cómo funciona cada una de las opciones principales:

## 1. Agregar un nuevo país
Qué hace: Permite dar de alta un país que no esté registrado en el sistema.

Cómo funciona: Solicita de forma secuencial el nombre, la población, la superficie y el continente. Utiliza funciones de validación para garantizar que las cadenas de texto no estén vacías y que los datos numéricos sean enteros positivos válidos, impidiendo que el usuario ingrese letras o símbolos.

### 2. Actualizar población y superficie de un país

Qué hace: Modifica los datos dinámicos de un país ya existente.

Cómo funciona: Solicita el nombre del país a modificar y lo busca en la lista de datos. Si no lo encuentra, gestiona la validación mediante un condicional.

Nota: Si el usuario ingresa mal el nombre, el sistema detecta que el resultado es inexistente (`None`) y, mediante un bucle `while True`, le permite reintentar el ingreso de forma infinita en lugar de expulsarlo al menú principal. Una vez encontrado el país, se actualizan su población y su superficie.

## 3. Buscar un país por nombre
Qué hace: Localiza la información completa de uno o varios países.

Cómo funciona: Despliega un submenú que le permite al usuario elegir entre dos tipos de búsqueda:

Coincidencia parcial: Si no se recuerda el nombre completo (por ejemplo, buscar "Ar" mostrará "Argentina").

Coincidencia exacta: Requiere ingresar el nombre idéntico para aislar el objeto específico.

## 4. Filtrar países (Continente / Población / Superficie)
Qué hace: Segmenta la base de datos para mostrar solo los países que cumplan con ciertos criterios.

Cómo funciona: Abre un submenú de filtros:

Por Continente: Muestra la lista de continentes disponibles y filtra ignorando mayúsculas/minúsculas.

Por Rango (Población o Superficie): Solicita un límite mínimo y un límite máximo. Incluye una validación interna en bucle que impide avanzar si el usuario ingresa un valor mínimo que sea mayor al máximo.

## 5. Ordenar países
Qué hace: Ordena la lista según el criterio elegido sin modificar los datos originales.
Cómo funciona: Despliega un submenú con tres criterios: nombre, población o superficie. En cada caso solicita la dirección: ascendente o descendente.

## 6. Mostrar estadísticas generales
Qué hace: Calcula y muestra indicadores clave del dataset.
Cómo funciona: Muestra el país con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente.

## 7. Guardar y Salir
Qué hace: Guarda todos los cambios y cierra el programa.
Cómo funciona: Reescribe el archivo paises.csv completo con los datos actuales en memoria y termina la ejecución.

## Formato del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Alemania,83149300,357022,Europa
```

## Links

-  **Video demostrativo:** https://www.youtube.com/watch?v=bJnISkzUnRw
-  **Informe PDF:** https://drive.google.com/drive/folders/19dgGtu8lo2ALfiJY3YJ_uBnr0cVkxtLp

---
*UTN TUP a Distancia — Programación 1 — 2026*
