print("Este es un programa para cuidar a Rubí")
print("¿Que día de la semana es hoy?")
dia = str(input())
if dia == "Martes":
  print("Regar a Rubí")
elif dia == "Jueves":
  print("Regar a Rubí")
elif dia == "Sabado":
  print("Regar a Rubí")
elif dia == "Lunes":
  print("No es necesario regar a Rubí")
elif dia == "Miercoles":
  print("No es necesario regar  Rubí")
elif dia == "Viernes":
  print("No es necesario regar a Rubí")
elif dia == "Domingo":
  print("No es necesario regar a Rubí")

print("¿A que temperatura se encuentra el entorno? En grados Celsius")
temperatura = float(input())
if temperatura < 20:
  print("Llevarla adetro de casa")
elif temperatura > 23:
  print("Llevarla dentro de casa y encender ventilador")
elif 20 <= temperatura <= 22:
  print("Buenas condiciones")
