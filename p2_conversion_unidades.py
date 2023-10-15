cant=float(input("Ingresa la cantidad a convertir:"))
unidad1=input("Ingresa la unidad de origen (milas,kilómetros,litros, galones,:")
unidad2=input("Ingresa la unidad de origen(kilómetros, millas,litros, galones,o nada):")
grados=input("Ingresa los grados que necesitas de origen (celcius,fahrenheit,kelvin):")
grados2=input("Ingresa los grados que necesitas de destino (celcius,fahrenheit,kelvin):")
if unidad1=='kilómetros' and unidad2=='millas':
  conversion=cant*1.60934 
  print("la conversión a kilómetros es",conversion)
elif unidad1=='millas' and unidad2=='kilómetros':
  conversion=cant/1.60934 
  print("la conversión a kilómetros es",conversion)
elif unidad1=='litros' and unidad2=='galones':
  conversion=cant/3.78541
  print("la conversión a galones es",conversion)
elif unidad1=='galones' and unidad2=='litros':
  conversion=cant*3.78541
elif grados=="celsius" and grados2 =="fahrenheit":
  resultado=(int(cant)*9/5+32)
  print("la temperatura de celsius a fahrenheit es",resultado)
elif grados=="celsius" and grados2 =="kelvin":
  resultado= cant+ 273.15
  print("la temperatura de celsius a kelvin es",resultado)
elif grados=="fahrenheit" and grados2=="celsius":
  resultado=(cant-32)*5/9 
  print("la temperatura defahrenheit a celsius es",resultado)
elif unidad1=='fahrenheit' and unidad2=='kelvin':
  resultado=(cant-32)*5/9+273.15
  print("la temperatura de fahrenheit a kelvin es",resultado)
elif unidad1=='kelvin' and unidad2=='celsius':
  resultado=cant-273.15
  print("la temperatura de kelvin a celsius es",resultado)
elif unidad1=='kelvin' and unidad2=='fahrenheit':
  resultado=(cant-273.15)*9/5 + 32
  print("la temperatura de kelvin a fahrenheit es",resultado)
else:
  print("No es posible realizar esta accion")
