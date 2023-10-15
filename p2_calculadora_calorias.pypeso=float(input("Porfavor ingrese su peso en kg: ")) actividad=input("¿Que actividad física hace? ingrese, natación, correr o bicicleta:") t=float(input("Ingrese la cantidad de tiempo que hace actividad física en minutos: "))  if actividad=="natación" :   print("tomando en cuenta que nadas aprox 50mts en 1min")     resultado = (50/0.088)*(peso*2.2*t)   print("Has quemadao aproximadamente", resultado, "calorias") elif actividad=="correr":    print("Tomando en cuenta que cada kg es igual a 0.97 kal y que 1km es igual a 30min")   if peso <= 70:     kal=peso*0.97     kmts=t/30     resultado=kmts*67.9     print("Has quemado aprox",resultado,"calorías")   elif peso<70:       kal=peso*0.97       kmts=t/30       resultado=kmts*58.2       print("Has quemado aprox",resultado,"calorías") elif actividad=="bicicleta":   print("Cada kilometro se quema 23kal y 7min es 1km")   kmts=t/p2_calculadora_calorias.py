peso=float(input("Porfavor ingrese su peso en kg: "))
actividad=input("¿Que actividad física hace? ingrese, natación, correr o bicicleta:")
t=float(input("Ingrese la cantidad de tiempo que hace actividad física en minutos: "))

if actividad=="natación" :
  print("tomando en cuenta que nadas aprox 50mts en 1min")
 
  resultado = (50/0.088)*(peso*2.2*t)
  print("Has quemadao aproximadamente", resultado, "calorias")
elif actividad=="correr":

  print("Tomando en cuenta que cada kg es igual a 0.97 kal y que 1km es igual a 30min")
  if peso <= 70:
    kal=peso*0.97
    kmts=t/30
    resultado=kmts*67.9
    print("Has quemado aprox",resultado,"calorías")
  elif peso<70:
      kal=peso*0.97
      kmts=t/30
      resultado=kmts*58.2
      print("Has quemado aprox",resultado,"calorías")
elif actividad=="bicicleta":
  print("Cada kilometro se quema 23kal y 7min es 1km")
  kmts=t/7
  resultado=kmts*23
  print("Has quemado aprox",resultado,"calorías")
