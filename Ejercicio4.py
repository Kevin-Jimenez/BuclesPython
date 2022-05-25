numero = int(input("Digite numero positivo: "))

if(numero <= 0):
    print("[-] Errpor el numero debe ser mayor a 0")
else:
    for i in range(numero,-1,-1):
        print(i, end=", ")