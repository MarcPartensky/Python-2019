from __future__ import unicode_literals
import youtube_dl

import os

os.system("""/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)""""")
os.system("brew install ffmpeg")
os.system("pip3.6 install youtube-dl")


#Choose the youtube-dl downloading options
#https://github.com/ytdl-org/youtube-dl for more informations
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': False,
    'ignoreerrors':True
}

#Main functions used
def clean():
    """Delete all the webm files and rename the mp3 files with the original youtube names."""
    l=os.listdir()
    for i,f in enumerate(l):
        if f[-4:]=="webm":
            os.remove(f)
        if f[-3:]=="mp3":
            nf=f[:-16]+".mp3"
            os.rename(f,nf)

def download(url,options):
    """Download all the musics using a youtube playlist url."""
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
    clean()
    print("Download is over.")


if __name__=="__main__":
    #Choose your directory
    DIRECTORY='/Users/olivierpartensky/Videos/2019/Youtube/Downloads'
    os.chdir(DIRECTORY)
    print(DIRECTORY)

    #Choose your musics
    #jjd_ocean="https://www.youtube.com/watch?v=XGyrclIGB9E"
    #playlist='https://www.youtube.com/playlist?list=UUMOgdURr7d8pOVlc-alkfRg'
    url="https://www.youtube.com/playlist?list=UUMOgdURr7d8pOVlc-alkfRg"

    #Download them
    download(url,ydl_opts)
    #clean()
