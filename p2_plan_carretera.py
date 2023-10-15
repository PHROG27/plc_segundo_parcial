def costo():
  x=(millas/millas_por_galon)*precio
  return x

print("Ingresa la distancia que recorreras en millas")
millas=float(input())
print("Ingresa el rendimiento en millas por galon")
millas_por_galon=float(input())
print("precio actual de la gasolina")
precio=float(input())
input("¿Cuantos días vas a viajar?")

print("El precio por viajar esa distancia es de $", costo())
