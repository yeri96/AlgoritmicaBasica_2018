# coding: utf-8
numero1 = input("Introduce el primer número: ")
numero2 = input("Introduce el segundo número: ")
numero3 = input("Introduce el tercer número: ")

if numero1 == numero2 and numero1 == numero3:
    print "Ha escrito 3 veces el mismo número"
else:
    if numero1 == numero2 and numero1 != numero3:
        print "Has escrito uno de los números dos veces"
    else:
	if numero1 != numero2 and numero1 == numero3:
            print "has escrito uno de los números dos veces"
        else:
            if numero2 == numero1 and numero2 == numero3:
                print "Ha escrito 3 veces el mismo número"
            else:
                if numero2 == numero1 and numero2 != numero3:
                    print "Has escrito uno de los números dos veces"
                else:
                    if numero2 != numero1 and numero2 == numero3:
                        print "has escrito uno de los números dos veces"
                    else:
                        if numero3 == numero1 and numero3 == numero2:
                            print "Ha escrito 3 veces el mismo número"
                        else:
                            if numero3 == numero1 and numero3 != numero2:
                                print "Has escrito uno de los números dos veces"
                            else:
                                if numero3 != numero2 and numero3 == numero1:
                                    print "has escrito uno de los números dos veces"
                                else:
                                    print "Los tres múmeros que ha escrito son distintos"
