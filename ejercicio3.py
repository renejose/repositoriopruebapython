Peru# Inicializamos una lista vacía para almacenar los países
paises = []

while True:
    pais = input("Ingresa el nombre de un país (escriba 'salir' para terminar): ").strip()
    
    if pais.lower() == "salir":
        break  # Sale del bucle si el usuario escribe "salir"

    paises.append(pais)  # Agrega el país a la lista

print("\nLista de países ingresados:")
print(paises)
