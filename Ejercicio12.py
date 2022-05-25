frase = input("Digite frase: ")
letra = input("Digite una letra: ")

def letraRepetida(frase,letra):
    count = 0
    for i in frase:
        #print(i)
        if i == letra:
            count += 1
    print(f"{i} Se repite {count} veces")
    return ""
print(letraRepetida(frase,letra))