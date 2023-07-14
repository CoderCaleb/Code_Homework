class MovieReview:
    moviereviews = []

    def __init__(self, movie, story_rating, actor_rating, music_rating):
        self.movie = movie
        self.story_rating = story_rating
        self.actor_rating = actor_rating
        self.music_rating = music_rating
        self.avg = int((self.story_rating + self.actor_rating + self.music_rating) / 3)
        self.myrating = {
            'Movie Name': self.movie,
            'Story Rating': self.story_rating,
            'Actor Rating': self.actor_rating,
            'Music Rating': self.music_rating
        }

    def add_movie_ratings(self, movie_list):
        movie_list.append(self.myrating)

    def get_star(self, movie_list):
        for movie in movie_list:
            avg_rating = movie['Story Rating'] + movie['Actor Rating'] + movie['Music Rating']
            avg_rating = int(avg_rating / 3)
            stars = '*' * avg_rating
            print(stars + ' ' + movie['Movie Name'])


review1 = MovieReview('Movie A', 4, 5, 3)

review1.add_movie_ratings(MovieReview.moviereviews)

review1.get_star(MovieReview.moviereviews)
