import tkinter
import pygame
from tkinter import *
import os
from tkinter import filedialog


        

class main:
    
    def __init__(self):
        pygame.mixer.init()
        self.paused = False
        self.root = tkinter.Tk()
        self.root.title("Music player")
        self.root.config(background="#ffffff")
        self.music_filename = ""
        panel1 = PanedWindow(background="#8d96f0" , height=90 , width=100, relief='ridge' , borderwidth=2)
        self.labeltitle = tkinter.Label(self.root , text="No music" , font=('calibri' , 15) , background="#ffffff")
        panel1.add(self.labeltitle , stretch="always")
        x = Label(self.root , text="" , background="#ffffff")
        self.var = DoubleVar()
        self.scale = Scale(self.root , variable=self.var , orient=HORIZONTAL, from_=0 , to=1 , resolution=0.01 , background="#d4f6fc")
        self.change_volume = Button(self.root , text="Change volume",command=self.ch_volume , background="#ffffff")
        self.button1 = tkinter.Button(self.root , text="Open file" , height=2 , width=8 , command=self.add_music)
        self.button2 = tkinter.Button(self.root , text="Play" , height=2 , width=8 , command=self.play_music)
        self.button3 = tkinter.Button(self.root , text="Pause" , height=2 , width=8 , command=self.pause_music)
        self.button4 = tkinter.Button(self.root , text="Stop" , height=2 , width=8 , command=self.stop_music)
        self.labelstatus = tkinter.Label(self.root , text="Status : stopped" , height=2 , background="#ffffff")
        self.volume = tkinter.Label(self.root , text="Volume : " , height=2 , background="#d4f6fc")
        #self.labeltitle.grid(row=1 , column=1 , pady=50 , padx=10)
        self.labeltitle.grid(row=1 , column=1)
        x.grid(row=2 , column=1 , pady=20)
        self.button1.grid(row=3  , column=1 , sticky=E)
        self.button2.grid(row=3 , column=2 , sticky=E)
        self.button3.grid(row=3 , column=3)
        self.button4.grid(row=3 , column=4)
        self.scale.set(60)
        self.labelstatus.grid(row=4 , column=1 , sticky=W)
        
        self.volume.grid(row=5 , column=1 , sticky=W)
        self.scale.grid(row=6 , column=1 , sticky=EW)
        self.change_volume.grid(row=7 , column=1)
        self.root.mainloop()
        
    
        
    def add_music(self):
        filename = filedialog.askopenfile()
        print(filename.name)
        self.music_filename = str(filename.name)
        self.labeltitle.config(text=os.path.basename(str(self.music_filename)))
        self.root.title(os.path.basename(str(self.music_filename)))
        
        
    def play_music(self):
        if self.paused == False:
            pygame.mixer.music.load(self.music_filename)
            print(self.scale.get())
            self.labelstatus.config(text="Playing")
            pygame.mixer.music.set_volume(self.scale.get())
            pygame.mixer.music.play(-1)
        else:
            self.labelstatus.config(text="Playing")
            pygame.mixer.music.unpause()
            self.paused = False
        
        
    def pause_music(self):
        self.labelstatus.config(text="Paused")
        pygame.mixer.music.pause()
        self.paused = True
        
    def stop_music(self):
        self.labelstatus.config(text="Stopped")
        pygame.mixer.music.stop()
        self.paused=False
       
    def ch_volume(self):
        pygame.mixer.music.set_volume(self.scale.get())
main()