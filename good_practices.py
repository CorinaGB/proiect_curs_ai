
# variabilelel trebuie sa contina litere mici, daca avem mai multe cuvinte separate cu "_"
student_count = 15
list_total_of_products = 15
#de evitat nume vagi, sau abrevieri excesive
# ex de evitat:a ,b, c,var,x, data


#constantele se scriu conventional cu majuscule pt a le distinge de variabile
#ex: MAX_SIZE; DEFAULT_COLOR
MAX_SIZE = 100
DEFAULT_COLOR = "red"
#daca vedeti ceva de genul, ele sunt considerate constante (prin conventie) si nu ar trebui modificate
# poate fi si o lista considerata constanta



#functii-e necesar sa folosim litere mici  separate prin "_"
#ex:calculate_total, print_report
#de evitat nume vagi, de ex : func, do_somethng, creat_something

# Clase - o clasaeste un sablon pentru crearea obiectelor
# numele claselor trebuie sa inceapa cu litera mare,daca sunt 2 cuvinte,fiecasre cuvant incepe cu litera mare
#ex: StudentProfile, InventoryManager(under score nu trebuie folosita la clase)
#obiectele trebuie trecute cu litera mica
#student_1 = StudentProfile() - obiectul "student_1" e instanta clasei StudentProfile()


#foloseste 4spatii pt identare (standard Python)
#nu supra - comenta cod simplu si nu scrie comentarii redundante

#docstrin-uri - tot un fel de comentariu
#se scriu intre triple quotes """ """
#servesc pt documentarea functiilor, claselor sau modulelr
# sunt accesibile la runtime, de ex cu help()

def calculate_area(raza):
    """
    Calculeaza aria unui cerc
    :param raza: raza cercului
    :return: aria cercului
    """
    return 3.14159 * 2 ** 2

help(calculate_area)

# foloseste spatiul in jurul peratorilor si dupa virgule
# se aplica si aceasta practica si pentru  liste/tuple/set si pentru argumentele unei functii
items = [1, 2, 3, 4, 5]
age = 18
total = age + 5

#foloseste conditii clare si explicite la structurii "if"
#ex: if age <= 18:
#evita conditii complicate sau if - uri  foarte impricate
#evita : if(age <= 18 and age < 65) or (membership and not banned) and score > 100)
#codul e greu de de citit si de intretinut
#trebuie sanalizezi fiecare parte ca sa intelegi logica + creste riscul de erori

#folosese "list comprehension" - pentru transformari de date
#ex :[x ** 2 for i in numbers]
# evita comprehension complexe sau impricate (dificil de citit)


#foloseste try-except pt erori asteptate
# nu captura toate exceptiile, fii specific cu tipurile de exceptii


#la crearea de functii, da nume foarte sugestive
# exemplu corect mai jos:
def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price

discounted_price = calculate_discount(100, 10)

#(unde nu avem nume specifice)
#Define function
def calc_d(p, d):
    fp = p - (p * d / 100)  # Calculate result
    return fp  # Return result

# Unclear and vague
dp = calc_d(100, 10)  # Call function with the following arguments: 100 and 10



#__name__ e o var interna pe care Python o seteaza automat
#daca rulezi unfisier direct (good_practice.py) atunci __name_ == __main__


def add(a, b):
    return a + b

def main():
    print("Test add:", add(2,3))

if __name__ == "__main__":
    main()