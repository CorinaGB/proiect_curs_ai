#creare functie "dramas"
def dramas(movies):
     return [movie["title"] for movie in movies if "Drama" in movie["genres"]]

movies =[
    {'title':"Schreck",'genres': ['Animation'],'runtime':120,'price':60},
    {'title':"Avengers:Endgame",'genres': ['Actions','Adventure'],'runtime':150,'price':40},
    {'title':"Forrest Gump",'genres': ['Drama','Romance'], 'runtime':90,'price':25}
]
print(dramas(movies))

#functie numita "findbyGenre" care returneaza lista cu titlul filmelor care se potrivesc unui gen
#functia primeste 2 argumente: genul de cautat si lista de filme
def findbyGenre(genre, movies):#
    return[movie["title"]for movie in movies if genre in movie["genres"]]

print(findbyGenre("Drama",movies))
print(findbyGenre("Animation",movies))

#functie numita "longestMovie" care determina filmul cu cea mai mare durata dintr-o lista
def longestMovie(movies):
    return max(movies, key = lambda movie :movie['runtime'])
#folosim max cu cheia"runtime" pt a gasi filmul cu durata cea mai mare
print(longestMovie(movies))


#functie care det cel mai ieftin film
def cheapestMovie(movies):
    return min(movies, key =lambda movie:movie["price"])

print(cheapestMovie(movies))

#am facut o sortare a filmelor dupa pret (cel mai mic la cel mai mare)
print("Filme sortate dupa pret:")
filme_sortate =sorted(movies, key =lambda movie : movie["price"])
print(filme_sortate)


#am facut o sortare a filmelor   a filmelor dupa pret (cel mai mare la cel mai mic)
filme_sortate2 = (sorted(movies, key =lambda movie: movie ["price"], reverse=True))
print(filme_sortate2)

#vom crea o functie "longestMovieByGenre" care identifica filmul cu cea mai mare durata dintr-un anumit ge
#functia primeste ca prim argument genul cautat si ca al doilea argument lista de filme

def longestMovieByGenre(genre,movies):
    filme_gen = [movie for movie in movies if genre in movie["genres"]] # filtram filmele care au genul specific
    if filme_gen:
        return max(filme_gen,key = lambda movie :movie ["runtime"])#daca exista filme pt genul respectiv
                                                                   #returnam filmul cu durata maxima
    else:
        return None # daca nu exista nici unfilm pt genul dat -> return None

print(longestMovieByGenre("Drama",movies))

