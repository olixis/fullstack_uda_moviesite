import webbrowser


class Movie(object):
    """Movie Class

    Attributes:
        movie_title (str): The title of the movie.
        movie_storyline (str): The movie storyline.
        poster_image (str): The link to the poster image.
        trailer_youtube (str): The link to youtube trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the browser with the instance given trailer link.

        Returns:
            None
        """
        webbrowser.open(self.trailer_youtube_url)
