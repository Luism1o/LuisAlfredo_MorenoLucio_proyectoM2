#Longitud de una frase.

def verificar_palabra(palabra, cond): #Se añaden variables para identificar la información y poder hacer el ejercicio.
    longitud = len(palabra) #Añadimos la funcion "len" para contabilizar el número de letras

    if longitud < 4: #Se coloca la función "if" para poner el primer valor
        print( f"Por favor ingresa una palabra más larga. Solo tiene {longitud} letras.") #Si la palabra que ingresa el usuario tiene menos de tres letras se le imprime un texto.
    elif 4<= longitud <= 8: #La funcion "elif" es el segundo dato 
        print( f"La palabra {palabra} tiene la cantidad de letras correcta.") #Si el usuario coloca la cantidad de letras correcta se imprimira este texto.
        cond = False #Esta funcion es para que el ciclo "while" se detenga una vez que se coloque la cantidad de letras correctas.
    else: #La función "else" es por si no se cumplen ninguna de las dos caracteristicas anteriores.
        print( f"Por favor ingresa una palabra más corta. Tiene {longitud} letras.") #Si el usuario coloca una palabra mayor a 8 caracteres se imprime este texto.
    
    return cond #Sirve para retornar la variable cond

cond = True
while cond == True: #Se utiliza el ciclo while para repetir el ciclo por si no colocan la cantidad de caracteres correcto.
    palabra = input("Ingresa una palabra de 4 a 8 caracteres: ") #Se le pide al usuario ingresar una palabra.
    cond = verificar_palabra(palabra, cond) #Se coloca verificar_palabra para que reciba la variable palabra y cond para que regrese el valor de cond

##############################

#Encuentra el cuadrante.

x = int (input ('Ingresa el valor de x: ')) #Se le pide al usuario que coloque el valor de X.
y = int (input ('Ingresa el valor de y: ')) #Se le pide al usuario que coloque el valor de Y.
if x==0 and y==0: #Se coloca la funcion if para determinar el valor de origen.
        print ('Origen') #Si el usuario determina que el valor de X y Y es de 0 se imprime "Origen"
elif x==0: #La funcion elif va a funcionar para saber en que parte esta el cuadrante dependiendo de los datos del usuario.
    print ('Eje Y') #Dependiendo los valores que coloque el usuario se imprimirá el valor correspondiente.
elif y==0:
    print ('Eje X')
elif x>0 and y>0:
    print ('Cuadrante I')
elif x<0 and y>0:
    print ('Cuadrante II')
elif x<0 and y<0:
    print ('Cuadrante III')
else: #En dado caso que los datos colocados por el usuario no cumpla las caracteristicas anteriores entrará la funcion "else"
    x>0 and y<0
    print ('Cuadrante VI')