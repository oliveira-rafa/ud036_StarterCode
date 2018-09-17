import webbrowser

class Movie():

	""" Define a movie object using parameters of a Movie from Hollywood.

		Title,
		Storyline - use to be a quote or a phrase about the movie,
		Poster of the Movie,
		Trailer of the Movie,
		The MPAA rating to the movie. """

	VALID_RATINGS = ["g", "pg", "pg-13", "r", "nc-17"]  # Constant for MPAA Movie Ratings

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating):  # Create a movie object
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating = rating

	def show_trailer(self):  # Open a movie trailer from Youtube on a new browser tab
		webbrowser.open(self.trailer_youtube_url)
		