https://replit.com/@Marco-Antoni518/Reto-Parcial-2?v=1

print("Favor de ingresar la calificacion del examen")
examen = float(input())
print("El estudiante participa en clase? Si o No?")
participacion = str(input())
print("Dame el número de asignaciones hechas 0-10")
asignaciones = int(input())


if examen > 70 and asignaciones > 5:
  print("Aprobado")
elif examen < 70 and participacion == "Si":
  print("Aprueba")
else:
  print("Reprobado")
