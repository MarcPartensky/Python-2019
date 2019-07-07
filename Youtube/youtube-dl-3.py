from __future__ import unicode_literals
import youtube_dl
from pydub import AudioSegment
from pydub.playback import play

import os
import subprocess

"""I tried all the codecs on my machine but none is able to convert ogg nor webm into mp3 without loss of audio quality."""

#import audiotools

#os.system("""/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)""""")
#os.system("brew install ffmpeg")
#os.system("pip3.6 install youtube-dl")


#Choose the youtube-dl downloading options
#https://github.com/ytdl-org/youtube-dl for more informations
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        #'preferredcodec': 'mp3',
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

def clean2():
    """Convert all the files into mp3."""
    l=os.listdir()
    for i,f in enumerate(l):
        #nf=f[:-16]+".mp3"
        nf=f[:-4]+".mp4"
        print(nf)
        convert_video(f,nf)


def clean3():
    """Convert all the files into mp3."""
    l=os.listdir()
    for i,f in enumerate(l):
        #nf=f[:-16]+".mp3"
        nf=f[:-5]+".mp3"
        print(f,nf)
        convert_music_absoletely(f,nf)

def convert_video(video_input, video_output):
    #"-b:v","1M" unknown argument
    #cmds = ['ffmpeg', '-i', video_input,"-b:a","192", video_output]
    cmds = ['ffmpeg', '-i', video_input, video_output]
    #avconv -i test.webm test.mp3
    #ffmpeg -i input.webm -acodec libmp3lame -aq 4 output.mp3
    #cmds ['ffmpeg','-i',video_input,'-acodec','libmp3lame','-aq','4',video_output]
    #os.system("ffmpeg -i "+video_input+" -acodec libmp3lame -aq 4 "+video_output)
    subprocess.Popen(cmds)

def convert_music_absoletely(input,output):
    """Try to convert the input into the output format using all the codes available."""
    sound = AudioSegment.from_file(input)
    codecs=getCodecs()
    for codec in codecs:
        try:
            sound.export(output,codec=codec)#, codec="libmp3lame")
            print("Codec: "+codec+" worked.")
            break
        except:
            print("Codec: "+codec+" failed.")

def convert_music(input,output):
    sound = AudioSegment.from_ogg(input)
    #play(sound)
    sound.export(output,format="mp3")#,codec="avui")#, codec="libmp3lame")

def convert_using_audiotools(input,output):
    pass
#def convert_to_audio(video_input,video_output)


def clear():
    """Delete all the files in the actual directory."""
    l=os.listdir()
    for i,f in enumerate(l):
        os.remove(f)



def download(url,options={}):
    """Download all the musics using a youtube playlist url."""
    print("clearing")
    clear()
    print("downloading")
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
    print("cleaning")
    clean3()
    print("Download is over.")

def showFormats(url):
    """Show the different formats."""
    cmd=["youtube-dl","-F",url]
    output=subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
    output=str(output)
    l=output.split("\\n")
    for e in l:
        print(e)

def showCodecs():
    """Show the different formats."""
    cmd=["ffmpeg","-codecs"]
    output=subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
    output=str(output)
    l=output.split("\\n")
    for e in l[10:]:
        print(e[8:].split(" ")[0])

def getCodecs():
    """Show the different formats."""
    cmd=["ffmpeg","-codecs"]
    output=subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
    output=str(output)
    l=output.split("\\n")
    nl=[]
    for e in l[10:]:
        nl.append(e[8:].split(" ")[0])
    return nl



if __name__=="__main__":
    #Choose your directory
    DIRECTORY='/Users/olivierpartensky/Videos/2019/Youtube/JJD'
    os.chdir(DIRECTORY)
    print(DIRECTORY)

    #Choose your musics
    jjd_ocean="https://www.youtube.com/watch?v=XGyrclIGB9E"
    url=jjd_ocean
    #playlist='https://www.youtube.com/playlist?list=UUMOgdURr7d8pOVlc-alkfRg'
    #url="https://www.youtube.com/playlist?list=UUMOgdURr7d8pOVlc-alkfRg"
    #url="https://www.youtube.com/playlist?list=UU9IdQzchnAAwsjQb6DCugPw"

    #Download them
    #showFormats(url)
    showCodecs()
    download(url,ydl_opts)

    #clean()
