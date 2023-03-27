#Made by Nils Santos

def make_album(singer, album_title, tracks = 0):
    album = {'Artist':singer,
             'Album Title': album_title,
             'Number of tracks': tracks}
    if tracks == 0:
        del album['Number of tracks']
        return album
    else:
        return album
    
print(make_album('Kendrick Lamar', 'HUMBLE'))
print(make_album('Taylor Swift', '1989', 1))
print(make_album('J.Cole', 'MIDDLE CHILD', 2))