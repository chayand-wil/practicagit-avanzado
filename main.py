# main.py

def menu_principal():
    print("=== SISTEMA DE CONVERSIONES ===")
    print("1. Conversiones de Volumen")
    print("2. Conversiones de Velocidad")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    return opcion

def modulo_volumen():
    # Aquí un compañero puede desarrollar su código en otra rama
    print("\n[Módulo de Volumen en construcción...]\n")

def modulo_velocidad():
    # Aquí otro compañero puede desarrollar su código en otra rama
    print("\n[Módulo de Velocidad en construcción...]\n")

def main():
    while True:
        opcion = menu_principal()
        
        if opcion == '1':
            modulo_volumen()
        elif opcion == '2':
            modulo_velocidad()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
