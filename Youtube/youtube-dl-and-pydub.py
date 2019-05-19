from __future__ import unicode_literals

import os


#os.sys("""ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)""")
#os.sys("brew install python3.6")
os.system("pip3.6 install youtube-dl")
os.system("pip3.6 install pydub")
os.system("pip3.6 install ffprobe")


from pydub import AudioSegment

import youtube_dl


DIRECTORY='/Users/olivierpartensky/Videos/2019/Youtube/Downloads'
os.chdir(DIRECTORY)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }]
}


ydl_opts={}


jjd_ocean="https://www.youtube.com/watch?v=XGyrclIGB9E"
playlist='https://www.youtube.com/playlist?list=UUMOgdURr7d8pOVlc-alkfRg'

def convertAll():
    """Convert all the webm files into mp3 using pytube."""
    l=os.listdir()
    print(l)
    for i,f in enumerate(l):
        if f[-3:]=="mp4":
            song=AudioSegment.from_file(f,"mp4")
            nf=f[:-3]+"mp3"
            song.export(nf, format="mp3")


if __name__=="__main__":
    url=jjd_ocean

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


    convertAll()

    print("Download is over.")
