def ingresar_notas():
 
  notas = input("Ingrese las notas de los estudiantes separadas por comas: ")

 
  notas = [int(nota) for nota in notas.split(",")]

  return notas

def calcular_promedio(notas):
  promedio = sum(notas) / len(notas)
  return promedio

def nota_mas_alta(notas):
  max_nota = max(notas)
  return max_nota

def nota_mas_baja(notas):
  min_nota = min(notas)
  return min_nota

def contar_aprobados_reprobados(notas):
  aprobados = len([nota for nota in notas if nota >= 60])
  reprobados = len([nota for nota in notas if nota < 60])
  return aprobados, reprobados

if __name__ == "__main__":
  notas = ingresar_notas()
  promedio = calcular_promedio(notas)
  max_nota = nota_mas_alta(notas)
  min_nota = nota_mas_baja(notas)
  aprobados, reprobados = contar_aprobados_reprobados(notas)

  print(f"Promedio de notas: {promedio}")
  print(f"Nota más alta: {max_nota}")
  print(f"Nota más baja: {min_nota}")
  print(f"Estudiantes aprobados: {aprobados}")
  print(f"Estudiantes reprobados: {reprobados}")
