import fresh_tomatoes
import classMovie

# Creating Mobies objects
toy_story = classMovie.Movie("Toy Story", 
	"A friendship tale 'to Inifinty and Beyond'.", 
	"https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg", 
	"https://www.youtube.com/watch?v=KYz2wyBy3kc", 
	classMovie.Movie.VALID_RATINGS[0])

avatar = classMovie.Movie("Avatar", 
	"Looking for a second chance in a alien planet.", 
	"https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg", 
	"https://www.youtube.com/watch?v=5PSNL1qE6VY", 
	classMovie.Movie.VALID_RATINGS[1])

rocky = classMovie.Movie("Rocky", 
	"A man and his path into boxing and life!", 
	"https://upload.wikimedia.org/wikipedia/pt/1/18/Rocky_poster.jpg", 
	"https://www.youtube.com/watch?v=3VUblDwa648", 
	classMovie.Movie.VALID_RATINGS[2])

lords_rings = classMovie.Movie("The Lord of the Rings", 
	"One to rule them all!", 
	"https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg", 
	"https://www.youtube.com/watch?v=V75dMMIW2B4", 
	classMovie.Movie.VALID_RATINGS[2])

matrix = classMovie.Movie("Matrix", 
	"I don't like the idea that I'm not in control of my life.", 
	"https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg", 
	"https://www.youtube.com/watch?v=m8e-FF8MsqU", 
	classMovie.Movie.VALID_RATINGS[3])

saving_priv_ryan = classMovie.Movie("Saving Private Ryan", 
	"Maybe saving Private Ryan is the one decent thing we did is this war.", 
	"https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg", 
	"https://www.youtube.com/watch?v=RYID71hYHzg",
	classMovie.Movie.VALID_RATINGS[4])


# Create a list of Movies objects
movies = [toy_story, avatar, rocky, lords_rings, matrix, saving_priv_ryan]
# Use open_movies_page function to open default browser 
fresh_tomatoes.open_movies_page(movies)