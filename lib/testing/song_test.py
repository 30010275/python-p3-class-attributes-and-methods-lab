class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
halo = Song("Halo", "Beyonce", "Pop")
imagine = Song("Imagine", "John Lennon", "Rock")

print(Song.count)  # Output: 3
print(Song.artists)  # Output: ['Jay-Z', 'Beyonce', 'John Lennon']
print(Song.genres)  # Output: ['Rap', 'Pop', 'Rock']
print(Song.genre_count)  # Output: {'Rap': 1, 'Pop': 1, 'Rock': 1}
print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Beyonce': 1, 'John Lennon': 1}
# test_song.py
import unittest
from song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        Song.count = 0
        Song.artists = []
        Song.genres = []
        Song.genre_count = {}
        Song.artist_count = {}

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Halo", "Beyonce", "Pop")
        song3 = Song("Imagine", "John Lennon", "Rock")
        self.assertEqual(Song.count, 3)

    def test_unique_artists(self):
        '''checks the unique artists list.'''
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Halo", "Beyonce", "Pop")
        song3 = Song("Imagine", "John Lennon", "Rock")
        self.assertEqual(Song.artists, ["Jay-Z", "Beyonce", "John Lennon"])

    def test_unique_genres(self):
        '''checks the unique genres list.'''
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Halo", "Beyonce", "Pop")
        song3 = Song("Imagine", "John Lennon", "Rock")
        self.assertEqual(Song.genres, ["Rap", "Pop", "Rock"])

    def test_genre_count(self):
        '''checks the genre count dictionary.'''
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Halo", "Beyonce", "Pop")
        song3 = Song("Imagine", "John Lennon", "Rock")
        song4 = Song("Formation", "Beyonce", "Pop")
        self.assertEqual(Song.genre_count, {"Rap": 1, "Pop": 2, "Rock": 1})

    def test_artist_count(self):
        '''checks the artist count dictionary.'''
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Halo", "Beyonce", "Pop")
        song3 = Song("Imagine", "John Lennon", "Rock")
        song4 = Song("Formation", "Beyonce", "Pop")
        self.assertEqual(Song.artist_count, {"Jay-Z": 1, "Beyonce": 2, "John Lennon": 1})

if __name__ == '__main__':
    unittest.main()
