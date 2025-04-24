#a=5
#while a>0:
#   print(a)
#    a-=1 # hace un contador inverso 

# lista del -10 al +10 y que identifique que numero es par o impar

numero = -10
while numero <= 10:
  if numero % 2 == 0: #negativo hasta llegar a 0
    print(numero,"es par")   
  else:
    print(numero,"es impar")  
  numero += 1 # llega a 0 y suma 1 y entra de nuevo en el bucle


