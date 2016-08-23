import webbrowser

class Movie():
    """This is the documentation"""
# each class needs an __init__ function with the keyword self as the first arg
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
# these are  instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# this is an instance method       
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
            
