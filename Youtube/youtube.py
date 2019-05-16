from pytube import YouTube,Playlist

import moviepy.editor as mp

import pytube
import os
import sys
import time


#print(pytube.__version__)

DIRECTORY='/Users/olivierpartensky/Videos/2019/Youtube/Downloads'



#print(os.getcwd())



class MyPlaylist(Playlist):
    def __init__(self,*args,n=None,path=None):
        self.n=n
        self.path=path
        os.chdir(path)
        super().__init__(*args)
        print("The playlist is set to be downloaded in the following path:"+str(self.path)+".")


    def getUrls(self):
        """Return the urls of the videos playlist."""
        base_url = 'https://www.youtube.com'
        link_list = self.parse_links()
        if not self.n: self.n=len(link_list)
        urls=[]
        for i in range(self.n):
            complete_url = base_url + link_list[i]
            urls.append(complete_url)
        return urls

    def doAll(self,*args,**kwargs):
        """Contrary to __call__ this function download each video one by one."""
        urls=self.getUrls()
        for i in range(self.n):
            print("Downloading:",i+1,"/",self.n)
            print(urls[i])
            try:
                video=YouTube(urls[i])
                video=video.streams.filter(*args,**kwargs).first()
                video.download()
            except:
                print("Error")


    def populate(self):
        """Populate the videos."""
        urls=self.getUrls()
        self.videos=[]
        for i in range(self.n):
            print("Populating:",i+1,"/",self.n)
            video=YouTube(urls[i])
            self.videos.append(video)

    def filter(self,*args,**kwargs):
        """Filter the musics using parameters such as only_audio which is None by default."""
        for i in range(self.n):
            print("Filtering:",i+1,"/",self.n)
            self.videos[i]=self.videos[i].streams.filter(*args,**kwargs).first()

    def download(self,path=None):
        """Download the videos of the playlist."""
        if not path: path=self.path
        for i in range(self.n):
            print("Downloading:",i+1,"/",self.n)
            self.videos[i].download(path)

    def video_to_mp3(self,file_name):
        """ Transforms video file into a MP3 file """
        try:
            file, extension = os.path.splitext(file_name)
            # Convert video into .wav file
            os.system('ffmpeg -i {file}{ext} {file}.wav'.format(file=file, ext=extension))
            # Convert .wav into final .mp3 file
            os.system('lame {file}.wav {file}.mp3'.format(file=file))
            os.remove('{}.wav'.format(file))  # Deletes the .wav file
            print('"{}" successfully converted into MP3!'.format(file_name))
        except OSError as err:
            print(err.reason)
            exit(1)


    def convertToMP3(self):
        """Convert the mp4 files in mp3."""
        videos=os.listdir()
        print(videos)
        for i in range(len(videos)):
            print(videos[i][-4:])
            if videos[i][-4:]=='.mp4':
                name=videos[i][:-4]
                self.video_to_mp3(videos[i])
                #print(name+".mp3")
                #clip=mp.VideoFileClip(videos[i]).subclip(0,20)
                #clip.audio.write_audiofile(name+".mp3")




    def __call__(self,only_audio=None,):
        """Populate the videos, filter them using args and kwargs and download them, all in once."""
        print("This download takes 4 steps")
        print("Step1: Populating")
        self.populate()
        print("\nStep2: Filtering")
        self.filter(*args,**kwargs)
        print("\nStep3: Downloading")
        self.download()
        print("\nStep4: Converting to mp3")
        #self.convertToMP3()
        print("The step 4 has been skipped for now.")
        print("\nThe download is over enjoy!")




if __name__=="__main__":
    url='https://www.youtube.com/playlist?list=UUMOgdURr7d8pOVlc-alkfRg'
    p=MyPlaylist(url,path=DIRECTORY)
    p.doAll(only_audio=True)
    #p.convertToMP3()






#----------------#
#Useless tests...#
#----------------#

#yt = YouTube(vd_url)
#pl=Playlist(pl_url)
#pl.populate_video_urls()
#urls=pl.videos_urls
#for url in urls[:5]:
#    vd=Youtube(url)
#    vd=vd.streams.filter(only_audio=True).first()
#    vd.download()

#print(yt.video_id) #Actually works

#print("The program is downloading %s videos."%len(yt.videos_urls))
#yt=yt.streams.filter(only_audio=True).first()
#yt=yt.streams.filter(only_audio=True).all()


#print(v)

#print(self.videos_urls)

#yt.download_all()
#yt=

#print(yt.__dict__)

#Affiche un certain bordel
#for key,value in zip(yt.__dict__.keys(),yt.__dict__.values()):
#    print(key,":",value)


#videos = yt.get_videos()
#print(yt.filename)

#yt = yt.get('mp4', '720')
#yt=yt.streams.first()
#yt.download()
#yt.download('../2019/Youtube/Downloads')

#'../2019/Youtube/Downloads'
