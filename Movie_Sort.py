

class Movie:
    def __init__(self, name, year, director, rating, genrea, cast):
        self.name = name
        self.year = year
        self.director = director
        self.rating = rating
        self.genrea = genrea
        self.cast = cast

    def movie_list():
        print("Test")
        

movie1 = Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"])

listss = []
for i in range(20):
    name = input('Name')
    year = int(input('year'))
    director = input('director')
    rate = input('rate')
    genra = input('genra')
    actors = input('actors')
    listss.append(name)
    listss.append(year)
    listss.append(director)
    listss.append(rate)
    listss.append(genra)
    listss.append(actors)
    print(listss)
    listss = []
movie1 = Movie('The Shawshank Redemption', 1994, 'Frank Darabont', 'R', 'Drama', ["Tim Robbins", "Morgan Freeman"])