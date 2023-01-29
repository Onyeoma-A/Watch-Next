# import spacy and language model
import spacy

nlp = spacy.load('en_core_web_md')

list_objects = []  # declare list objects for comparing the movies

# open text file to read various movie descriptions
with open('movies.txt', 'r+') as f:
	movies = f.readlines()
for line in movies:
	each_movie = line.split(":")
	compare_movies = nlp(each_movie[1])
	list_objects.append(compare_movies)

# description for planet hulk movie
planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too"
			   "dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to "
			   "planet where the Hulk can live in peace. Unfortunately, Hulk land on the"
			   " planet Sakaar where he is sold into slavery and trained as a gladiator."""

compare_planet_hulk = nlp(planet_hulk)
similarity_rate = 0   # declared a variable to keep track of the closest movie
closet_match = ""   # declared empty string

# for loop that takes the description as a parameter and return the title of the most similar movie
for token in list_objects:
	if token.similarity(compare_planet_hulk) > similarity_rate:
		similarity_rate = token.similarity(compare_planet_hulk)
		closet_match = token
movie_number = ""
for line in movies:
	each_movie = line.split(":")

	if each_movie[1] == str(closet_match):
		movie_number = each_movie[0]

# prints out the movie with the closet match and it's similarity rate
print(f" The movie with the closet match is:\n {movie_number}: {closet_match}")
print(f"The similarity rate is {similarity_rate}")
