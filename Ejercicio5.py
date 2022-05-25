inversion = float(input("Digite la cantidad a invertir: "))
taza = float(input("Digite el interes: "))
anios = int(input("Digite la cantidad de años: "))
result = ""

while(inversion >= 1):
    result = (inversion * taza)/anios
    print(f"Ganancias por año -> {result}")
    break