#Problem #1

class Animal():
    type = ""
    name = ""
    voice = ""
    weight=""

    def __init__(self, type, name, weight):
        self.type = type
        self.name = name
        self.weight = weight

    def feed(self):
        return 0
    def milk(self):
        return 0
    def shear(self):
        return 0
    def collect_eggs(self):
        return 0

animals = []

animals.append(Animal("Geese", "Gray", 5))
animals.append(Animal("Geese", "White", 6))
animals.append(Animal("Cow", "Man'ka", 78))
animals.append(Animal("Sheep", "Lamb", 50))
animals.append(Animal("Sheep", "Curly", 51))
animals.append(Animal("chicken", "Ko-Ko", 4))
animals.append(Animal("chicken", "Kukareku", 2))
animals.append(Animal("duck", "Kriakva", 3))

total_weight=0
max_weight=0
leader_animal=0
for a in animals:
    if a.weight>max_weight:
        max_weight=a.weight
        leader_animal=a.name
    total_weight = a.weight + total_weight
print(f"total weight equals: {total_weight}")
print(f"max weight animal is: {leader_animal}")


#Problem #2

class Album():
    name_of_album = ""
    group = ""
    tracks = []
    def __init__(self, name_of_album, group):
        self.name_of_album = name_of_album
        self. group = group

    def add_track(self, track):
        self.tracks.append(track)
    def get_tracks(self):
        for t in self.tracks:
            t.show()
    def get_duration(self):
         total_duration=0
         for t in self.tracks:
             total_duration = t.duration + total_duration
         return total_duration




class Track():
    name=""
    duration = 0
    def __init__(self, name, duration):
        self.duration = duration
        self.name = name
    def show(self):
        print(self.name,self.duration)


tr1 = Track("Flowers",6)
tr2 = Track("Beach",9)



album=Album("Country", "sufferings")
album.add_track(tr1)
album.add_track(tr2)

album.get_tracks()
print(album.get_duration())