'''
Your program should have 3 classes: Artist, Album, and Track. 
Each class should contain the following information: 

Artist	
    name: string
    albums: list [Album object]
Album	
    name: string
    artist: object
    tracks: list [Track object]
Track
    number: integer
    name: string
    length: integer (seconds)
'''
# Artist class
class Artist:
    def __init__(self, name):
        self.name = name
        #initialize empty tracks list for later association.
        self.albums = []
    
# Album class
class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        #initialize empty tracks list for later association.
        self.tracks = []

# Track class
class Track:
    def __init__(self, number, name, length):
        self.number = number
        self.name = name
        self.length = length

'''
* Create an artist. Create an album. Be sure that your 
* album object is initialized with an artist object.
* Add Track object to your Album objects.
* Print every track from every album published by an artist.
* Print an artist summary that lists all of their albums, and
* the total run time of each album.  
''' 

# Create Artist objects
raja = Artist("Ilayaraja")
arr = Artist("AR Rahman")

# Create album objects
album1 = Album("soothing melodies", raja)
album2 = Album("90s hits", arr)

# Create Track objects that are in soothing melodies album.
track1 = Track(1, "Enna satham intha neram", 300)
track2 = Track(2, "Inji iduppazhagi", 289)
track3 = Track(3, "Kathalin deepam ondru", 240)

# associating track to soothing melodies album.
album1.tracks.append(track1)
album1.tracks.append(track2)
album1.tracks.append(track3)

# Create Track objects that are in 90s hits album.
track4 = Track(1, "Muqqala muqabla", 300)
track5 = Track(2, "Snehithane Snehithane", 289)
track6 = Track(3, "kaathal sadugudu gudu", 240)

# associating track to 90s hits album.
album2.tracks.append(track4)
album2.tracks.append(track5)
album2.tracks.append(track6)

#associating albums to artist
#Associating soothimg melodies album to artist raja
raja.albums.append(album1)
#Associating 90s hits album to artist arr
arr.albums.append(album2)

#Priniting a summary of Artist
# Artist details of Ilayaraja
print("-" * 50)
# Print artist name
print("Artist name is : ", raja.name)
print("Album Details " + "-" * 50)
# Retrieve from albums list and print
for album in raja.albums:
    print("Album name is : ", album.name)
    # Retrieve from tracks list and print
    for track in album.tracks:
        print("Track name is : ", track.name)
        print("Track length is : ", track.length)
print("-" * 50)

# Artist summary of AR Rahman
print("-" * 50)
# Print artist name
print("Artist name is : ", arr.name)
print("Album Details " + "-" * 50)
# Retrieve from albums list and print
for album in arr.albums:
    print("Album name is : ", album.name)
    # Retrieve from tracks list and print
    for track in album.tracks:
        print("Track name is : ", track.name)
        print("Track length is : ", track.length)
print("-" * 50)