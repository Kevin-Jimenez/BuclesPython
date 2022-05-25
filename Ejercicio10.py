numero = int(input("Digite numero: "))

def numeroPrimo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print(f"No es primo {n} es divisor")
            #return False
    print("Es primo")
    #return True

print(numeroPrimo(numero))