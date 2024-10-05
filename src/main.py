import os

def read_file(file_path):
    print("Hola esta actualizacion hay que subirla a git")
    # with open(file_path, "r", encoding="utf-8") as file:
    #     for line in file:
    #         print(line.strip())

def main():
    # Obtener la ruta absoluta del archivo de texto basado en la ubicación del script
    script_dir = os.path.dirname(__file__)  # Directorio del script
    file_path = os.path.join(script_dir, 'texto.txt')  # Ruta relativa a 'texto.txt'
   
    read_file(file_path)


if __name__ == '__main__':
    main()