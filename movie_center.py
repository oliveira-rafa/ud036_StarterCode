import fresh_tomatoes
import classMovie

# Creating Mobies objects
toy_story = classMovie.Movie("Toy Story", 
	"A story of a boy and his toys that come to life.", 
	"https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg", 
	"https://www.youtube.com/watch?v=KYz2wyBy3kc", 
	classMovie.Movie.VALID_RATINGS[0])

avatar = classMovie.Movie("Avatar", 
	"A marine on a alien planet.", 
	"https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg", 
	"https://www.youtube.com/watch?v=5PSNL1qE6VY", 
	classMovie.Movie.VALID_RATINGS[2])

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

saving_priv_ryan = classMovie.Movie("Saving Private Ryan", 
	"They went to save a private but instead they saved themselves from who they where before war.", 
	"https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg", 
	"https://www.youtube.com/watch?v=RYID71hYHzg",
	classMovie.Movie.VALID_RATINGS[3])

matrix = classMovie.Movie("Matrix", 
	"The Chosen One to free them all.", 
	"https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg", 
	"https://www.youtube.com/watch?v=m8e-FF8MsqU", 
	classMovie.Movie.VALID_RATINGS[2])

# Create a list of Movies objects
movies = [toy_story, avatar, rocky, lords_rings, saving_priv_ryan, matrix]
# Use open_movies_page function to open default browser 
fresh_tomatoes.open_movies_page(movies)