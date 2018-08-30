import webbrowser

class Movie():
	""" Define a movie object using parameters of a Real Movie from Hollywood."""

	VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"] # Constant for Movie Ratings

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating = rating

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)