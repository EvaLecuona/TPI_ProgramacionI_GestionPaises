# 🌍 Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**  
Tecnicatura Universitaria en Programación (TUP) — UTN a Distancia

---

## 📋 Descripción

Aplicación de consola en Python 3 que permite gestionar un dataset de países cargado desde un archivo CSV. Implementa búsquedas, filtros, ordenamientos y estadísticas utilizando listas, diccionarios y funciones modulares.

## 👥 Integrantes

| Nombre | Legajo |
|--------|--------|
| [Nombre Integrante 1] | [Legajo 1] |
| [Nombre Integrante 2] | [Legajo 2] |

## 🗂 Estructura del proyecto

```
tpi_prog1/
├── main.py          # Código fuente principal
├── paises.csv       # Dataset base (50 países)
└── README.md        # Este archivo
```

## ▶️ Cómo ejecutar

**Requisitos:** Python 3.x (sin dependencias externas)

```bash
# Clonar el repositorio
git clone https://github.com/[usuario]/[repositorio].git
cd [repositorio]

# Ejecutar el programa
python3 main.py
```

## 🧭 Menú de opciones

```
══════════════════════════════════════════════════
   GESTIÓN DE DATOS DE PAÍSES - TPI UTN TUP
══════════════════════════════════════════════════
  1. Agregar un país
  2. Actualizar datos de un país
  3. Buscar país por nombre
  4. Filtrar países
  5. Ordenar países
  6. Mostrar todos los países
  7. Ver estadísticas
  0. Salir
```

## 📊 Ejemplos de uso

### Agregar un país
```
Seleccione una opción: 1
── AGREGAR PAÍS ──
Nombre del país: Corea del Sur
Población: 51700000
Superficie (km²): 100210
Continente: Asia
[OK] País 'Corea Del Sur' agregado correctamente.
```

### Filtrar por continente
```
Seleccione una opción: 4
── FILTRAR PAÍSES ──
1. Por continente
2. Por rango de población
3. Por rango de superficie
Seleccione una opción: 1
Continentes disponibles: África, América, Asia, Europa, Oceanía
Ingrese el continente: Europa
```

### Ver estadísticas
```
Seleccione una opción: 7
  Total de países registrados: 50
  POBLACIÓN
  País con mayor población : China (1.412.600.000 hab.)
  País con menor población : Samoa (198.414 hab.)
  Promedio de población    : 142.567.832 hab.
```

### Manejo de errores
```
Ingrese el continente: 123
Ingrese el continente:     (vacío)
[ERROR] Este campo no puede estar vacío. Intente nuevamente.

Población: abc
[ERROR] Ingrese un número entero positivo válido (sin letras ni símbolos).
```

## 📁 Formato del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Alemania,83149300,357022,Europa
```

## 🔗 Links

- 📹 **Video demostrativo:** [URL del video — completar antes de entregar]
- 📄 **Informe PDF:** [URL del PDF — completar antes de entregar]

---
*UTN TUP a Distancia — Programación 1 — 2025*
