# FOR --->  
for i in range (5+1):
    print (i)
# programa donde se ingrese por teclado un valor entero y que me liste de 0 al valor ingresado

#n=int(input("Ingrese el valor: "))
#for i in range(n+1):
    #print(i)

# estructura del for ---> ( inicio, final -1 , icremento)

#for i in range(1,10,2):
    #print(i)


print("--------------------------------------------------")
print("RECORRE POR POSICIONES E IMPRIME TODOS LOS ELEMENTOS DE LA LISTA")
for i in [1,2,3]:
    print (i)
    
print("--------------------------------------------------")
print("MATRIZ")
for i in range(0,6):
    print("TABLA DEL ",i)
    for j in range(0,11):
        print(i, "x",j,"=",i*j)
