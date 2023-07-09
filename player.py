from tkinter import *
from pygame import mixer
import tkinter.font as font
from tkinter import filedialog

#creating main window 
root=Tk()
root.title('My Music Player')
#initializing mixer 
mixer.init()

#Playlist of songs
Playlist=Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial',15), height=12, width=47,selectbackground="gray",selectforeground="black")
Playlist.grid(columnspan=9)

    
def Play():
    song=Playlist.get(ACTIVE)
    song=f'C:/Users/Anvitha/MY_music_player/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()
    
#add many songs to the playlist of python mp3 player
def addsongs():
    #to open a file  
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    
    for s in temp_song:
        s=s.replace("C:/Users/Anvitha/MY_music_player/Music/", "")
        Playlist.insert(END,s)
     
def deletesong():
    curr_song=Playlist.curselection()
    Playlist.delete(curr_song[0])
    

#Pause 
def Pause():
    mixer.music.pause()

#Stop
def Stop():
    mixer.music.stop()
    Playlist.selection_clear(ACTIVE)

#Resume
def Resume():
    mixer.music.unpause()

#Go to previous song
def Previous():
    #to get the selected song index
    previous_one=Playlist.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=Playlist.get(previous_one)
    temp2=f'C:/Users/Anvitha/MY_music_player/Music/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    Playlist.selection_clear(0,END)
    #activate new song
    Playlist.activate(previous_one)
    #set the next song
    Playlist.selection_set(previous_one)

#Go to next song
def Next():
    #to get the selected song index
    next_one=Playlist.curselection()
    #to get the next song index
    next_one=next_one[0]+1
    #to get the next song 
    temp=Playlist.get(next_one)
    temp=f'C:/Users/Anvitha/MY_music_player/Music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    Playlist.selection_clear(0,END)
    #activate newsong
    Playlist.activate(next_one)
     #set the next song
    Playlist.selection_set(next_one)
    
#font for all the buttons
defined_font = font.Font(family='Helvetica')

#play button
play_button=Button(root, text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#stop button
stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

#resume button
Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

#previous button
previous_button=Button(root,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

#nextbutton
next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)


mainloop()