n = int(input("Ingrese un n: "))
n

lista_valores = []
for i in range(1, 13):
    x = f'{n} x {i} = {n*i}\n'
    lista_valores.append(x)
lista_valores

try:
    file1 = open("txt/bit.txt")
 
except Exception as e:
    print("file not found",e)

with open(f'tabla-{n}.txt', mode='w') as file:
    file.writelines(lista_valores)

