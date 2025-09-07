#decorator = o metoda de a impacheta (wrapped) ofunctie pt a-i adauga functionlitate fara sa
            # sa modificam codul acelei functii direct


#sintaxa:
#def "nume_decorator":
#...........
#@nume_decorator
#def nume_functie
#......
#nume_functie()

#aici am creat decoratorul

def decoratorul_meu(functie_originala):    #decoratorul primeste o functie ca argument
    def functie_noua():                    #definim o fct interna care face "wrapperd" pe fct originala
        print("Inainte de functie.")       #cod care ruleaza inainte de functia originala
        functie_originala()                #apelam functia originala
        print("Dupa functie.")             #codul care ruleaza dupa functia originala
    return functie_noua                #returnam functia interna, fara paranteze, pt a fi apelata


#aici utilizez decoratorul creat mai sus:
@decoratorul_meu
def salut():
    print("Salutare tuturor!")

#am apelat functia salut
#s-a executat tot ce are functia salut in interiorul ei + functionalitatea data de decorator
salut()


def decorator(filling_function):
    def taco():
        print("Pun sos inainte....")
        filling_function()
        print("Mai pun si salata dupa.")
    return taco

@decorator
def adauga_carne():
    print("Carne gatita.")


adauga_carne()

def dubleaza_rezultatul(functie):
    def functie_noua():
        rezultat = functie()
        return rezultat * 2
    return functie_noua


@dubleaza_rezultatul
def numar():
    return 5

print(numar())

@dubleaza_rezultatul
def functie_string():
    return "Hello"

print(functie_string())

#cand Python intalneste @ decorator, decoratorul este apelat imediat, dar inca nu ruleaza functia originala
# decoratorul primeste fct ca argument si returneaza o functie noua(wrapped)
#cand apelezi functia decorat, functia noua creata de decorator se executa


#De ce este util decoratorul?
#separa responsabilitatile - decoratorul se ocupa de lucruri aditionale
#reutilizare - 1 un singur deorator poate fi folosit pt mai multe functii
#curatenie in cod - nu bagi peste tot aceleasi bucati repetitive
#poti activa/dezactiva anumite comportamente doar punand sau scotand @anume_decorator


#*args - permite functiei sa primeasca orice nr de argumente pozitionale
#se scrie cu "*"inainte
#in interiorul functiei, args devine un tuple cu toate argumentele primite

#suma pt 2 numere
def sum2(a,b):
    return a + b

print(sum2(10,20))

#suma pt 3 numere
def sum3(a,b,c):
    return a + b + c

print(sum3(10,20,30))

#suma pt 4 numere#
def sum4(a,b,c,d):
    return a +b+c+d
print(sum4(10,20,30,40))

#args este argument pe care il primeste functia
# *args este un tuple cecontine toate argumentele pozitionale primite de functie

def suma(*args):
    return sum(args)

print(suma(10,20))
print(suma(10,20,30,40,50,60,70,400))


#**kwargs permite fctsa primeasca orice nr de argumente
#se scrie cu "**" inainte de nume
# in interiorul functiei , kwargs devine un dictionar cu perechi:"cheie:valoare"

def prezentare(**kwargs):
    for cheie, valoare in kwargs.items(): # dict.items() returneaza toate perechile cheie:valoare ale unui dictionar
        print(f"{cheie}:{valoare}")        #e folosita pt aitera printr-un dictionar

#apelam functia cu diferite argumente numite
prezentare(nume ="Mircea", varsta =31)
prezentare(marca= "Tesla", model = "Model 3", anul = 2023)

#**kwargs - permite functiei sa primeasca un numar variabil de argumente numite (cheie:valoare)


#decorator ce foloseste *args pt a putea prelua orice nr de argumente de la functia dorita:

def decorator_3(functia_originala):
    def functia_noua(*args):
        print("Primul mesaj.")
        rezultat = functia_originala(*args) #aici se calculeaza si apeleaza noua variabila "rezultat"si ea e 8
        print(rezultat)    #daca pun acest print - se va afisa aici valoarea variabile "rezultat"
        print("Al doilea mesaj.")
        return rezultat
    return functia_noua

@decorator_3
def aduna(a,b):
    return a+b

print(aduna(5,3))

#generator
#generator = o functie speciala careproduce valri pe rand, pe masura ce ele sunt cerute,
#            in lc sa genereze toate valorile deodata si sa le stocheze in  memorie
#o functie normala in python -> folosim "return"
#un generator -> folosim "yield"(in loc de "return")
#un generator foloseste memorie mai eficient decat  functie normala

#definirea unui generator (folosim "yield" in loc de "return")

def numere_pare(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for numar in numere_pare(10):
    print(numar)

#yield "tine mine" unde a ramas functia, astfel incat la urmatoarea iteratie sa continue de unde  a ramas
# nu ocupa multa memorie, pt ca nu genereaza toate valorile deodata

#cand safolosesti generatori?
#datele sunt foarte mari:fisiere mari, milioane valori
#economisesti memorie


#acelasi exemplu doar ca e cu "return"

def numere_pare2(n):
    lista = []
    for i in range(n):
        if i % 2 == 0:
            lista.append(i)   #append - adauga valori in lista
    return lista

rezultat_nou = numere_pare2(10000)
print(rezultat_nou)
#toate valorile sunt stocate in lista


#yield emite cate un elemnt pe rand, fara sa stocheze 100000 in memorie
#filtrarea if < 5 face ca doar 5 elementele sa fie produse

def elemente_mici(n):
    for i in range(n):
        if i < 5:
            yield i


for e in elemente_mici(100000):
    print(e)



gen = elemente_mici(100)
#next il folosimpt a luaelemnetele unul cate unul
print(next(gen))
print(next(gen))
print(next(gen))

#daca apelam next() dupa ce generatorul s-a terminat, apare StopIteration


