# Simulador de AFD en Python (AFD.py)

Este proyecto implementa un **Autómata Finito Determinista (AFD)** en Python.  
El programa lee un archivo `.txt` que contiene cadenas formadas únicamente por `0` y `1`, y para cada cadena imprime en consola si el autómata la **ACEPTA** o **NO ACEPTA**.

---

## Requerimientos

- Tener instalado **Python 3.x**
- Tener un archivo de entrada `.txt` con mínimo **10 líneas**
- Cada línea debe contener una cadena con solo `0` y `1`

---

## Archivos del proyecto

- `AFD.py` → Programa principal que simula el autómata
- `entrada.txt` → Archivo con cadenas a evaluar (ejemplo)

---

## Cómo ejecutar el programa

Desde la terminal, en la carpeta donde está el archivo `AFD.py`, ejecutar:

```bash
python AFD.py entrada.txt
```

 Donde:
- `AFD.py` es el programa
- `entrada.txt` es el archivo con las cadenas

---

## Formato del archivo de entrada

El archivo debe tener una cadena por línea, por ejemplo:

```
0
1
01
10
000
111
00101
10101
010101
11000
```

---

## Salida del programa

El programa imprime únicamente:

- `ACEPTA` → si la cadena es válida para el AFD
- `NO ACEPTA` → si la cadena no es válida para el AFD

Ejemplo de salida:

```
ACEPTA
NO ACEPTA
ACEPTA
NO ACEPTA
ACEPTA
NO ACEPTA
ACEPTA
NO ACEPTA
ACEPTA
NO ACEPTA
```

---

## Explicación del AFD

Este AFD tiene:

- **q1** → estado inicial  
- **q2** → estado de aceptación  
- **q3** → estado de rechazo  

### Transiciones del autómata

- Desde **q1**:
  - con `0` → va a **q2**
  - con `1` → va a **q3**

- Desde **q2**:
  - con `0` o `1` → se queda en **q2**

- Desde **q3**:
  - con `0` o `1` → se queda en **q3**

---

## ¿Qué lenguaje acepta?

El autómata acepta todas las cadenas binarias que **empiecen con `0`**.

Ejemplos:

### Acepta:
- `0`
- `01`
- `000`
- `010101`

### No acepta:
- `1`
- `10`
- `111`
- `10101`

---

## Funcionamiento del programa

1. El programa recibe el nombre del archivo `.txt` como parámetro.
2. Lee todas las líneas del archivo.
3. Por cada línea:
   - elimina espacios y saltos de línea
   - verifica que solo contenga `0` y `1`
   - simula el recorrido del AFD según las transiciones
4. Si el estado final es **q2**, imprime `ACEPTA`
5. Si el estado final es otro, imprime `NO ACEPTA`

---
