# Aceasta este sarcina pentru lecția despre funcții lambda, generatori, decoratori și gestionarea excepțiilor în Python.

from sigmoid_check.python_odyssey.lesson_16.lesson_16 import Lesson16

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.9
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.9

# VERIFICATION PROCESS
session = Lesson16()
# VERIFICATION PROCESS

### Lambda Functions
"""
Creează o funcție lambda numită `task1` care adaugă 10 la un număr dat.
"""

# CODUL TĂU VINE MAI JOS
task1 = lambda x:x+10
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(1, task1))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task2` care verifică dacă un număr este par.
"""

# CODUL TĂU VINE MAI JOS
task2 = lambda x: x%2 == 0
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(2, task2))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task3` care înmulțește două strings.
"""

# CODUL TĂU VINE MAI JOS
task3 = task3 = lambda x, y: x*y
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(3, task3))
# VERIFICATION PROCESS

"""
Crează o funcție lambda numită `task4` care returnează lungimea unui șir de caractere.
"""

# CODUL TĂU VINE MAI JOS
task4 = lambda s:len(s)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(4, task4))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task5` care convertește un șir de caractere în majuscule.
"""

# CODUL TĂU VINE MAI JOS
task5 = lambda s:s.upper()
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(5, task5))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task6` care găsește maximul dintre trei strings.
"""

# CODUL TĂU VINE MAI JOS
task6 = lambda x, y, z:max(x,y,z)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(6 ,task6))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task7` care concatenează două șiruri de caractere cu un spațiu între ele.
"""

# CODUL TĂU VINE MAI JOS
task7 = lambda a,b: a +" "+ b
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(7, task7))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task8` care filtrează stringsle impare dintr-o listă și le returnează.
"""

# CODUL TĂU VINE MAI JOS
task8 = lambda strings: list(filter(lambda s: len(s) % 2 != 0, strings))
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(8, task8))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task9` care calculează factorialul unui număr folosind funcția reduce din functools (google it!).
"""

# CODUL TĂU VINE MAI JOS
from functools import reduce
task9 = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(9, task9))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task10` care sortează o listă de tuple după a doua valoare din fiecare tuple.
"""

# CODUL TĂU VINE MAI JOS
task10 = lambda strings: sorted(strings, key=lambda x: x[1])
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(10, task10))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task11` care returnează rădăcina pătrată a unui număr.
"""

# CODUL TĂU VINE MAI JOS
task11 = lambda x: x**0.5
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(11, task11))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task12` care verifică dacă un șir de caractere este palindrom.
"""

# CODUL TĂU VINE MAI JOS
task12 = lambda string : string == string[::-1]
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(12, task12))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task13` care numără numărul de vocale dintr-un șir de caractere.
"""

# CODUL TĂU VINE MAI JOS
task13 =  lambda s: sum(1 for char in s if char.lower() in 'aeiouăîâșț')
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(13, task13))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task14` care returnează inversul unui șir de caractere.
"""

# CODUL TĂU VINE MAI JOS
task14 = lambda sir: sir[::-1]
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(14, task14))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task15` care filtrează toate șirurile de caractere mai lungi de 5 caractere dintr-o listă.
"""

# CODUL TĂU VINE MAI JOS
task15 = lambda lst: list(filter(lambda s: len(s) > 5, lst))
# CODUL TĂU VINE MAI SUS
# VERIFICATION PROCESS
print(session.check_task(15, task15))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task16` care sortează o listă de dicționare după o cheie specificată.
"""

# CODUL TĂU VINE MAI JOS
task16 = lambda lista, key: sorted(lista, key=lambda d: d[key])
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(16, task16))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task17` care găsește cel mai mare divizor comun al două strings.
"""

# CODUL TĂU VINE MAI JOS
task17 = lambda x, y: x if y == 0 else task17(y, x % y) #algoritmul euclid
#impartirea pana restul = 0, respectiv a va fi cmdc
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(17, task17))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task18` care calculează suma pătratelor stringslor pare dintr-o listă.
"""

# CODUL TĂU VINE MAI JOS
task18 = lambda lst: sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, lst)))
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(18, task18))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task19` care verifică dacă un an dat este bisect.
"""

# CODUL TĂU VINE MAI JOS
task19 = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(19, task19))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task20` care găsește cel mai lung cuvânt dintr-o listă de cuvinte.
"""

# CODUL TĂU VINE MAI JOS
task20 = lambda cuvinte: max(cuvinte, key=len)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(20, task20))
# VERIFICATION PROCESS

### Generators
"""
Creează un generator numit `task21` care generează strings de la 1 la 10.
"""

# CODUL TĂU VINE MAI JOS
def task21():
    for i in range(1, 11):
        yield i
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(21, task21))
# VERIFICATION PROCESS

"""
Creează un generator numit `task22` care generează pătratele stringslor de la 1 la 10.
"""

# CODUL TĂU VINE MAI JOS
def task22():
    for i in range(1, 11):
        yield i*i
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(22, task22))
# VERIFICATION PROCESS

"""
Creează un generator numit `task23` care generează caracterele unui string primit ca input unul câte unul.
"""

# CODUL TĂU VINE MAI JOS
def task23(string):
    for char in string:
        yield char
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(23, task23))
# VERIFICATION PROCESS

"""
Creează un generator numit `task24` care generează strings pare până la un limită dată ca input.
"""

# CODUL TĂU VINE MAI JOS
def task24(limit):
    for num in range(2, limit + 1, 2):
        yield num
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(24, task24))
# VERIFICATION PROCESS

"""
Creează un generator numit `task25` care primește ca input un număr n și generează primele n strings Fibonacci.
"""

# CODUL TĂU VINE MAI JOS
def task25(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(25, task25))
# VERIFICATION PROCESS

"""
Creează un generator numit `task26` care generează strings prime până la o limită dată ca input.
"""

# CODUL TĂU VINE MAI JOS
def task26(limit):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit + 1):
        if is_prime(num):
            yield str(num)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(26, task26))
# VERIFICATION PROCESS

"""
Creează un generator numit `task27` care generează strings într-un interval specificat start, și end cu un pas dat.
"""

# CODUL TĂU VINE MAI JOS
def task27(start, end, step):
    for num in range(start, end, step):
        yield num
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(27, task27))
# VERIFICATION PROCESS

"""
Creează un generator numit `task28` care generează toate subșirurile unui șir oferit sub formă de string.
Exemplu:
pentru input-ul "ciao"
output-ul va fi: "c", "ci", "cia", "ciao", "i", "ia", "iao", "a", "ao", "o"
"""

# CODUL TĂU VINE MAI JOS
def task28(string):
    length = len(string)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield string[i:j]
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(28, task28))
# VERIFICATION PROCESS

"""
Creează un generator numit `task29` care generează factorialul stringslor de la 1 la n primind n ca input.
"""

# CODUL TĂU VINE MAI JOS
def task29(n):
    def factorial(x):
        if x == 0 or x == 1:
            return 1
        else:
            return x * factorial(x - 1)
    
    for i in range(1, n + 1):
        yield str(factorial(i))
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(29, task29))
# VERIFICATION PROCESS

"""
Creează un generator numit `task30` care generează cifrele unui număr în ordine inversă primind numărul ca input.
"""

# CODUL TĂU VINE MAI JOS
def task30(number):
    number = str(number)
    for digit in reversed(number):
        yield int(digit)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(30, task30))
# VERIFICATION PROCESS

"""
Creează un generator numit `task31` care generează toate combinațiile posibile ale elementelor dintr-o listă.
Exemplu:
pentru input-ul [1, 2, 3, 4]
output-ul va fi: (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)
"""

# CODUL TĂU VINE MAI JOS
import itertools

def task31(lst):
    for r in range(1, len(lst) + 1):
        for combo in itertools.combinations(lst, r):
            yield combo


# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(31, task31))
# VERIFICATION PROCESS

"""
Creează un generator numit `task32` care generează suma curentă a unei liste de strings primite ca input.
"""

# CODUL TĂU VINE MAI JOS
def task32(string):
    sum = 0
    for numar in string:
        sum += int(numar)
        yield sum

    pass
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(32, task32))
# VERIFICATION PROCESS

"""
Creează un generator numit `task33` care generează primele n termeni ai unei secvențe aritmetice primind a, d și n ca input unde a este primul termen, d este diferența sau pasul de creștere și n este numărul de termeni.
Exemplu:
pentru input-ul a=1, d=2, n=5
output-ul va fi: 1, 3, 5, 7, 9
"""

# CODUL TĂU VINE MAI JOS
def task33(a, d, n):
    current_term = a
    for _ in range(n):
        yield current_term
        current_term += d
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(33, task33))
# VERIFICATION PROCESS

"""
Creează un generator numit `task34` care generează puterile lui 2 până la o limită dată ca input (inclusiv).
"""

# CODUL TĂU VINE MAI JOS
def task34(limit):
    power_of_two = 1
    while power_of_two <= limit:
        yield power_of_two
        power_of_two *= 2

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(34, task34))
# VERIFICATION PROCESS

"""
Creează un generator numit `task35` care generează strings într-o secvență geometrică infinită primind a și r ca input unde a este primul termen și r este rația.
Exemplu:
pentru input-ul a=2, r=3
output-ul va fi: 2, 6, 18, 54, 162, ...
"""

# CODUL TĂU VINE MAI JOS
def task35(a, r):
    current_term = a
    while True:
        yield current_term
        current_term *= r

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(35, task35))
# VERIFICATION PROCESS

"""
Creează un generator numit `task36` care generează permutările unei liste primite ca input.
Exemplu:
pentru input-ul [1, 2, 3]
output-ul va fi: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
"""

# CODUL TĂU VINE MAI JOS
def task36(lst):
    if len(lst) == 1:
        yield tuple(lst)
    else:
        for i in range(len(lst)):
            remaining_elements = lst[:i] + lst[i+1:]
            for perm in task36(remaining_elements):
                yield (lst[i],) + perm

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(36, task36))
# VERIFICATION PROCESS

"""
Creează un generator numit `task37` care generează toți factorii primi ai unui număr dat ca input.
"""

# CODUL TĂU VINE MAI JOS
def task37(num):
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            yield factor
            num //= factor
        else:
            factor += 1
    if num > 1:
        yield num

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(37, task37))
# VERIFICATION PROCESS

"""
Creează un generator numit `task38` care generează reprezentarea binară a stringslor de la 1 la n primind n ca input.
"""

# CODUL TĂU VINE MAI JOS
def task38(n):
    for i in range(1, n + 1):
        yield bin(i)[2:]

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(38, task38))
# VERIFICATION PROCESS

"""
Creează un generator numit `task39` care generează toate anagramele unui șir dat ca input.
Exemplu:
pentru input-ul "abc"
output-ul va fi: "abc", "acb", "bac", "bca", "cab", "cba"
"""

# CODUL TĂU VINE MAI JOS
def task39(sir):
    def generate_anagrams(sir, prefix=""):
        if len(sir) == 0:
            yield prefix
        else:
            for i, c in enumerate(sir):
                remaining = sir[:i] + sir[i+1:]
                for anagram in generate_anagrams(remaining, prefix + c):
                    yield anagram

    anagrams = sorted(set(generate_anagrams(sir)))
    for anagram in anagrams:
        yield anagram
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(39, task39))
# VERIFICATION PROCESS

"""
Creează un generator numit `task40` care generează termenii unei serii matematice simple. 
De exemplu, acest generator va produce termenii unei serii în care fiecare termen este dat de formula:

termen = (-1)^n / n!

Aici, n este indexul termenului (începând de la 0), iar n! (n factorial) este produsul tuturor stringslor întregi pozitive până la n.
"""

# CODUL TĂU VINE MAI JOS
def task40():
    n = 0
    while True:
        yield (-1) ** n / factorial(n)
        n += 1

def factorial(num):
    if num == 0:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(40, task40))
# VERIFICATION PROCESS

### Decorators
"""
Creează un decorator numit `task41` care afișează timpul de execuție al unei funcții în formatul "Execution time: x seconds".
"""

# CODUL TĂU VINE MAI JOS
import time

def task41(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution time:", end_time - start_time, "seconds")
        return result
    return wrapper

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(41, task41))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task42` care afișează mesaje "Before" și "After" în jurul apelului unei funcții.
"""

# CODUL TĂU VINE MAI JOS
def task42(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(42, task42))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task43` care memorează rezultatele unei funcții într-un dicționar `cache` pentru a le returna direct dacă aceleași argumente sunt folosite din nou.
"""

# CODUL TĂU VINE MAI JOS
def task43(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return wrapper

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(43, task43))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task44` care numără de câte ori o funcție este apelată. La fiecare apel, afișează numărul de apeluri în formatul "Count: x".
"""

# CODUL TĂU VINE MAI JOS
def task44(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print("Count:", count)
        return func(*args, **kwargs)
    return wrapper

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(44, task44))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task45` care convertește rezultatul unei funcții în majuscule.
"""

# CODUL TĂU VINE MAI JOS
def task45(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(45, task45))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task46` care reîncearcă o funcție dacă aceasta aruncă o excepție. Dacă funcția aruncă o excepție, decoratorul va încerca să o apeleze din nou de 3 ori.
"""

# CODUL TĂU VINE MAI JOS
def task46(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                pass
        raise Exception("3 incercari")
    return wrapper

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(46, task46))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task47` care adaugă o valoare specificată la valoarea returnată de o funcție primind valoarea ca input.
"""

# CODUL TĂU VINE MAI JOS
def task47(value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + value
        return wrapper
    return decorator

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(47, task47))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task48` care validează tipurile argumentelor primite de o funcție și aruncă o excepție `TypeError` dacă tipurile nu sunt cele așteptate.
"""

# CODUL TĂU VINE MAI JOS
def task48(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != len(types):
                raise TypeError("Numărul de argumente nu se potrivește")

            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError("Tipul argumentelor este greșit")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(48, task48))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task49` care asigură că o funcție este apelată doar de utilizatori cu un anumit rol. Utilizând decoratorul, vei specifica rolul necesar pentru a apela funcția.

Aceasta va arunca o excepție `PermissionError` dacă utilizatorul nu are rolul specificat.
"""

# CODUL TĂU VINE MAI JOS
def task49(required_role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != required_role:
                raise PermissionError("PermissionError")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(49, task49))
# VERIFICATION PROCESS