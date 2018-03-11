from movieGenre import *

print(Genre)

movie = Movie()
thor = Movie()
thor.title = "Thor Ragnarok"

genre = Genre()
action = Genre()
action.name = "Action"

print(action.name)

genre.addMovie(movie)
 #print genre.movies
#print (genre['name'])

print (genre.movies)

print (movie.setGenre(genre))

print(thor.setGenre(action))
print(action.movies[0].title)

darkWorld = Movie()
darkWorld.title = "Dark World"
print(thor.addRelatedMovie(darkWorld))
print(thor.related[0].title)