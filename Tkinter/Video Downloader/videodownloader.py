from __future__ import unicode_literals

from tkinter import *
from tkinter import ttk, filedialog
import os
import pickle
from typing import Optional, Any



# Install non native required dependencies.
try:
    import youtube_dl
except:
    import sys
    major = str(sys.version_info.major)
    minor = str(sys.version_info.minor)
    v = major + "." + minor
    print('importing python library: youtube-dl')
    os.system("pip" + v + " install youtube-dl")
    print("installing package manager: homebrew")
    os.system(
        """/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)""""")
    print("installing audio library: ffmpeg")
    os.system("brew install ffmpeg")
    print("imports are done you are ready to go")
    import youtube_dl


def update():
    """Update non native required dependencies."""
    import sys
    major = str(sys.version_info.major)
    minor = str(sys.version_info.minor)
    v = major + "." + minor
    print('updating python library: youtube-dl')
    os.system("pip" + v + " install update youtube-dl")
    print("updating package manager: homebrew")
    print("updating audio library: ffmpeg")
    os.system("brew upgrade ffmpeg")
    print("updates are done you are ready to go")



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


class VideoDownloader(Frame):
    ydl_opts: Optional[Any]

    def __init__(self, window, width=800, height=600, **kwargs):
        super().__init__(window, width=width, height=height, **kwargs)
        self.pack(fill=BOTH)
        self.window = window
        self.window.winfo_toplevel().title(type(self).__name__)
        self.config(background="#e5e5e5")
        self.count = 0
        self.directory = ""
        self.url = ""
        self.config_filename = "config.txt"
        self.ydl_opts_filename = "youtube-dl.config"
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
        # Grid
        # self.grid(padx=20, pady=20)

        # Style
        self.style = ttk.Style()
        self.style.configure("info.TLabel", foreground="black", padding=10)
        self.style.configure("button.TButton", padding=10)
        self.style.configure("main.TLabel", foreground="red", font=('calibri', 20, 'bold', 'underline'), padding=10, margin=10)
        self.style.configure("green.TLabel", foreground="green")
        self.style.configure("grey.TLabel", foreground="grey")
        # self.style.configure("TLabel", background="#002200")

        # Main label
        self.main_label = ttk.Label(self, text="Bienvenue dans le downloader de vidéos youtube!", style="main.TLabel")
        self.main_label.pack()

        # Directory
        self.directory_label = ttk.Label(self, text="Veuillez sélectionner votre dossier de stockage.", style="info.TLabel")
        self.directory_label.pack()
        self.directory_button = ttk.Button(self, text="Choisir", command=self.getDirectory, style="button.TButton")
        self.directory_button.pack()

        # Youtube
        self.url_label = ttk.Label(self, text="Veuillez sélectionner votre lien youtube.", style="info.TLabel")
        self.url_label.pack()
        self.url_input = StringVar()
        self.url_entry = ttk.Entry(self, textvariable=self.url_input, width=30)
        self.url_entry.pack()
        self.url_button = ttk.Button(self, text="Choisir", command=self.getUrl, style="button.TButton")
        self.url_button.pack()

        # Download
        self.download_button = ttk.Button(self, text="Télécharger", command=self.download)
        self.download_button.pack()

        # Quit
        self.quit_button = ttk.Button(self, text="Quitter", command=self.quit)
        self.quit_button.pack()

        # Main label
        self.info_label = ttk.Label(self, text="Auteur: Marc Partensky\nLicense: None", style="grey.TLabel")
        self.info_label.pack()

        # Loading if possible
        try:
            self.load()
            self.show()
            print("Loaded registered config.")
        except:
            self.dump()
            print("Created new config file")

    def getUrl(self):
        self.url = self.url_input.get()
        self.showUrl()
        self.dump()

    def showUrl(self):
        self.url_button.config(text="Changer")
        text = "Votre url est: {}".format(self.url)
        self.url_label.config(text=text)

    def getDirectory(self):
        self.directory = filedialog.askdirectory()
        self.showDirectory()
        self.dump()

    def showDirectory(self):
        text = "Votre dossier est: {}".format(self.directory)
        self.directory_button.config(text="Changer")
        self.directory_label.config(text=text)

    def show(self):
        self.showUrl()
        self.showDirectory()

    def dump(self):
        # We store seriazable data
        with open(self.config_filename, "w") as file:
            data = ["count: " + str(self.count),
                    "url: " + self.url,
                    "directory: " + self.directory]
            file.write("\n".join(data))
        # We store unserizable data
        data = pickle.dumps(self.ydl_opts)
        pickle.dump(data, open(self.ydl_opts_filename, "wb"))

    def load(self):
        # We load seriazable data
        with open(self.config_filename, "r") as file:
            data = file.read()
            lines = data.split("\n")
            self.count = int(lines[0].split(": ")[1]) + 1
            self.url = lines[1].split(": ")[1]
            self.directory = lines[2].split(": ")[1]
        # We load unserizable data
        data = pickle.load(open(self.ydl_opts_filename, "rb"))
        self.ydl_opts = pickle.loads(data)

    def download(self):
        program_directory = os.getcwd()
        os.chdir(self.directory)
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([self.url])
        os.chdir(program_directory)
        self.main_label.config(text="Votre téléchargement est terminé.")

    def center(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


if __name__ == "__main__":
    window = Tk()
    root = VideoDownloader(window)
    root.center()
    root.mainloop()
