from sys import stdin
import os
import random
import datetime
A=["0"," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"," K"," L"," M"," N"," O"," P"," Q"," R"," S"," T"," U"," V"," W"," X"," Y"," Z"]
N=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
L=[]
CPU=[]
CPU1=[]
def pri(L):
    """pre:entra la matriz L en el estado que se encuentre
       pos: muestra la matriz para en pantalla"""
    n=0
    while n<len(L):
        print("["+",".join([str(i) for i in L[n]])+"]")
        n=n+1
def Dificultad():
    """pre:le pide al jugador que ingrese el nivel de dificultad
       pos:valida el valor ingresado y retorna la dificultad validada"""
    print("Selecciona la dificultad de tu partida entre el 1 y 5")
    a=stdin.readline().strip()
    if a.isdigit()== True:
        if int(a)<1 or int(a)>5:
            print("valor incorrecto trata de nuevo")
            main()
        else:
            return a
    else:
        print("dato no valido")
        main()
def instrucciones():
    """Da la informacion al jugador sobre las reglas de la partida"""
    print("a continuacion se ubicaran tus barcos de manera aleatoria segun la dificultad escogida")
    print("---------------------------------------------------------------------------------------")
    print("Las reglas son:")
    print("1. Tienes un limite de turnos para ganar la partida que varia segun la dificultad, si se te acaban los turnos pierdes")
    print("2. Pierdes un turno cuando fallas al atacar o das una posicion no valida")
    print("3. No pierdes turnos cuando aciertas el barco del rival o tratas atacar una posicion que atacaste antes")
    print("4. El rival te atacara de manera constante, es decir aun cuando falles,aciertes,digas una posicion no valida el rival te seguira atacando")
    print("5. cuando se pida la coordenada vertical se debe poner una letra que este en el tablero de juego de lo contrario no sera un movimiento valido")
    print("6. cuando se pida la coordenada horizontal se debe poner un numero que este en el tablero de juego de lo contrario no sera un movimiento valido")
    print("7. En el tablero de juego 'xx' quiere decir que hubo un impacto en esa posicon y 'oo' quiere decir que hubo un impacto fallido en esa posicion")
    print("8. Buena suerte soldado")
    print("---------------------------------------------------------------------------------------")
    z=stdin.readline().strip()
def Tablero(L,a,A,N):
    """pre:Entra una lista vacia y dos listas ya formadas junto con la variable pedida para la dificultad del juego
       pos:Sale el tablero creado para la partida en la matriz L segun la dificultad elegida"""
    a=int(a) 
    if a<=5 and a>=1:
        #crea la matriz correspondiente a la dificultad#        
        for i in range(2+a*5):
            L.append([])
            for j in range(2+a*5):
                L[i].append("--")
        for i in range(2+a*5):
            L[0][i]=A[i]
        for i in range(2+a*5):
            L[i][0]=N[i]
  
def Buct(a,A,N,CPU):
    """pre:entra el tablero del rival con submarinos
    pos:sale el tablero del rival con destructores"""
    n=a
    x=1
    def U1(n,x):
        if CPU[N.index(c4)][A.index(c3)]=="--" and (int(N.index(c4)-2)>=(1)):
            if CPU[N.index(c4)-1][A.index(c3)]=="--" and CPU[N.index(c4)-2][A.index(c3)]=="--":
                CPU[N.index(c4)][A.index(c3)]="B"+str(x)
                CPU[N.index(c4)-1][A.index(c3)]="B"+str(x)
                CPU[N.index(c4)-2][A.index(c3)]="B"+str(x)
            else:
                n=n+1
                x=x-1
        else:
            n=n+1
            x=x-1
    def L1(n,x):
        if CPU[N.index(c4)][A.index(c3)]=="--"  and (int(A.index(c3)-2)>=(1)):
            if CPU[N.index(c4)][A.index(c3)-1]=="--" and CPU[N.index(c4)][A.index(c3)-2]=="--" :
                CPU[N.index(c4)][A.index(c3)]="B"+str(x)
                CPU[N.index(c4)][A.index(c3)-1]="B"+str(x)
                CPU[N.index(c4)][A.index(c3)-2]="B"+str(x)
            else:
                n=n+1
                x=x-1
        else:
            n=n+1
            x=x-1
    def D1(n,x):
        if CPU[N.index(c4)][A.index(c3)]=="--"  and int(N.index(c4)+2)<=(int(1+(a*5))):
            if CPU[N.index(c4)+1][A.index(c3)]=="--" and CPU[N.index(c4)+2][A.index(c3)]=="--":
                CPU[N.index(c4)][A.index(c3)]="B"+str(x)
                CPU[(N.index(c4))+1][A.index(c3)]="B"+str(x)
                CPU[N.index(c4)+2][A.index(c3)]="B"+str(x)
            else:
                n=n+1
                x=x-1
        else:
            n=n+1
            x=x-1
    def R1(n,x):
        if CPU[N.index(c4)][A.index(c3)]=="--" and (int(A.index(c3)+2)<=(int(1+(a*5)))) :
            if CPU[N.index(c4)][A.index(c3)+1]=="--" and CPU[N.index(c4)][A.index(c3)+2]=="--" :
                CPU[N.index(c4)][A.index(c3)]="B"+str(x)
                CPU[N.index(c4)][A.index(c3)+1]="B"+str(x)
                CPU[N.index(c4)][A.index(c3)+2]="B"+str(x)
            else:
                n=n+1
                x=x-1
        else:
            n=n+1
            x=x-1
    while n!=0:
        c3=random.choice(A[1:int(a*5)+2])
        c4=random.choice(N[1:int(a*5)+2])
        if int(c4)<=9:
                c4=("0"+str(int(c4)))
        #Caso base el de la esquina superior izquierda A1 
        if c3==" A" and c4=="01" and CPU[N.index(c4)][A.index(c3)]=="--":
            L1=["R","D"]
            CD=random.choice(L1)
            if CD=="D":
                D1(n,x)
            elif CD=="R":
                R1(n,x)
        #Caso base el de la esquina superior derecha A(ultimo numero del tablero) 
        elif c3==" A" and int(c4)==a*5+1 and CPU[N.index(c4)][A.index(c3)]=="--":
            L2=["R","U"]
            CD=random.choice(L2)
            if CD=="R":
                    R1(n,x)
            elif CD=="U":
                    U1(n,x)
         #Caso base el de la esquina inferior izquierda (ultima letra del tablero)1     
        elif c3==A[a*5+1] and c4=="01" and CPU[N.index(c4)][A.index(c3)]=="--":
            L3=["D","L"]
            CD=random.choice(L3)
            if CD=="D":
                D1(n,x)
            elif CD=="L":
                L1(n,x)
         #Caso base el de la esquina inferior derecha (ultima letra)(ultimo numero)del tablero
        elif c3==A[a*5+1] and int(c4)==a*5+1 and CPU[N.index(c4)][A.index(c3)]=="--":
            L4=["U","L"]
            CD=random.choice(L4)
            if CD=="L":
                L1(n,x)
            elif CD=="U":
                U1(n,x)
        #caso para la primera columna
        elif c3=="A" and int(c4)<=1+a*5 and CPU[N.index(c4)][A.index(c3)]=="--":
            L5=["D","R","D"]
            CD=random.choice(L5)
            if CD=="D":
                D1(n,x)
            elif CD=="U":
                U1(n,x)
            elif CD=="R":
                R1(n,x)
        #caso para la ultima columna
        elif c3==A[a*5+1] and int(c4)<=1+a*5 and CPU[N.index(c4)][A.index(c3)]=="--":
            L6=["D","L","U"]
            CD=random.choice(L6)
            if CD=="D":
                D1(n,x)
            elif CD=="U":
                U1(n,x)
            elif CD=="L":
                L1(n,x)
        #caso para la ultima fila
        elif int(A.index(c3))<=1+a*5 and c4==N[1+a*5] and CPU[N.index(c4)][A.index(c3)]=="--":
            L7=["U","R","L"]
            CD=random.choice(L7)
            if CD=="R":
                R1(n,x)
            elif CD=="U":
                U1(n,x)
            elif CD=="L":
                L1(n,x)
         #caso para la primera fila
        elif int(A.index(c3))<=1+a*5 and c4=="01" and CPU[N.index(c4)][A.index(c3)]=="--":
            L8=["U","R","L"]
            CD=random.choice(L8)
            if CD=="R":
                R1(n,x)
            elif CD=="D":
                D1(n,x)
            elif CD=="L":
                L1(n,x)
        # cualquier posicion que no sea un borde
        elif int(A.index(c3))<1+a*5 and int(c4)<1+a*5 and CPU[N.index(c4)][A.index(c3)]=="--" :
            L9=["U","R","L","D"]
            CD=random.choice(L9)
            if CD=="U":
                U1(n,x)
            elif CD=="R":
                R1(n,x)
            elif CD=="D":
                D1(n,x)
            elif CD=="L":
                L1(n,x)
        x=x+1
        n=n-1
def destrcp(a,A,N,CPU):
    """pre:entra el tablero del rival con submarinos
    pos:sale el tablero del rival con destructores"""
    n=a+1
    x=1
    def U(n,x):
        if CPU[N.index(c4)][A.index(c3)]=="--" and CPU[N.index(c4)-1][A.index(c3)]=="--":
            CPU[N.index(c4)][A.index(c3)]="D"+str(x)
            CPU[N.index(c4)-1][A.index(c3)]="D"+str(x)
        else:
            n=n+1
            x=x-1
    def L(n,x):
        if CPU[N.index(c4)][A.index(c3)]=="--" and CPU[N.index(c4)][A.index(c3)-1]=="--":
            CPU[N.index(c4)][A.index(c3)]="D"+str(x)
            CPU[N.index(c4)][A.index(c3)-1]="D"+str(x)
        else:
            n=n+1
            x=x-1
    def D(n,x):
        if CPU[N.index(c4)][A.index(c3)]=="--" and CPU[N.index(c4)+1][A.index(c3)]=="--":
            CPU[N.index(c4)][A.index(c3)]="D"+str(x)
            CPU[N.index(c4)+1][A.index(c3)]="D"+str(x)
        else:
            n=n+1
            x=x-1
    def R(n,x):
        if CPU[N.index(c4)][A.index(c3)]=="--" and CPU[N.index(c4)][A.index(c3)+1]=="--":
            CPU[N.index(c4)][A.index(c3)]="D"+str(x)
            CPU[N.index(c4)][A.index(c3)+1]="D"+str(x)
        else:
            n=n+1
            x=x-1
    while n!=0:
        c3=random.choice(A[1:int(a*5)+2])
        c4=random.choice(N[1:int(a*5)+2])
        if int(c4)<=9:
                c4=("0"+str(int(c4)))
        #Caso base el de la esquina superior izquierda A1 
        if c3=="A" and c4=="01" and CPU[N.index(c4)][A.index(c3)]=="--":
            L1=["R","D"]
            CD=random.choice(L1)
            if CD=="D":
                D(n,x)
            elif CD=="R":
                R(n,x)
        else:
            #Caso base el de la esquina superior derecha A(ultimo numero del tablero) 
            if c3=="A" and int(c4)==a*5+1 and CPU[N.index(c4)][A.index(c3)]=="--":
                L2=["R","U"]
                CD=random.choice(L2)
                if CD=="R":
                        R(n,x)
                elif CD=="U":
                        U(n,x)
            else:
		 #Caso base el de la esquina inferior izquierda (ultima letra del tablero)1     
                if c3==A[a*5+1] and c4=="01" and CPU[N.index(c4)][A.index(c3)]=="--":
                    L3=["D","L"]
                    CD=random.choice(L3)
                    if CD=="D":
                        D(n,x)
                    elif CD=="L":
                        L(n,x)
                 #Caso base el de la esquina inferior derecha (ultima letra)(ultimo numero)del tablero
                elif c3==A[a*5+1] and int(c4)==a*5+1 and CPU[N.index(c4)][A.index(c3)]=="--":
                    L4=["U","L"]
                    CD=random.choice(L4)
                    if CD=="L":
                        L(n,x)
                    elif CD=="U":
                        U(n,x)
                #caso para la primera columna
                elif c3=="A" and int(c4)<=1+a*5 and CPU[N.index(c4)][A.index(c3)]=="--":

                    L5=["D","R","D"]
                    CD=random.choice(L5)
                    if CD=="D":
                        D(n,x)
                    elif CD=="U":
                        U(n,x)
                    elif CD=="R":
                        R(n,x)
                #caso para la ultima columna
                elif c3==A[a*5+1] and int(c4)<=1+a*5 and CPU[N.index(c4)][A.index(c3)]=="--":
                    L6=["D","L","U"]
                    CD=random.choice(L6)
                    if CD=="D":
                        D(n,x)
                    elif CD=="U":
                        U(n,x)
                    elif CD=="L":
                        L(n,x)
                #caso para la ultima fila
                elif int(A.index(c3))<=1+a*5 and c4==N[1+a*5] and CPU[N.index(c4)][A.index(c3)]=="--":
                    L7=["U","R","L"]
                    CD=random.choice(L7)
                    if CD=="R":
                        R(n,x)
                    elif CD=="U":
                        U(n,x)
                    elif CD=="L":
                        L(n,x)
                 #caso para la primera fila
                elif int(A.index(c3))<=1+a*5 and c4=="01" and CPU[N.index(c4)][A.index(c3)]=="--":
                    L8=["U","R","L"]
                    CD=random.choice(L8)
                    if CD=="R":
                        R(n,x)
                    elif CD=="D":
                        D(n,x)
                    elif CD=="L":
                        L(n,x)
                # cualquier posicion que no sea un borde
                elif int(A.index(c3))<=1+a*5 and int(c4)<=1+a*5 and CPU[N.index(c4)][A.index(c3)]=="--":
                    L9=["U","R","L","D"]
                    CD=random.choice(L9)
                    if CD=="U":
                        U(n,x)
                    elif CD=="R":
                        R(n,x)
                    elif CD=="D":
                        D(n,x)
                    elif CD=="L":
                        L(n,x)
               
        x=x+1
        n=n-1

def subcp(a,A,N,CPU):
    """pre:entra el tablero de juego junto a las otras lista y la variable de dificultad
     pos:Sale el tablero del rival editado con los "submarinos" ubicados en el tablero"""
    n=a+2
    while n!=0:
        c1=random.choice(A[1:int(a*5)+2])                   
        c2=random.choice(N[1:int(a*5)+2])   
        #verifico que los valores ingresados puedan ser ubicados en el tablero
        if int(c2)<=9:
            c2="0"+str(int(c2))
            if A.index(c1)<=int(1+a*5):
            #verifico que la posicion donde se vaya a colocar el submarino no este ocupada  
                if CPU[N.index(c2)][A.index(c1)]=="--":
                    CPU[N.index(c2)][A.index(c1)]="SS"
                else:
                    n=n+1
            else:
                n=n+1 
        else:
           #mismo proceso para cuando c2>9                
            if int(c2)<=int(1+a*5):
                if A.index(c1)<=int(1+a*5):
                    if CPU[N.index(c2)][A.index(c1)]=="--":
                        CPU[N.index(c2)][A.index(c1)]="SS"
                    else:
                        n=n+1
            else:
                n=n+1
        n=n-1

def play(CPU,A,N,b):
    """pre:entra un tablero de juego"""
    """pos:sale la cantidad de mar en el tablero"""
    c=0
    for i in range(2+b*5):
        c=c+(CPU[i].count("--"))
    return c
 
def vic(l):
    """pre: entra una lista con los puntajes de la partida
       pos: Compara los puntajes y dice si ganaste o perdiste""" 
    if l[0]>l[1]:
        print("Felicidades")
        print("tu puntaje fue "+str(int(l[0])-30+int(l[2])))
        p=str(int(l[0])-30+int(l[2]))+", Ganando la partida"
        return p
    if l[1]>l[0]:
        print("Perdiste")
        print("tu puntaje fue "+str(int(l[1])-30+int(l[2])))
        p=str(int(l[1])-30+int(l[2]))+", Perdiendo la partida"
        return p
    if L[2]==0:
        print("se te acabaron los turnos")
        print("perdiste")
        p="0, Perdiendo la partida"
        return p
def jugada(c,L,b,CPU,A,N,d,CPU1):
    """pre:entran los tableros tanto del jugador como el del rival
    pos:salen los impactos al jugador y indica cuando gana o pierde el jugador"""
    T=(10+b*8)
    while c!=(1+b*5)**2 and d!=(1+b*5)**2 and T!=0:
        print("tu tablero")
        pri(L)
        print("Tienes "+str(T)+" Turnos para vencer al rival")
        print("------------------------------------------------------------------------------------------------------------------")
        print("te toca atacar")
        print("------------------------------------------------------------------------------------------------------------------")
        print("di una coordenada  vertical")
        c0=" "+str(stdin.readline()).upper().strip()    
        if str(c0)in A[1:(2+b*5)]:
            print("di una coordenada horizontal")
            c10=stdin.readline().strip()
            if c10.isdigit():
                if int(c10)<=9 and int(c10)>=1:
                    c10=("0"+str(int(c10)))
                if int(c10)>=10 and int(c10)<=26:
                    c10=(str(c10))
                if c10 in N[1:(2+b*5)]:
                    if CPU[N.index(c10)][A.index(c0)]!="--" and CPU[N.index(c10)][A.index(c0)]!="xx"and CPU[N.index(c10)][A.index(c0)]!="oo":
                        if CPU[N.index(c10)][A.index(c0)]=="SS":
                            CPU[N.index(c10)][A.index(c0)]="xx"
                            CPU1[N.index(c10)][A.index(c0)]="xx"
                            print("Le has dado")
                            print("Has undido un submarino")
                            c=c+1
                        else:
                            CPU[N.index(c10)][A.index(c0)]="xx"
                            CPU1[N.index(c10)][A.index(c0)]="xx"
                            print("Le has dado")
                            c=c+1
                            X=1
                            while X<=(b+1):
                                j=0
                                for i in range(2+(b*5)):
                                    j=j+(CPU[i].count("D"+str(X)))
                                if j==0:
                                    print("Has undido el destructor"+str(X))
                                    X=X+1
                                else:
                                    X=X+1
                            X=1
                            while X<=(b):
                                j=0
                                for i in range(2+(b*5)):
                                    j=j+int((CPU[i].count("B"+str(X))))
                                if j==0:
                                    print("Has undido el Buque"+str(X))
                                    X=X+1
                                else:
                                    X=X+1
                    elif CPU[N.index(c10)][A.index(c0)]=="--":
                        CPU[N.index(c10)][A.index(c0)]="oo"
                        CPU1[N.index(c10)][A.index(c0)]="oo"
                        print("has fallado")
                        T=T-1
                    elif CPU[N.index(c10)][A.index(c0)]=="xx" or CPU[N.index(c10)][A.index(c0)]=="00":
                        print("Ya has atacado esa zona")

                else:
                    print("Dato no valido, vuelve a intentarlo")
                    T=T-1
            else:
                print("Dato no valido, vuelve a intentarlo")
                T=T-1
        else:
            print("Dato no valido, vuelve a intentarlo")
            T=T-1
        print("------------------------------------------------------------------------------------------------------------------")
        print("registro de ataque contra el enemigo")
        pri(CPU1)
        c1=random.choice(A[1:int(b*5)+2])
        c2=random.choice(N[1:int(b*5)+2])
        if L[N.index(c2)][A.index(c1)]!="--" and L[N.index(c2)][A.index(c1)]!="oo" and L[N.index(c2)][A.index(c1)]!="xx":
            L[N.index(c2)][A.index(c1)]="xx"
            print("Te han dado!")
            d=d+1
        else:
            if  L[N.index(c2)][A.index(c1)]=="oo" or L[N.index(c2)][A.index(c1)]=="xx":
                print("tu enemigo a fallado!")
            else:
                print("tu enemigo a fallado!")
                L[N.index(c2)][A.index(c1)]="oo"
        print("------------------------------------------------------------------------------------------------------------------")
        l=[]
        l.append(c)
        l.append(d)
        l.append(T)
    return l 
print("Bienvenido Jugador porfavor ingresa tu nombre")
nombre=stdin.readline().strip()    
def main():
    D=Dificultad()
    if D!=None:
        Tablero(L,D,A,N)
        Tablero(CPU1,D,A,N)
        Tablero(CPU,D,A,N)
        instrucciones()
        Buct(int(D),A,N,CPU)
        Buct(int(D),A,N,L)
        destrcp(int(D),A,N,CPU)
        destrcp(int(D),A,N,L)
        subcp(int(D),A,N,CPU)
        subcp(int(D),A,N,L)
        k=play(CPU,A,N,int(D))
        K=play(L,A,N,int(D))
        l=jugada(k,L,int(D),CPU,A,N,K,CPU1)
        p=vic(l)
        fin=datetime.datetime.now()
        print("la partida finalizo")
        r=print(fin)
        script_dir = os.path.dirname(__file__)
        script_dir = script_dir + "/Resultados.txt"
        f=open(script_dir,"a")
        f.write("datos de la ultima partida del "+str(fin)+", Nombre del jugador: "+str(nombre)+", el puntaje fue "+str(p))
        f.write("\n")
        f.close()
main()
