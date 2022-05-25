number = int(input("Digite numero: "))

for i in range(number):
    i#+=1
    for j in range(i+1):
        if(i % 2 != 0):
            print(j,end="")
        print()
    #print()