from __future__ import unicode_literals
import youtube_dl

import os

DIRECTORY='/Users/olivierpartensky/Videos/2019/Youtube/Downloads'
os.chdir(DIRECTORY)

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
     'ignoreerrors':True,
}


if __name__=="__main__":
    url='https://www.youtube.com/playlist?list=UUMOgdURr7d8pOVlc-alkfRg'

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Done")
