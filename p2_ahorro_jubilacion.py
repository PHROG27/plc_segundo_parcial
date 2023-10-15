edad= int(input("Cual es tu edad actual?"))
edad_a_retirarse=int(input("A que edad desea retirarse"))
dinero=int(input("Cuanto dinero desea obtener al retirarse?"))
r = 0.25/12
n = (edad_a_retirarse - edad) * 12
t = edad_a_retirarse - edad
PMT= dinero*r/((1+r)**n-1)*(1+r)**-t
print("El dinero mensual requerido para retirarse es de", PMT)
