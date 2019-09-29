import os

def limpiaPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

tiposDatos = {
    "serial"         : ["use to id", 4, "bytes"],
    "smallint"       : ["-32768 to +32767", 2, "bytes"],
    "integer"        : ["-2147483648 to +2147483647", 4, "bytes"],
    "bigint"         : ["-9223372036854775808 to +9223372036854775807", 8, "bytes"],
    "real"           : ["6 digit precision", 4, "bytes"],
    "doubleprecision": ["15 digit precision", 8, "bytes"],
    "varchar"        : ["variable-length with limit", 1/8, "bit"],
    "char"           : ["One Character", 1/8, "bit"],
    "time"           : ["date and time", 8, "bytes"],
    "timestamp"      : ["date, time and time zone", 8, "bytes"],
    "date"           : ["date", 4, "bytes"],
    "boolean"        : ["True, False / 1, 0", 1/8, "bit"]
}
tipos = tiposDatos.keys()
tipo = []

def numEntero(msg = "", lim = 999):
    try:
        numVar = int(input(msg))
        if(numVar > 0 and numVar <= lim):
            return numVar
        else:
            print("\tIngresa un valor dentro del rango. ")
            return numEntero(msg=msg, lim=lim)
    except:
        print("\tIngresa un numero entero. ")
        return numEntero(msg=msg, lim=lim)

def menuTipoDatos(num):
    limpiaPantalla()
    print("\nSelecciona el tipo de dato para la variable: " + str(num) + ".")
    print("\t{0:4}{1:16}{2:16}".format("", "Tipo de dato ", " Descripcion"))
    j = 1
    for i in tipos:
        print("\t{0:4}{1:16} {2:16}".format(str(j)+".-", i, tiposDatos.get(i)[0]))
        j+=1
    tipo = numEntero("\tSelecciona una opcion: ", len(tipos))
    return tipo-1

def calculaSizeFila(fila):
    tamFila = 0.0
    n = 1
    for i in fila:
        if (tipo[i] == "varchar"):
            n = numEntero(msg="Se necesita un tamanio n para variables varchar: ", lim=255)
            tamFila = tamFila + (n/8)
        elif (tipo[i]  == "char" or tipo[i]  == "boolean"):
            tamFila = tamFila + (1/8)
        else:
            tamFila = tamFila + tiposDatos.get(tipo[i])[1]
    return tamFila

if __name__ == "__main__":
    for i in tipos:
        tipo.append(i)

    limpiaPantalla()
    totalRegistros = numEntero("Ingresa el total de registros que tendra la DataBase: ", 1000000000)
    filasPorHoja   = numEntero("Ingresa el total de filas que tendra cada hoja: ", 1000)
    numVar = numEntero(msg="Ingresa el Numero de Variables que tendra cada fila: ", lim=250)
    fila = []
    for i in range(0,numVar):
        fila.append(menuTipoDatos(i+1))  

    tamFilaBytes = calculaSizeFila(fila)
    numHojas = totalRegistros / filasPorHoja

    tamFilaKiloBytes = tamFilaBytes / 1000
    tamFilaMegaBytes = tamFilaBytes / 1e+6
    tamFilaGigaBytes = tamFilaBytes / 1e+9
    TamFilaTeraBytes = tamFilaBytes / 1e+12

    limpiaPantalla()

    
    print("\n"*3)
    print("Estimacion del peso de una DataBase".center(90, " ") + "\n\n")
    print("\t{0:20}{1:20}{2:25}{3:25}".format("", "Fila", "Filas por Hoja", "Total DB" ) )
    print("\t{0:20}{1:20}{2:25}{3:25}".format("KiloBytes", str(round(tamFilaKiloBytes,4)), str(round(tamFilaKiloBytes * filasPorHoja,4)), str(round(tamFilaKiloBytes * totalRegistros,4)) ))
    print("\t{0:20}{1:20}{2:25}{3:25}".format("MegaBytes", str(round(tamFilaMegaBytes,4)), str(round(tamFilaMegaBytes * filasPorHoja,4)), str(round(tamFilaMegaBytes * totalRegistros,4)) ))
    print("\t{0:20}{1:20}{2:25}{3:25}".format("GigaBytes", str(round(tamFilaGigaBytes,4)), str(round(tamFilaGigaBytes * filasPorHoja,4)), str(round(tamFilaGigaBytes * totalRegistros,4)) ))
    print("\n\n\t{0:26} {1:10}".format("Numero de Registros: ", str(round(totalRegistros,4)) ))
    print("\t{0:26} {1:10}".format("Numero de filas por hoja: ", str(round(filasPorHoja,4) )))
    print("\t{0:26} {1:10}".format("Numero de hojas: ", str(round(numHojas,4))))
    print("\n"*3)