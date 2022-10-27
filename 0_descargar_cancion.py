from pytube import YouTube
from pytube import Playlist

def descargarCancion (url:str):
    youtube= YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()

def descargarLista (url:str):
    playlist= Playlist(url)
    for cancion in playlist.videos:
        print("Descargando ", cancion.title)
        cancion.streams.get_audio_only().download("canciones/")
        print("***********\n")

url= "https://www.youtube.com/watch?v=NN1f066QTMU&list=PLSFitF4B6yNS82pcRx5XvD1PB6m8lIs5J"

#descargarCancion ("https://www.youtube.com/watch?v=z5aNHbvMMZU")

descargarLista(url)