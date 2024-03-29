def contar_lineas_codigo(archivo_path):
    try:
        if archivo_path.endswith('.py'):
            with open(archivo_path, 'r') as archivo:
                lineas = archivo.readlines()
                lineas_codigo = [linea.strip() for linea in lineas if linea.strip() and not linea.strip().startswith('#')]
                return len(lineas_codigo)
        else:
            print("El archivo no tiene la extensión .py.")
            return 
    except FileNotFoundError:
        print(f'Archivo no encontrado: {archivo_path}')
        return

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    cantidad_lineas = contar_lineas_codigo('txt/exe6.py')
    
    if cantidad_lineas is not None:
        print(f'El archivo tiene {cantidad_lineas} líneas de código (excluyendo comentarios y líneas en blanco).')

if __name__ == "__main__":
    main()