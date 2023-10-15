def juego_rol():
  import random
  print("Bienvenido a este mundo de fantasia")
  print("Deberas salvar este mundo antes de que sea normal como el que tu conoces")
  print("Selecciona tu personaje, cada uno tiene caracteristicas algo idferentes")
  print("1.El curador")
  print("2.El mago")
  print("3.El espadachin")
  print("4.El arquero")
  print("5.El ladron")
personaje  = input()
if personaje == "1":
  print("Eres un curador, ayudarás a tu equipo a estar siempre sano")
  personaje_seleccionado = "Curador"
elif personaje == "2":
  print("Eres el mago, con diversos hechizos curaras a tus aliasdos o destruiras a tus enemigos")
  personaje_seleccionado = "Mago"
elif personaje == "3":
  print("Eres el espadachin, con tu espada derribaras a tus enemigos")
  personaje_seleccionado = "Espadachin"
elif personaje == "4":
  print("Eres el arquero, desde la distancia derroataras a los que se te enfrente")
  personaje_seleccionado = "Arquero"
elif personaje == "5":
  print("El ladron robara cosas a sus enemigos y las usara a su favor")
  personaje_seleccionado = "Ladron"
  
print("Estas llegando al castillo de este mundo, el cual esta plagado de monstruos")
print("Un grupo de monstruos ha decidido hacer una emboscada. Rapido" ,personaje_seleccionado,"Que harás?")
print("1. Luchar, 2. Huir, 3. Tratar de esconderte")
eleccion=input()
if eleccion == "1":
  resultado = ['Derrotaste a los monustros , Los mosntruso derrotaron a tu equipo']
  print(random.choice(resultado))
if eleccion == "2":
  print("Los monstruos eran más rapidos y te alcanzaron, mejor suerte la proxima")
if eleccion == "3":
  resultado = ['Lograste esconderte y que te perdieran de vista , Los monstruos te encontraron y te comieron']
  print(random.choice(resultado))
print("Has entrado al castillo, donde esta el rey de los monstruos, para dar fin a esta historia deberas derrotarlo, como lo haras?")
print("1. Llegandole por la espalda, 2. Le cortas la cabeza 3. Le quitas su corona que es la fuente de su poder")
if eleccion_2 == "1":
  resultado = ['El rey se dio cuenta que estabas detras de el y te aplasta , Logras apuñalarlo por la espalda']
  print(random.choice(resultado))
if eleccion_2 == "2":
  resultado = ['El rey deja descubierto su cuello por lo que le cortas la cabeza , El rey te agarra con su mano y te come , El rey logra derrotar a tu equipo y se lo come dejandote solo']
  print(random.choice(resultado))
if eleccion_2 == "3":
  resultado = [ 'Logras quitare su corona al rey pero ahora tu eres malvado , Logras quitarle la corona y acabar con el , Fallas en el intento y mueres']
  print(random.choice(resultado))
