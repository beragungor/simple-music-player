import os
import json
import tkinter as tk
from tkinter import filedialog
import pygame
from PIL import Image, ImageTk
 
class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Music Player")
        self.master.geometry("400x200")

        # Load the icon
        icon_path = "./pingu.ico"
        icon_image = Image.open(icon_path)
        icon_image = ImageTk.PhotoImage(icon_image)

        # Set the window icon
        self.master.iconphoto(True, icon_image)

        self.playlist = []
        self.current_track = 0
        
        pygame.init()
        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, selectbackground="yellow", selectforeground="black", height=10, width=40)
        self.listbox.pack(pady=10)

        self.btn_add = tk.Button(self.master, text="Add Song", command=self.add_song)
        self.btn_add.pack(pady=5)

        self.btn_play = tk.Button(self.master, text="Play", command=self.play_music)
        self.btn_play.pack(pady=5)

        self.btn_stop = tk.Button(self.master, text="Stop", command=self.stop_music)
        self.btn_stop.pack(pady=5)


    def load_database():
        songs = json.load(open("data/songs.json", "r+")) ["songs"]

    def update_database(filename: str):
        data = json.load(open("data/songs.json", "r+"))
        if filename not in data["songs"]:
            data["songs"] += [filename]
        json.dump(data, open("data/songs.json", "r+"), indent=4)

    def add_song(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            filename = os.path.basename(file_path)
            self.playlist.append((filename, file_path))
            self.listbox.insert(tk.END, filename)

    def play_music(self):
        if self.playlist:
            selected_index = self.listbox.curselection()
            if selected_index:
                self.current_track = selected_index[0]
            else:
                self.current_track = 0

            pygame.mixer.music.load(self.playlist[self.current_track][1])
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    master = tk.Tk()
    music_player = MusicPlayer(master)
    master.mainloop()
