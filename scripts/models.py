from sandman.model import register, activate, Model

class Track(Model):
    __tablename__ = 'Track'

    def __str__(self):
        return self.Name

class Artist(Model):
    __tablename__ = 'Artist'
    def __str__(self):
        return self.Name

class Album(Model):
    __tablename__ = 'Album'
    def __str__(self):
        return self.Title

class Playlist(Model):
    __tablename__ = 'Playlist'
    def __str__(self):
        return self.Name

class Type(Model):
    __tablename__ = 'Genre'
    def __str__(self):
        return self.Name

class PlaylistTrack(Model):
    __tablename__ = 'PlaylistTrack'

class MediaType(Model):
    __tablename__ = 'MediaType'
    def __str__(self):
        return self.Name

register((Artist, Album, Playlist, Type, Track, MediaType, PlaylistTrack))
activate(admin=True)
