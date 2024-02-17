# Forma 1 de apertura a partir del método with 
#consideraciones generales para manejo de archivos : donde se ejecuta el programa , a donde apunta lo que vas llamar o abrir 
ruta_archivo = './txt/bit.txt' #donde se almacena # ruta relativa 
# en windows al usar la ruta absoltua agregar un /  => C://Users//Carpeta01//Carpeta02//archivo.txt 
with open(ruta_archivo,mode='r') as file:
    # capturo la información del archivo
    data = file.read()
    pass # Archivo se cierra de forma automática

# muestro la data
print(data)
#print("hello",'\n',"word")