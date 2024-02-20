import sys

def filtrar_ventas(ventas, umbral):
  
    return {mes: balance for mes, balance in ventas.items() if balance > umbral}

def main():
    # Diccionario con los balances
    ventas = {
        "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000, 
        "Mayo": 81000, "Junio": 13000, "Julio": 21000, "Agosto": 41200, 
        "Septiembre": 25000, "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000
    }

    # Leer el umbral desde los argumentos de línea de comandos
    umbral = int(sys.argv[1])

    # Obtener y mostrar los resultados
    ventas_filtradas = filtrar_ventas(ventas, umbral)
    print(ventas_filtradas)

if __name__ == "__main__":
    main()
