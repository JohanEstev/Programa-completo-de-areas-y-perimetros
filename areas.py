def areacuadrado():
    lado =float(input("ingrese el valor del lado: " ))
    return print ("area del cuadrado es", lado**2)


def arearectangulo():
    base =float (input("ingrese el valor de la base: " ))
    altura =float (input("ingrese el valor de la altura: " ))
    return print ("area del rectangulo es", base*altura)



def areacirculo():
    radio =float(input("ingrese el valor del radio: " ))
    pi=3.1416
    return print ("area del circulo es", pi*radio*2)




if __name__==("__main__"):
    print(__name__)
    print("soy el archivo principal")
    areacirculo()
    areacuadrado()
    arearectangulo()

else :
    print("soy una libreria")
    print(__name__)
    