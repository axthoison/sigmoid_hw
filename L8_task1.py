# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listaă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista = []
for i in range(11):
    lista.append(i)
   
print(lista)

# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți listaa creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for i in lista:
    if i % 2 == 0:
        print(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {
"name" : "Lia",
"age" : "17",
"city" : "London"
}
for i,j in person.items():
    print(i,j)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for element in row:
        print(element)

# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
for i in range(1,20,3):
    print(i)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listaă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
lista = ["A", "B", "C"]
for i, j in enumerate(lista):
    print(i,j)

# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
city = ["London", "Nevada", "Amsterdam"]
age = [20, 30, 40]
for city,age in zip(city,age):
    print(city,age)
# CODUL TĂU VINE MAI SUS:

# Creați o listaă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista = []
for i in range(11):
    lista.append(i)
   
print(lista)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
lista=[1,2,3,4,5,6,7,8,9,10]
while lista[0] <=50:
    for i in range(len(lista)):
        lista[i] *=2
    if lista[0] > 50:
        break
print(lista)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
patratperfect=[]
for i in range(1,101):
    radacina = int(i ** 0.5)
    if i == radacina ** 2 : #sau math.sqrt()
        patratperfect.append(i)
print(patratperfect)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(1,11):
    result = i*7
    print(f"{i}*7={result}")

# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listaă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listaă de perechi.

# CODUL TĂU VINE MAI JOS:
listaperechi=[]
for i in range(6):
    sublista=[]
    for j in range(6):
        sublista.append((i,j))
    listaperechi.append(sublista)

for sublista in listaperechi:
    print(sublista)

# CODUL TĂU VINE MAI SUS:

# Parcurge listaa de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for sublista in listaperechi:
    for (i,j) in sublista:
        if i<j:
            print((i,j))
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listaă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
random = [4,8,6,54,9,71,6,1,1,4,3,2]
i = 0
gasit = False
while i < len(random):
        if random[i]>10:
            print(random[i])
            gasit = True
            break
        i += 1
if not gasit:
            print("Nu exista valori mai mari decat 10")
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(7):
     for j in range(1,i+1):
        print(j,end="")
     print()
print()

# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(6):
     for j in range(5,i,-1):
        print(j,end="")
     print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
for i in range(7):
    for j in range(i, 7):
        print(chr(97 + j), end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
for i in range(8):
    for j in range(16):
        if (i + j) % 2 == 0:
            print("+", end="")
        else:
            print("-", end="")
    print()

# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
numbers = [3, 9, 27, 81, 243]
for i in range(len(numbers)):
    for j in range(0,i+1):
        print(numbers[j],end=" ")
    print()
for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        print(numbers[j], end=" ")
    print()
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.