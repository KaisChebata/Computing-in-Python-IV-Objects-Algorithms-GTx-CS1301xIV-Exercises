#We've given you a class called "Song" that represents
#some basic information about a song. We also wrote a 
#class called "Artist" which contains some basic 
#information about an artist.
#
#Your job is to create three instances of the song class,
#called song_1, song_2, and song_3.
#
#song_1 should have the following attributes:
#   name = "You Belong With Me"
#   album = "Fearless"
#   year = 2008
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
#song_2 should have the following attributes:
#   name = "All Too Well"
#   album = "Red"
#   year = 2012
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
#song_3 should have the following attributes:
#   name = "Up We Go"
#   album = "Midnight Machines"
#   year = 2016
#   artist.name = "artist_2"
#   artist.label = "Warner Bros. Records Inc."
#
#Notice, though, that song_1 and song_2 have the same
#artist and label. That means they should each have the
#SAME instance of artist: do not create separate instances
#of artist for each song.
#
#When your code is done running, there should exist three
#variables: song_1, song_2, and song_3, according to the
#requirements above.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
        

#Write your code here!

artist_1 = Artist('Taylor Swift', 'Big Machine Records, LLC')
artist_2 = Artist('artist_2', 'Warner Bros. Records Inc.')

song_1 = Song('You Belong With Me', 'Fearless', 2008, artist_1)
song_2 = Song('All Too Well', 'Red', 2012, artist_1)
song_3 = Song('Up We Go', 'Midnight Machines', 2016, artist_2)


#Feel free to add code to test your code below.
print('Song_1 infos:', song_1.name, song_1.album, song_1.year, 
        song_1.artist.name, song_1.artist.label, '-----------------', sep='\n')
print('Song_2 infos:', song_2.name, song_2.album, song_2.year, 
        song_2.artist.name, song_2.artist.label, '-----------------', sep='\n')
print('Song_3 infos:', song_3.name, song_3.album, song_3.year, 
        song_3.artist.name, song_3.artist.label, '-----------------', sep='\n')