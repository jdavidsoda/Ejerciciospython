number=int(input("Escriba un numero"))
total=0

for number in range(0,number+1):
  cuadrado=number**2
  total=total+cuadrado
  print(total)