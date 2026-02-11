import sys  # permite leer argumentos desde la consola (como el nombre del archivo)

def simular_afd(cadena):
    estado = "q1"  # estado inicial

    # Recorremos los simbolos de la cadena
    for simbolo in cadena:

        # estado inicial q1
        if estado == "q1":
            if simbolo == "0":
                estado = "q2"  # con 0 vamos a q2
            elif simbolo == "1":
                estado = "q3"  # con 1 vamos a q3

        # aceptado
        elif estado == "q2":
            if simbolo == "0" or simbolo == "1":
                estado = "q2"  # con 0 o 1 se queda en q2

        # no aceptado
        elif estado == "q3":
            if simbolo == "0" or simbolo == "1":
                estado = "q3"  # con 0 o 1 se queda en q3

    # se verifica si terminó en el estado de aceptacion
    if estado == "q2":
        return True
    else:
        return False


def main():

    # verifica que se haya escrito correctamente python AFD.py entrada.txt
    if len(sys.argv) != 2:
        sys.exit(1)

    archivo = sys.argv[1]  # guarda el nombre del archivo recibido como parámetro

    try:
        # abre el archivo y lee todas las líneas
        with open(archivo, "r") as f:
            lineas = f.readlines()

        # recorre cada línea del archivo
        for linea in lineas:
            cadena = linea.strip()  # elimina espacios y saltos de línea

            # verifica que la cadena solo tenga 0 y 1
            if cadena == "" or any(c not in "01" for c in cadena):
                print("NO ACEPTA")
                continue

            # simula el AFD y muestra resultado
            if simular_afd(cadena):
                print("ACEPTA")
            else:
                print("NO ACEPTA")

    # si el archivo no existe se cierra el programa
    except FileNotFoundError:
        sys.exit(1)


if __name__ == "__main__":
    main()
