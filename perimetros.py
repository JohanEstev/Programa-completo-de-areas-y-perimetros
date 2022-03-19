def perimetrocuadrado():
    lado =float(input("ingrese el valor del lado: " ))
    return print("perimetro del cuadrado es", lado*4)


def perimetrorectangulo():
    base =float(input("ingrese el valor de la base: " ))
    altura =float(input("ingrese el valor de la altura: " ))
    return print("perimetro del rectangulo es", 2*base+2*altura)



def perimetrocirculo():
    radio =float(input("ingrese el valor del radio: " ))
    pi=3.1416
    return print("perimetro del circulo es", 2*pi*radio)




if __name__==("__main__"):
    print(__name__)
    print("soy el archivo principal")
    perimetrocirculo()
    perimetrocuadrado()
    perimetrorectangulo()

else :
    print("soy una libreria")
    print(__name__)