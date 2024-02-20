from string import ascii_lowercase

def adivinar_contraseña(contraseña):
    intentos = 0
    contraseña_adivinada = ''
    # Bucle para cada letra de la contraseña (Usamos un bucle anidado donde el bucle exterior itera sobre cada letra de la contraseña y el bucle interior intenta cada letra del alfabeto hasta encontrar una coincidencia.)
    for letra_real in contraseña:
        # Prueba cada letra del alfabeto
        for letra_prueba in ascii_lowercase:
            intentos += 1
            if letra_prueba == letra_real:
                contraseña_adivinada += letra_prueba
                break
    return intentos

def main():
    # Solicitar contraseña
    contraseña = input("Ingrese la contraseña (se mostrará oculta): ")
    intentos = adivinar_contraseña(contraseña)
    print(f"La contraseña fue forzada en {intentos} intentos.")

if __name__ == "__main__":
    main()
