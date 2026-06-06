# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**  
Tecnicatura Universitaria en Programación (TUP) — UTN a Distancia


## Descripción

Aplicación de consola en Python que permite gestionar un dataset de países cargado desde un archivo CSV. Implementa búsquedas, filtros, ordenamientos y estadísticas utilizando listas, diccionarios y funciones modulares.

## Integrantes

| Nombre | Legajo |
|--------|--------|
| Lecuona Gonzalez Eva | 612.507|
| [Nombre Integrante 2] | [Legajo 2] |

## Estructura del proyecto

```
tpi_prog1/
├── main.py          # Código fuente principal
├── paises.csv       # Dataset base (50 países)
└── README.md        # Este archivo
```

## Cómo ejecutar

**Requisitos:** Python

```bash
# Clonar el repositorio
git clone https://github.com/EvaLecuona/TPI_ProgramacionI_GestionPaises
cd [repositorio]

# Ejecutar el programa
python3 main.py
```

## Menú de opciones

```
   GESTIÓN DE DATOS DE PAÍSES - TPI UTN TUP
  1. Agregar un país
  2. Actualizar datos de un país
  3. Buscar país por nombre
  4. Filtrar países
  5. Ordenar países
  6. Mostrar todos los países
  7. Ver estadísticas
  0. Salir
```

## Instrucciones de Ejecución

Para correr el programa, asegurarse de tener instalado Python 3 y seguir estos pasos desde la terminal:

1. **Descargar los archivos:** Asegurarse de tener en la misma carpeta el archivo principal (`main.py`), el módulo de funciones y el archivo de datos `paises.csv`.
2. **Abrir la terminal:** Navegar hasta la carpeta del proyecto.
3. **Ejecutar el programa:** Correr el siguiente comando:
```bash
   python main.py

```

## Guía de Opciones del Menú
El sistema cuenta con un menú interactivo validado para evitar ingresos erróneos. Se detalla qué incluye y cómo funciona cada una de las opciones principales:

## 1. Agregar un nuevo país
Qué hace: Permite dar de alta un país que no esté registrado en el sistema.

Cómo funciona: Solicita de forma secuencial el nombre, la población, la superficie y el continente. Utiliza funciones de validación para garantizar que las cadenas de texto no estén vacías y que los datos numéricos sean enteros positivos válidos, impidiendo que el usuario ingrese letras o símbolos.

## 2. Actualizar población y superficie de un país
Qué hace: Modifica los datos dinámicos de un país ya existente.

Cómo funciona: Solicita el nombre del país a modificar y lo busca en la base de datos mediante un sistema de excepciones (try-except).

Nota: Si el usuario ingresa mal el nombre, el sistema atrapa el error (ValueError) y le permite reintentar el ingreso de forma infinita dentro de un bucle, en lugar de expulsarlo al menú principal. Una vez encontrado, se actualizan de forma segura su población y su superficie.

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

## Formato del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Alemania,83149300,357022,Europa
```

## Links

-  **Video demostrativo:**
-  **Informe PDF:**

---
*UTN TUP a Distancia — Programación 1 — 2026*
