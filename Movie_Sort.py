class Movie:
    def __init__(self, name, year, director, rating, genre, cast):
        self.name = name
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast

    def __str__(self):
        return f"Name: {self.name}\nYear: {self.year}\nDirector: {self.director}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {', '.join(self.cast)}"

    def sort_Alpha(self, movie_list):
        Aplha_sort = []
        while movie_list:
            low_movie = movie_list[0]
            for movie in movie_list:
                if movie.name < low_movie.name:
                    low_movie = movie
            Aplha_sort.append(low_movie)
            movie_list.remove(low_movie)
        return Aplha_sort

    def sort_chrono(self, movie_list):
        chrono_sort = []
        while movie_list:
            low_movie = movie_list[0]
            for movie in movie_list:
                if movie.year < low_movie.year:
                    low_movie = movie
            chrono_sort.append(low_movie)
            movie_list.remove(low_movie)
        return chrono_sort

    def genre_sort(self, movie_list, genre):
        newmovie_list = []
        for movie in movie_list:
            if movie.genre.lower() == genre.lower():
                newmovie_list.append(movie)
        return newmovie_list

    def director_sort(self, movie_list, director):
        newmovie_list = []
        for movie in movie_list:
            if movie.director.lower() == director.lower():
                newmovie_list.append(movie)
        return newmovie_list

    def cast_sort(self, movie_list, actor):
        newmovie_list = []
        for movie in movie_list:
            if actor.lower() in [cast_member.lower() for cast_member in movie.cast]:
                newmovie_list.append(movie)
        return newmovie_list

    def movie_menu(self):
        print("\n***** Movie Sorting Menu *****")
        print("1. View Movies Sorted Alphabetically")
        print("2. View Movies Sorted Chronologically")
        print("3. Search Movies by Genre")
        print("4. Search Movies by Director")
        print("5. Search Movies by Cast")
        print("6. Exit")
        print("*****************************")

    def runmovie(self, movie_list):
        while True:
            self.movie_menu()
            ch = int(input("Please Choose 1-6: "))

            if ch == 1:
                print("\nMovies sorted alphabetically:")
                sorted_movies = self.sort_Alpha(movie_list.copy())
                for movie in sorted_movies:
                    print(movie)

            elif ch == 2:
                print("\nMovies sorted chronologically:")
                sorted_movies = self.sort_chrono(movie_list.copy())
                for movie in sorted_movies:
                    print(movie)

            elif ch == 3:
                genre = input("Enter the genre to search for: ")
                print(f"\nMovies in the '{genre}' genre:")
                found_movies = self.genre_sort(movie_list, genre)
                for movie in found_movies:
                    print(movie)

            elif ch == 4:
                director = input("Enter the director's name to search for: ")
                print(f"\nMovies directed by '{director}':")
                found_movies = self.director_sort(movie_list, director)
                for movie in found_movies:
                    print(movie)

            elif ch == 5:
                actor = input("Enter the actor's name to search for: ")
                print(f"\nMovies with '{actor}' in the cast:")
                found_movies = self.cast_sort(movie_list, actor)
                for movie in found_movies:
                    print(movie)

            elif ch == 6:
                print("Leaving Program")
                break
            else:
                print("Please try again.")

movie_list = [
    Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"]),
    Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]),
    Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"]),
    Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]),
    Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]),
    Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"]),
    Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),
    Movie("Schindler's List", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"]),
    Movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]),
    Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta", "Joe Pesci"]),
    Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"]),
    Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]),
    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", ["Elijah Wood", "Ian McKellen", "Orlando Bloom"]),
    Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]),
    Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"]),
    Movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", ["Tom Hanks", "Matt Damon", "Tom Sizemore"]),
    Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"]),
    Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"]),
    Movie("The Lion King", 1994, "Roger Allers, Rob Minkoff", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"]),
    Movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", ["Jim Carrey", "Kate Winslet", "Kirsten Dunst"]),
]

startmovie = Movie("", 0, "", "", "", [])

startmovie.runmovie(movie_list)