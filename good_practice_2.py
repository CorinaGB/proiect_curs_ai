import good_practices

#cand import un fisier in altul, DocSting-ul sau este accesibil prin atributul .__doc__
print (good_practices.__doc__)

def main():
    print("Test add:", good_practices.add(2, 3))

# daca fisierul e rulat direct, codul de bloc se va executa
# protejeaza codul de test sau executabil
if __name__ == "__main__":
    main()
