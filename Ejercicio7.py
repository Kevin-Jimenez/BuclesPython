#Tabla de multiplicar

num = int(input("Digite el numero de la tabla que desa saber: "))
print(f"Tabla del {num}")
for i in range(10):
    i+=1
    print(f"{num} * {i} = {i*num}")