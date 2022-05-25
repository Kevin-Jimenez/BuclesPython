#Triangulo
altura_triangulo = int(input("Digite la Altura del triangulo: "))

for i in range(altura_triangulo):
    for j in range(i+1):
        print("*" ,end="")
    print()