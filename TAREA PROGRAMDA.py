#Elaborado por: José Andres Salazar y Jocsan Pérez Coto
#Fecha de Creación: 03/04/2022 3:00pm
#Fecha de última Modificación: 29/04/2022 9:00pm 
#Versión: 3.10.2

#Este codigo representa la Tarea Programada

#importaciones
import re

#lista del abecedario general
abecedario = "abcdefghijklmnopqrstuvwxyz"

#------------------------------------------------------------------------------------------------------------------
#Funciones Principales
#------------------------------------------------------------------------------------------------------------------
#RETO #1
#1 CIFRADO CESAR
def cifradoCesar(mensaje,modo):
    """
    Funcionamiento: Realiza el cifrado cesar, codifica o decodifica según se solicite
    Entradas:
    str(mensaje) = el mensaje a codificar o decodificar
    str(modo) = modo, si quiere codificar o decodificar
    Salida: 
    str (nuevoMensaje) = el mensaje ingresado anteriormente codificado o decodificado
    """  
    lista = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mensaje = mensaje.upper() #por si ingresan minúsculas
    nuevoMensaje = ""
    for n in mensaje:
        if n in lista:
            num = lista.find(n) #encuentra la posicion de la letra
            if modo == "1": #codificar
                num = num + 3
            elif modo == "2":#decodificar
                num = num - 3
            if num >= len(lista):
                num -= len(lista) #por las ultimas 3 letras, para que vuelvan al inicio de la lista o del abecedario
            elif num < 0:
                num += len(lista) #por las primeras 3 letras, para que vayan al final de la lista
            nuevoMensaje += lista[num]
        else:
            nuevoMensaje += n #por el espacio
    return nuevoMensaje

#------------------------------------------------------------------------------------------------------------------#
#RETO #2
#2 Cifrado por llave
def obtenerCifradoLlave(frase,clave,modo):
    """
    Funcionamiento: Realiza el cifrado por llave, codifica o decodifica según se solicite
    Entradas:
    str(frase) = la frase a codificar o decodificar
    str(clave) = la clave representa la forma de realizar el proceso de cifrado
    str(modo) = modo, si quiere codificar o decodificar
    Salida: 
    str (nuevaLista) = el mensaje ingresado anteriormente codificado o decodificado
    """ 
    lista = " a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
    lista = lista.replace(" ", "") #quita los espacios
    lista = re.sub(",","",lista) #quita las comas
    num = 0
    codigo = 0
    nuevaLista = ""
    frase = frase.lower()#por si dan mayúsculas 
    clave = clave.lower()#por si dan mayúsculas 
    for i in range(len(frase)):
        if num == len(clave):
            num = 0
        if frase[i].isspace():
            nuevaLista += " "
            num = 0
        else:
            ValorFrase = encontrarValor(frase[i]) #Encuentra el valor en el abecedario
            valorClave = encontrarValor(clave[num]) #Encuentra el valor en el abecedario
            if modo == "1":
                codigo = ValorFrase + valorClave
                if codigo >= 26:
                    codigo -= 26
                nuevaLista += lista[codigo-1]
            else:
                codigo = ValorFrase - valorClave
                if codigo <= -1:
                    codigo += 26
                nuevaLista += lista[codigo-1]                
            num += 1
    return nuevaLista

#------------------------------------------------------------------------------------------------------------------#
#RETO 3
#3 CIFRADO VIGENERE
def obtenerVinere(mensaje,cifra,modo):
    """
    Funcionamiento: Realiza el VIGENERE, codifica o decodifica según se solicite
    Entradas:
    str(mensaje) = mensaje a codificar o decodificar
    str(cifra) = la cifra representa la forma de realizar el proceso de cifrado
    str(modo) = modo, si quiere codificar o decodificar
    Salida: 
    str (nuevoMensaje) = el mensaje ingresado anteriormente codificado o decodificado
    """    
    lista = "abcdefghijklmnopqrstuvwxyz"
    nuevoMensaje = ""
    bandera = True #para hacer el ciclo de la cifra
    mensaje = mensaje.lower() #por si dan mayúsculas   
    for n in range(len(mensaje)):
        if mensaje[n].isspace():
            nuevoMensaje += " "
            bandera = True #para que no se pierda el ciclo de la cifra
        elif bandera == True:
            valor = int(lista.index(mensaje[n]))#busca la posicion de la letra y lo transforma a entero
            if modo == "1":
                nuevoMensaje += lista[valor+int(cifra[0])]
            else:
                nuevoMensaje += lista[(valor-int(cifra[0]))]#cifra[0] utiliza el numero dado de la primera posicion    
            bandera = False #para hacer el ciclo de la cifra
        else:
            valor = int(lista.index(mensaje[n]))#busca la posicion de la letra y lo transforma a entero
            if modo == "2":
                nuevoMensaje += lista[valor-int(cifra[1])]
            else:
                nuevoMensaje += lista[(valor+int(cifra[1]))]#cifra[1] utiliza el numero dado de la primera posicion
            bandera = True #para hacer el ciclo de la cifra
    return nuevoMensaje

#------------------------------------------------------------------------------------------------------------------#
#RETO 4

#4 Sustitución mediante XOR y llave
def cifradoXORLlave(frase,llave,volver):
    """
    Funcionamiento: Realiza la sustitución mediante XOR y llave, codifica o decodifica según se solicite
    Entradas:
    str(mensaje) = mensaje a codificar o decodificar
    str(cifra) = la cifra representa la forma de realizar el proceso de cifrado
    str(modo) = modo, si quiere codificar o decodificar
    Salida: 
    str (nuevoMensaje) = el mensaje ingresado anteriormente codificado o decodificado
    """
    cifradoLlave = []
    num = 0
    for n in range(len(frase)):
        if num == len(llave):
            num = 0
        valorFrase = ord(frase[n])#Da el valor de las letras de frase en la tabla ASCII
        valorLlave = ord(llave[num])#Da el valor de las letras de llave en la tabla ASCII
        ASCII = (valorFrase^valorLlave) #XOR
        cifradoLlave.append(chr(ASCII))
        num += 1
    print ("\nSu mensaje nuevo es:",cifradoLlave)
    if volver == 1:
        return ""
    print ("Para este caso se puede decodificar la frase anterior, Desea decodificarla?")
    print("1. Si, decodificar y luego salir al menu")
    print("2. No, salir al menu") 
    modo = input("Ingrese el numero: ")
    if verificaModoAux(modo) == True:
        if modo == "1":
            volver = 1
            (cifradoXORLlave(cifradoLlave,llave,volver))
        else:
            return ""
    else:
        opcion2XORLlave()
    return ""


#------------------------------------------------------------------------------------------------------------------#
#RETO 5
#4 Palabra inversa
def palabraInversa(palabra):
    """
    Funcionalidad: Devuelve la frase con las letras al inverso pero manteniendo el orden que tienen este conjunto
    Entradas:
    palabra=La frase que ingreso el usuario
    Salidas:
    codigo= La frase invertida pero mantendiendo el orden
    """
    codigo=""
    palabra=palabra.split()
    for n in palabra:
        n=n[::-1]
        codigo+=n+" "
    return codigo

#------------------------------------------------------------------------------------------------------------------#
#RETO 6
def mensajeInverso(mensaje):
    """
    Funcionalidad: Manda el mensaje totalmente inverso
    Entradas:
    mensaje=La oracion que ingreso el usario
    Salidas:
    str= El mensaje invertido
    """
    return mensaje[::-1]

#------------------------------------------------------------------------------------------------------------------#
#RETO 7
def codigoTelefonoCodi(mensaje):
    """
    Funcionalidad: Convierte un texto a un codigo telefonico
    Entradas:
    mensaje= El texto ingresado por el usuario.
    Salidas:
    codigo= Devuelve el texto convertido a codigo
    """
    codigo=" "
    num2=["a","b","c"]
    num3=["d","e","f"]
    num4=["g","h","i"]
    num5=["j","k","l"]
    num6=["m","n","o"]
    num7=["p","q","r","s"]
    num8=["t","u","v"]
    num9=["w","x","y","z"]
    for n in mensaje:
        if n in num2:
            codigo+=str(2)
            codigo+=str(num2.index(n)+1)
            codigo+=" "
        elif n in num3:
            codigo+=str(3)
            codigo+=str(num3.index(n)+1)
            codigo+=" "
        elif n in num4:
            codigo+=str(4)
            codigo+=str(num4.index(n)+1)
            codigo+=" "
        elif n in num5:
            codigo+=str(5)
            codigo+=str(num5.index(n)+1)
            codigo+=" "
        elif n in num6:
            codigo+=str(6)
            codigo+=str(num6.index(n)+1)
            codigo+=" "
        elif n in num7:
            codigo+=str(7)
            codigo+=str(num7.index(n)+1)
            codigo+=" "
        elif n in num8:
            codigo+=str(8)
            codigo+=str(num8.index(n)+1)
            codigo+=" "
        elif n in num9:
            codigo+=str(9)
            codigo+=str(num9.index(n)+1)
            codigo+=" "
        elif n==" ":
            codigo+="*"
            codigo+=" "
    return codigo   

#Reto 7 descodificar
def codigoTelefonoDescodi(codigo):
    """
    Funcionalidad: Descodifica el codigo a texto
    Entradas:
    codigo= El codigo ingresado por el usario
    Salidas:
    oracion= Devuelve el codigo convertido a texto
    """
    oracion=""
    nume=0
    num2=["a","b","c"]
    num3=["d","e","f"]
    num4=["g","h","i"]
    num5=["j","k","l"]
    num6=["m","n","o"]
    num7=["p","q","r","s"]
    num8=["t","u","v"]
    num9=["w","x","y","z"]
    codigo=codigo.split(" ")
    for i in codigo:
        if i[0]=="2":
            nume=i[1]
            oracion+=num2[int(nume)-1]
        elif i[0]=="3":
            nume=i[1]
            oracion+=num3[int(nume)-1]
        elif i[0]=="4":
            nume=i[1]
            oracion+=num4[int(nume)-1]
        elif i[0]=="5":
            nume=i[1]
            oracion+=num5[int(nume)-1]
        elif i[0]=="6":
            nume=i[1]
            oracion+=num6[int(nume)-1]
        elif i[0]=="7":
            nume=i[1]
            oracion+=num7[int(nume)-1]
        elif i[0]=="8":
            nume=i[1]
            oracion+=num8[int(nume)-1]
        elif i[0]=="9":
            nume=i[1]
            oracion+=num9[int(nume)-1]
        elif i=="*":
            oracion+=" "
    return oracion

#------------------------------------------------------------------------------------------------------------------#
#RETO 8
def cifradoBinarioCodi(oracion):
    """
    Funcionalidad: Convierte un texto a binario
    Entradas:
    oracion= El texto ingresado por el usario
    Salidas:
    codigo= El texto convertido a binario.
    """
    codigo=""
    num=0
    listabi=["00000","00001","00010","00011","00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01110","01111","10000","10001","10010","10011","10100","10101","10110","10111","11000","11001"]
    listaletra=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in oracion:
        if i in listaletra:
            num=listaletra.index(i)
            codigo+=listabi[num]+" "   
        elif i ==" ":
            codigo+="* "
    
    return codigo
#Reto 8 descodificar
def resolverBinarioDescodi(mensaje):
    """
    Funcionalidad: Descodifica el codigo binario
    Entradas:
    mensaje= Elcodigo ingresado por el usario
    Salidas:
    codigo= El codigo convertido a texto
    """
    mensaje=mensaje.split(" ")
    codigo=""
    num=0
    listabi=["00000","00001","00010","00011","00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01110","01111","10000","10001","10010","10011","10100","10101","10110","10111","11000","11001"]
    listaletra=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in mensaje:
        if i in listabi:
            num=listabi.index(i)
            codigo+=listaletra[num]   
        elif i =="*":
            codigo+=" "
    if codigo=="":
        print("Ingrese una cadena valida. Revise que hayan espacios entre cada numero y que sean de 5 digitos. Y que contengan solo 1 y 0.")
    return codigo

#------------------------------------------------------------------------------------------------------------------
#Función para buscar valor
def encontrarValor(letra): #Encuentra el valor en el abecedario
    """
    Funcionamiento: busca la posicion de una letra en el abecedario
    entradas:
    str (letra): letra a analizar
    salidas:
    int (valor): valor en entero de la posicion de la letra en el abecedario
    """
    valor = int(abecedario.index(letra)) #busca la posicion de la letra en el abecedario global y lo transforma a entero
    valor += 1 #se le suma uno a la posicion porque las posiciones empiezan en cero
    return valor
#------------------------------------------------------------------------------------------------------------------
#AUXILIARES#
#------------------------------------------------------------------------------------------------------------------
def verificaLetrasAux(palabra): #Verifica que no tenga numeros en una palabra o letra y tampoco ñ o Ñ  
    if re.match("\w",palabra): #verificar si tiene espacios vacíos
        for i in palabra:
            if i == "ñ" or i == "Ñ":
                return print ("No se permite el uso de: ñ o Ñ ") #retorna este print si esta incorrecto
            if re.match("\d",i): #verificar si tiene numeros
                return print ("Por favor ingrese una palabra sin numeros") #retorna este print si esta incorrecto
        return True #retorna True si esta correcto
    return print ("Debe de ingresar una palabra correcta") #retorna este print si esta incorrecto

def verificaCifraAux(cifra): #Verifica que la cifra sean numeros y tenga solo dos numeros ej:(23),(41)
    if re.match("\d{2}$",cifra):
        return True #retorna True si esta correcto
    return print ("Por favor ingrese una cifra de dos numeros") #retorna este print si esta incorrecto

def verificaModoAux(modo): #Verifica que elija el modo correcto
    if modo == "1" or modo == "2":
        return True #retorna True si esta correcto
    return print("Por favor, debe de ingresar un número correcto") #retorna este print si esta incorrecto

#pequeña opcion/Auxiliar para cuando se decodifica
def opcion2XORLlave():
    print ("Para salir indique un 2")
    print("2. Salir al menu") 
    salir = input("Ingrese el numero: ")
    if verificaSalir(salir) == True:
        if salir == "2":
            menu()
    else:
        opcion2XORLlave()

def verificaSalir(salir): #para el reto de XORyLlave y la opcion2XORLlave
    if salir == "2":
        return True
    else:
        return False

def verificaOpcion(opcion):
    if re.match("\d{1}$",opcion): #Verifica que se le elija la opcion correcta, solo permite 1 numero 
        return True #retorna True si esta correcto
    return False #retorna False si esta incorrecto

#Reto 7 Codificar
def codigoTelefonoAux(mensaje):
    """
    Funcionalidad:Valida que solo sean letras y lo pone todo a minusculas 
    Entradas:
    mensaje: mensaje ingresado por el usuario.
    Salidas:
    str: Un caso de error segun el caso
    """
    mensaje=mensaje.lower()
    if re.match("^[a-z ]*$",mensaje):
        return codigoTelefonoCodi(mensaje)
    else: 
        return "Usted debe ingresar unicamente letras."

#Reto 8 Auxiliar codificar
def cifradoBinarioAux(oracion):
    """
    Funcionalidad:Valida que solo sean letras y lo pone todo a minusculas 
    Entradas:
    mensaje: mensaje ingresado por el usuario.
    Salidas:
    str: Un caso de error segun el caso
    """
    oracion=oracion.lower()
    if re.match("^[a-z ]*$",oracion):
        return cifradoBinarioCodi(oracion)
    else: 
        return "Usted debe ingresar unicamente letras."

#Reto 8 Auxiliar Descodificar
def resolverBinarioAux(mensaje):
    """
    Funcionalidad: Divide el mensaje 
    Entradas:
    mensaje: mensaje ingresado por el usuario.
    Salidas:
    """
    mensaje=mensaje.split(" ")
    return resolverBinarioDescodi(mensaje)

#-----------------------------------------------------------------------------------------------------------------------
#Funciones de las opciones
#-----------------------------------------------------------------------------------------------------------------------
#reto1
def opcionCesar():
    print("\n------------CIFRADO CESAR------------")
    mensaje = input("Introducir Mensaje: ")
    if verificaLetrasAux(mensaje) == True:
        print("Modos:")
        print("1. Codificar")
        print("2. Decodificar")
        modo = input("Ingrese el numero del modo: ")
        if verificaModoAux(modo) == True:
            print("Su mensaje nuevo es:",cifradoCesar(mensaje,modo))
            menu()
    opcionCesar()

#reto2
def opcionLlave():
    print("\n------------Cifrado por llave------------")
    frase = input("ingrese una frase: ")
    if verificaLetrasAux(frase) == True:
        clave = input("ingrese una clave: ")
        if verificaLetrasAux(clave) == True:
            print("Modos:")
            print("1. Codificar")
            print("2. Decodificar")
            modo = input("Ingrese el numero del modo: ")
            if verificaModoAux(modo) == True:
                print("Su frase nueva es:",obtenerCifradoLlave(frase,clave,modo))
                menu()
    opcionLlave()

#reto3
def opcionVigenere():
    print("\n------------CIFRADO VIGENERE------------")
    mensaje = input("ingrese una frase: ")
    if verificaLetrasAux(mensaje) == True:
        cifra = input("ingrese una cifra numérica de dos digitos: ")
        if verificaCifraAux(cifra) == True:
            print("Modos:")
            print("1. Codificar")
            print("2. Decodificar")
            modo = input("Ingrese el numero del modo: ")            
            if verificaModoAux(modo) == True:
                print ("Su frase nueva es:",obtenerVinere(mensaje,cifra,modo))
                menu()
    opcionVigenere()

#reto4
def opcionXORLlave():
    """
    para este caso, solo se puede ingresar la frase de tarea programada y no la
    \x07\x04\x11\x17\x04T\x1f\x01\n\x04\x00\x04\x19\x0e\x17\x04 debido a que python
    interpreta los "\" como espacios y al momento de procesar la frase inserta otros "\"
    a la par de los "\" y no se puede analizar la frase correctamente
    """ 
    volver = 0
    print("\n------------Sustitución mediante XOR y llave------------")
    frase = input("ingrese una frase: ")
    llave = input("ingrese una llave: ")
    print("En este primer caso solamente se puede codificar, desea hacerlo?")
    print("1. Si, codificar")
    print("2. No, salir al menu")
    modo = input("Ingrese el numero: ")            
    if verificaModoAux(modo) == True:
        if modo == "2":
            menu()
        else:
            cifradoXORLlave(frase,llave,volver)
            menu()
    opcionXORLlave()
#reto5
def opcionInversa():
    print("\n------------Reto 5 Palabra inversa------------")
    palabra=input("Ingrese una frase: ")
    print("Mensaje codificado: ",palabraInversa(palabra))
    menu()

#reto6
def opcionInverso():
    print("\n------------Reto 6 Mensaje inverso------------")
    mensaje=input("Ingrese una frase: ")
    print("Mensaje codificado: ",mensajeInverso(mensaje))
    menu()

#reto7
def opcionTelefono():
    try:
        print("\n------------Reto 7 Codigo Telefónico------------")
        num=int(input("Digite 1 para codificar o 2 para decodificar: "))
        if num==1:
            mensaje=input("Ingrese una frase: ")
            print("Mensaje codificado:",codigoTelefonoAux(mensaje))
            menu()
        elif num==2:
            codigo=str(input("Ingrese el codigo telefónico: "))
            print("Mensaje descodificado:",codigoTelefonoDescodi(codigo))
            menu()
        else:
            print("Usted debe de ingresar un 1 o un 2.")
            opcionTelefono()
    except ValueError:
        print("El dato ingresado deber ser un número.")
        opcionTelefono()

#reto8
def opcionBinario():
    try:
        print("\n------------Reto 8 Codigo Binario------------")
        num=int(input("Digite 1 para codificar o 2 para decodificar: "))
        if num==1:
            oracion=input("Ingrese una frase: ")
            print("Mensaje codificado: ",cifradoBinarioAux(oracion))
            menu()
        elif num==2:
            mensaje=str(input("Ingrese el codigo binario: "))
            print("Mensaje descodificado: ",resolverBinarioDescodi(mensaje))
            menu()
        else:
            print("Usted debe de ingresar un 1 o un 2.")
            opcionBinario()
    except ValueError:
        print("El dato ingresado deber ser un número.")
        opcionBinario()

#------------------------------------------------------------------------------------------------------------------
#FUNCIÓN DEL MENU PRINCIPAL
#------------------------------------------------------------------------------------------------------------------
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    print ("\n**************************")
    print ("Tarea Programada")
    print ("**************************")
    print ("1. Cifrado César")
    print ("2. Cifrado por llave")
    print ("3. Sustitución Vigenére")
    print ("4. Sustitución mediante XOR y llave")
    print ("5. Palabra inversa")
    print ("6. Mensaje inverso")
    print ("7. Codigo Telefónico")
    print ("8. Codigo Binario")
    print ("0. Salir")
    opcion = input ("Escoja una opción: ")
    if verificaOpcion(opcion) == True:
        opcion = int(opcion)
        if opcion >= 0 and opcion <= 9: 
            if opcion == 1:
                opcionCesar()
            elif opcion == 2:
                opcionLlave()
            elif opcion == 3:
                opcionVigenere()
            elif opcion == 4:
                opcionXORLlave()
            elif opcion == 5:
                opcionInversa()
            elif opcion == 6:   
                opcionInverso()  
            elif opcion == 7:   
                opcionTelefono()
            elif opcion == 8:   
                opcionBinario()
            elif opcion == 9:   
                print ("Por favor, algún numero entre las opciones")
                menu()                               
            else:
                print ("\n*********************************")
                print ("Gracias por usar nuestro programa")
                print ("*********************************")
                return ""
    else:
        print ("Por favor, ingrese algunas de las opciones")
        menu()
#------------------------------------------------------------------------------------------------------------------
#PROGRAMA PRINCIPAL
#------------------------------------------------------------------------------------------------------------------
menu()