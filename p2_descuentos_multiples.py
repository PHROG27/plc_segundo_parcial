print ("Dame el precio de tu producto")
x = float(input())
print("Dame su categoria A, B o C")
y = input()
if y == "A":
  precio_A = int(x)-int(x)*.10
  print("Tu precio es de", precio_A)
elif y == "B":
  precio_B = int(x)-int(x)*.5
  print("Tu precio es de", precio_B)
elif y == "C":
  precio_C = int(x)-int(x)/.2
  print("Tu precio es de", precio_C)
