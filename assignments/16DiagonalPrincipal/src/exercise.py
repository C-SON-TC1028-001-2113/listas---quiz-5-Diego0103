def diagonal(m):
    diag = []
    largo = len(m)
    for i in range(largo):
        diag.append(m[i][i])
    return(diag)

def main():
    reng = int(input())
    columnas = int(input())
    if reng==columnas:
        valores = []
        matriz = []
        for i in range(reng):
            for j in range (columnas):
                valor= int(input())  
                valores.append(valor)
            matriz.append(valores)
            valores = []
        print (diagonal(matriz))
    else:
        print ("La matriz no es cuadrada")


if __name__=='__main__':
    main()
