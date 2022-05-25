#pedir contraseña

contrsena = input("Digite su contraseña: ")
probar = contrsena
new = input("Confirme su contraseña: ")
while (new != probar):
    new = input("Contraseña incorrecta, Confirme su contraseña: ")
print("Correcto!")