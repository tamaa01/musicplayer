import tkinter
import pygame
from tkinter import *
import os
from tkinter import filedialog


        

class main:
    
    def __init__(self):
        pygame.mixer.init()
        self.x = 0
        self.y = 0
        self.paused = False
        self.root = tkinter.Tk()
        self.root.title("Music player")
        self.musics = {
            'a' : 'a'
        }
        self.musics1 = []
        self.root.config(background="#ffffff")
        self.music_filename = ""
        self.lists = Listbox(self.root , width=50)
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
        self.button5 = tkinter.Button(self.root , text="Delete music" , height=2 , width=8 , command=self.delete_music)
        self.button6 = tkinter.Button(self.root , text="Play all" , height=2 , width=8 , command=self.play_all)
        self.labelstatus = tkinter.Label(self.root , text="Status : stopped" , height=2 , background="#ffffff")
        self.volume = tkinter.Label(self.root , text="Volume : " , height=2 , background="#d4f6fc")
        #self.labeltitle.grid(row=1 , column=1 , pady=50 , padx=10)
        self.labeltitle.grid(row=1 , column=1)
        x.grid(row=2 , column=1 , pady=20)
        self.button1.grid(row=3  , column=1 , sticky=E)
        self.button2.grid(row=3 , column=2 , sticky=E)
        self.button3.grid(row=3 , column=3)
        self.button4.grid(row=3 , column=4)
        self.button5.grid(row=3 , column=5)
        self.button6.grid(row=3 , column=6)
        self.scale.set(60)
        self.labelstatus.grid(row=4 , column=1 , sticky=W)
        
        self.volume.grid(row=5 , column=1 , sticky=W)
        self.scale.grid(row=6 , column=1 , sticky=EW)
        self.change_volume.grid(row=7 , column=1)
        self.lists.grid(row=8 , column=1)
        self.root.mainloop()
        
    
        
    def add_music(self):
        filename = filedialog.askopenfilename()
        print(filename)
        self.x = self.x + 1
        self.music_filename = str(filename)
        self.musics[os.path.basename(str(self.music_filename))] = self.music_filename
        self.musics1.append(str(self.music_filename))
        #self.labeltitle.config(text=os.path.basename(str(self.music_filename)))
        self.lists.insert(self.x , os.path.basename(str(self.music_filename)))
        self.root.title(os.path.basename(str(self.music_filename)))
        
        
    def play_music(self):
        if self.paused == False:
            song = str(self.lists.get(self.lists.curselection()))

            pygame.mixer.music.load(self.musics[song])
            print(self.scale.get())
            self.labeltitle.config(text=song)
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

    def delete_music(self):
        selection = self.lists.curselection()
        print(self.lists.get(selection))
        self.musics1.remove(self.musics[str(self.lists.get(selection))])
        del self.musics[self.lists.get(self.lists.curselection())]

        self.lists.delete(selection[0])

    def play_all(self):
        self.labelstatus.config(text="Playing")
        self.root.title(os.path.basename(self.musics1[self.y]))
        self.labeltitle.config(text=os.path.basename(self.musics1[self.y]))
        pygame.mixer.music.load(self.musics1[self.y])
        pygame.mixer.music.play(0)
        self.que()

    def que(self):
        
        pos = pygame.mixer.music.get_pos()
        if int(pos) == -1:
            self.y += 1
            self.root.title(os.path.basename(self.musics1[self.y]))
            self.labeltitle.config(text=os.path.basename(self.musics1[self.y]))
            pygame.mixer.music.load(self.musics1[self.y])
            pygame.mixer.music.play(0)
            if self.y > len(self.musics1)-1:
                self.labelstatus.config(text="Stopped")
                self.root.cancel_after(self.que)
        self.root.after(1, self.que)


        
main()