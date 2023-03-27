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
    
singer = ""
album_title = ""

while singer != 'quit' or album_title != 'quit':
    
    singer = str(input('Enter artist: '))
    album_title = str(input('Enter album title: '))
   
    if singer == 'quit':
        break
    elif album_title == 'quit':
        break
   
    print(make_album(singer, album_title))

    