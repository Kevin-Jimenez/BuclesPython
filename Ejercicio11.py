#mostrar frase alreves
phrase = str(input("Digite frase: "))

def reversarFrase(phrase):
    reverse= []
    i= len(phrase)
    while  i>0:
        reverse += phrase[i-1]
        i = i -1
    return ''.join(reverse)
print(reversarFrase(phrase))