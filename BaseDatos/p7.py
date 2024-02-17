import requests
import sqlite3

def obtener_datos_sunat():
    # Reemplaza la siguiente URL con la API real de SUNAT para obtener datos del dólar.
    url_sunat = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

    try:
        response = requests.get('https://api.apis.net.pe/v1/tipo-cambio-sunat')
        datos = response.json()
        return datos
    except Exception as e:
        print(f"Error al obtener datos de SUNAT: {e}")
        return None

def crear_tabla_db():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT,
            precio_compra REAL,
            precio_venta REAL
        )
    ''')

    conn.commit()
    conn.close()

def insertar_datos_db(datos):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Insertar los datos en la tabla
    for registro in datos:
        cursor.execute('''
            INSERT INTO sunat_info (fecha, precio_compra, precio_venta)
            VALUES (?, ?, ?)
        ''', (registro['fecha'], registro['precio_compra'], registro['precio_venta']))

    conn.commit()
    conn.close()

def mostrar_contenido_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Obtener y mostrar el contenido de la tabla
    cursor.execute('SELECT * FROM sunat_info')
    filas = cursor.fetchall()

    for fila in filas:
        print(f"Fecha: {fila[0]}, Precio Compra: {fila[1]}, Precio Venta: {fila[2]}")

    conn.close()

def main():
    datos_sunat = obtener_datos_sunat()

    if datos_sunat:
        crear_tabla_db()
        insertar_datos_db(datos_sunat)
        print("Datos almacenados en la tabla 'sunat_info'.\n")

        print("Contenido de la tabla:")
        mostrar_contenido_tabla()

if __name__ == "__main__":
    main()