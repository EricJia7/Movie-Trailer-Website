import webbrowser


class Movie(object):

    def __init__(self, mv_title, mv_storyline, mv_poster_image, mv_trailer):
        # Create Movie object structure
        self.title = mv_title
        self.storyline = mv_storyline
        self.poster_image_url = mv_poster_image
        self.trailer_youtube_url = mv_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
