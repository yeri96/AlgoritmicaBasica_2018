#coding: utf-8

print "TIPOS DE GASOLINA:"
print "=================="
print "1.- Super"
print "      L Normal (1,5€)"
print "      L Turbo (1,55€)"
print "2.- Sin plomo"
print "        L Normal (1,6€)"
print "        L Con adictivos (1,65€)"
print "3.- Diesel"
print "      L Normal (1,7€)"
print "      L Fast&Furious (1,75€)"

###########################################################################
#                               VARIABLES                                 #
###########################################################################

super_normal = 1.5
super_turbo = 1.55

sin_plomo_normal = 1.6
sin_plomo_con_adictivos = 1.65

diesel_normal = 1.7
diesel_fast_furious = 1.75

gasolina = input("Que tipo de gasolina quiere: 1,2 o 3: ")

if gasolina >= 1 and gasolina <= 3:
    if gasolina == 1:
        print "GASOLINA SUPER:"
        print "    A) Normal"
        print "    B) Turbo"
        opcion = raw_input("Introduzca su categoria: A o B: ")
        if opcion == "A":
            litros = input("¿Cuantos litros quiere?: ")
            importe = litros * super_normal
            print "Importe = ", importe, "€"
        else:
            if opcion == "B":
                litros = input("¿Cuantos litros quiere?: ")
                importe = litros * super_turbo
                print "Importe = ", importe, "€"
            else:
                print "Esta opcion no es correcta intentalo de nuevo"


    elif gasolina == 2:
        print "GASOLINA SIN PLOMO:"
        print "    A) Normal"
        print "    B) Con adictivos"
        opcion = raw_input("Introduzca su categoria: A o B: ")
        if opcion == "A":
            litros = input("¿Cuantos litros quiere?: ")
            importe = litros * sin_plomo_normal
            print "Importe = ", importe, "€"
        else:
	    if opcion == "B":
                litros = input("¿Cuantos litros quiere?: ")
                importe = litros * sin_plomo_con_adictivos
                print "Importe = ", importe, "€"
            else:
                print "Esta opcion no es correcta intentalo de nuevo"

    elif gasolina == 3:
        print "DIESEL :"
        print "    A) Normal"
        print "    B) Fast&furious"
        opcion = raw_input("Introduzca su categoria: A o B: ")
        if opcion == "A":
            litros = input("¿Cuantos litros quiere?: ")
            importe = litros * diesel_normal
            print "Importe = ", importe, "€"
        else:
	    if opcion == "B":
                litros = input("¿Cuantos litros quiere?: ")
                importe = litros * diesel_fast_furious
                print "Importe = ", importe, "€"
            else:
                print "Esta opcion no es correcta intentalo de nuevo"
else:
    print "Esta opcion no es correcta intentalo de nuevo"
