def inicio():
    respuesta = input("¿Responde a estímulos? (s/n): ").lower()
    if respuesta == 's':
        valorar_hospital()
    else:
        abrir_via_aerea()

def valorar_hospital():
    print("Valorar la necesidad de llevarlo al hospital más cercano.")
    fin()

def abrir_via_aerea():
    respuesta = input("¿Respira? (s/n): ").lower()
    if respuesta == 's':
        print("Permitirle posición de suficiente ventilación.")
        fin()
    else:
        administrar_ventilaciones()

def administrar_ventilaciones():
    print("Administrar 5 Ventilaciones y llamar a Ambulancia.")
    buscar_signos_vida()

def buscar_signos_vida():
    respuesta = input("¿Signos de Vida? (s/n): ").lower()
    if respuesta == 's':
        reevaluar_espera_ambulancia()
    else:
        administrar_compresiones()

def reevaluar_espera_ambulancia():
    respuesta = input("¿Llegó la Ambulancia? (s/n): ").lower()
    if respuesta == 's':
        fin()
    else:
        buscar_signos_vida()

def administrar_compresiones():
    print("Administrar Compresiones Torácicas hasta que llegue ambulancia.")
    reevaluar_espera_ambulancia()

def fin():
    print("El proceso de primeros auxilios ha terminado.")

if __name__ == "__main__":

    inicio()
