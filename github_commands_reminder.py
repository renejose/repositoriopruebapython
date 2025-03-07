# Diccionario con todos los comandos de GitHub organizados por categoría
commands = {
    "Configuración inicial": [
        {
            "comando": "git config --global user.name \"Tu Nombre\"",
            "descripción": "Configura tu nombre de usuario para todos tus repositorios"
        },
        {
            "comando": "git config --global user.email \"tu@email.com\"",
            "descripción": "Configura tu correo electrónico para todos tus repositorios"
        },
        {
            "comando": "git config --list",
            "descripción": "Muestra todas tus configuraciones actuales"
        }
    ],
    "Crear y clonar repositorios": [
        {
            "comando": "git init",
            "descripción": "Inicializa un nuevo repositorio Git en la carpeta actual"
        },
        {
            "comando": "git clone https://github.com/usuario/repositorio.git",
            "descripción": "Clona un repositorio existente desde GitHub"
        }
    ],
    "Cambios básicos": [
        {
            "comando": "git status",
            "descripción": "Muestra el estado actual del repositorio"
        },
        {
            "comando": "git add archivo.txt",
            "descripción": "Añade un archivo específico al área de preparación"
        },
        {
            "comando": "git add .",
            "descripción": "Añade todos los archivos modificados al área de preparación"
        },
        {
            "comando": "git commit -m \"Mensaje del commit\"",
            "descripción": "Guarda los cambios con un mensaje descriptivo"
        }
    ],
    "Trabajar con ramas": [
        {
            "comando": "git branch",
            "descripción": "Lista todas las ramas locales"
        },
        {
            "comando": "git branch nueva-rama",
            "descripción": "Crea una nueva rama llamada 'nueva-rama'"
        },
        {
            "comando": "git checkout otra-rama",
            "descripción": "Cambia a la rama 'otra-rama'"
        },
        {
            "comando": "git checkout -b nueva-rama",
            "descripción": "Crea una nueva rama y cambia a ella en un solo paso"
        },
        {
            "comando": "git merge otra-rama",
            "descripción": "Fusiona 'otra-rama' en tu rama actual"
        }
    ],
    "Sincronizar con GitHub": [
        {
            "comando": "git remote add origin https://github.com/usuario/repositorio.git",
            "descripción": "Conecta tu repositorio local con uno remoto en GitHub"
        },
        {
            "comando": "git push -u origin main",
            "descripción": "Sube tus cambios a GitHub y establece la rama principal"
        },
        {
            "comando": "git push",
            "descripción": "Sube los cambios a la rama remota ya configurada"
        },
        {
            "comando": "git pull",
            "descripción": "Obtiene y fusiona los cambios del repositorio remoto"
        },
        {
            "comando": "git fetch",
            "descripción": "Obtiene los cambios del repositorio remoto sin fusionarlos"
        }
    ],
    "Revisar historial": [
        {
            "comando": "git log",
            "descripción": "Muestra el historial de commits"
        },
        {
            "comando": "git log --oneline",
            "descripción": "Muestra el historial de commits en formato resumido"
        },
        {
            "comando": "git blame archivo.txt",
            "descripción": "Muestra quién modificó cada línea de un archivo"
        }
    ],
    "Deshacer cambios": [
        {
            "comando": "git restore archivo.txt",
            "descripción": "Descarta cambios en un archivo específico"
        },
        {
            "comando": "git reset HEAD archivo.txt",
            "descripción": "Quita un archivo del área de preparación"
        },
        {
            "comando": "git reset --hard HEAD~1",
            "descripción": "Elimina el último commit (¡cuidado!)"
        },
        {
            "comando": "git revert HEAD",
            "descripción": "Crea un nuevo commit que revierte el último commit"
        }
    ]
}

def main():
    """Función principal del programa"""
    while True:
        # Mostrar menú principal
        print("\n\n" + "=" * 40)
        print("===== RECORDATORIO DE COMANDOS GITHUB =====\n")
        print("Categorías disponibles:")
        
        # Listar categorías
        categorias = list(commands.keys())
        for i, categoria in enumerate(categorias, 1):
            print(f"{i}. {categoria}")
        
        print("\n0. Salir")
        
        # Obtener selección del usuario
        try:
            opcion = int(input("\nSelecciona una categoría (0-7): "))
            
            # Salir del programa
            if opcion == 0:
                print("¡Hasta pronto!")
                break
                
            # Mostrar comandos de la categoría seleccionada
            elif 1 <= opcion <= len(categorias):
                categoria = categorias[opcion-1]
                
                print("\n\n" + "=" * 40)
                print(f"===== {categoria.upper()} =====\n")
                
                for cmd in commands[categoria]:
                    print(f"{cmd['comando']}")
                    print(f"  {cmd['descripción']}")
                    print()
                
                input("\nPresiona Enter para volver al menú principal...")
                
            else:
                input("Opción no válida. Presiona Enter para continuar...")
                
        except ValueError:
            input("Por favor, ingresa un número. Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
