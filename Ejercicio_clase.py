print("////////////////////////////////////////////////////////////////////////////////////////////////////")
#Funcion que calcula los descuentos 
def descuentos():
    cant=int(input("Escriba la cantidad de unidades del producto que desea comprar: "))
##AQUI HABIA UN PROBLEMA CON EL IF PUES HABIAS PUESTO OR >0 POR LO QUE PRATCICAMENTE TOMO TODOS LOS NUMEROS
##Y ARROJABA QUE NO TENIA DESCUENTO YA HICE EL CAMBIO
    if(cant<=4 or cant==0):
        precioR=4000*cant
        print("Su Compra no tendrá descuento.")
        print("El valor de su compra es de ",precioR,"$")
        print("Gracias por utilizar nuestros servicios electrónicos, que tenga un buen dia.")
    else:
        if((cant>=5 or cant<=9)and cant):
            descuento=4000*cant*0.05
            totalC=(4000*cant)-descuento
            precioR=4000*cant
            print("Su compra costará ",precioR,"$")
            print("El descuento de su compra será de ",descuento,"$\n")
            print("El valor de su compra ahora es de ",totalC,"$\n")
            print("Gracias por utilizar nuestros servicios electrónicos, que tenga un buen dia.")
        elif(cant>=10 or cant<=19):
            descuento=4000*cant*0.10
            totalC=(4000*cant)-descuento
            precioR=4000*cant
            print("Su compra costará ",precioR,"$")
            print("El descuento de su compra será igual a ",descuento,"$\n")
            print("el valor de su compra ahora es de ",totalC,"$\n")
            print("Gracias por utilizar nuestros servicios electrónicos, que tenga un buen dia.")
        elif(cant>=20):
            descuento=4000*cant*0.20
            totalC=(4000*cant)-descuento
            precioR=4000*cant
            print("Su compra costará ",precioR,"$")
            print("El descuento de su compra será igual a ",descuento,"$\n")
            print("el valor de su compra ahora es de ",totalC,"$\n")
            print("Gracias por utilizar nuestros servicios electrónicos, que tenga un buen dia.")
#vamos a ver -- si lo metemos en un ciclo el menu se ejecuta bien, si llegan a meter datos erroneos el ciclo se repite
print("\n\tBienvenido a Gaseosas.SAS\nConozca nuestros productos de gaseosas en botellas de 1.5L")
print("\nTabla de precios:")
print("- Pepsi 4.000$\t\t- Coca-cola 4.000$\t\t- Colombiana 4.000$\n")
while True:
    Producto_seleccionado=int(input("Por favor escriba:\n1) Si desea adquirir PEPSI\n2) Si desea adquirir COCA-COLA\n3) Si desea adquirir COLOMBIANA \n"))
    
    if Producto_seleccionado==1: #PEPSI
        print("Usted ha seleccionado el producto: 1.)Pepsi \tEXITOSAMENTE")
        descuentos()
        break
    elif Producto_seleccionado==2: #COCA-COLA
        print("Usted ha seleccionado el producto: 2.) Coca-Cola \tEXITOSAMENTE")
        descuentos()
        break
    elif Producto_seleccionado==3: #COLOMBIANA
        print("Usted ha seleccionado el producto: \n3.)Colombiana\tEXITOSAMENTE")
        descuentos()
        break
    else:
        print("\nUsted no ha seleccionado ninguno de los productos disponibles, vuelva a intentarlo\n")