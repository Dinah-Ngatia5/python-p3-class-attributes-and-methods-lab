class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
        Song.add_to_genre_count()

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
        Song.add_to_artist_count()

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {genre: 0 for genre in Song.genres}
        for song in Song.genres:
            cls.genre_count[song] += 1

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {artist: 0 for artist in Song.artists}
        for artist in Song.artists:
            cls.artist_count[artist] += 1
