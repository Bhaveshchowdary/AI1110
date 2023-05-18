from tkinter import *
from tkinter import font
from pygame import mixer
import prog
import time

mixer.init()
pauseit=0
print(prog.finalarr)

def playstatus():
    global pauseit
    if not mixer.music.get_busy() and not pauseit :
        playall()
    else:
        root.after(100,playstatus)

def play(song):
    data = "./mp3/" + str(song) + ".mp3"
    print(data)
    mixer.music.load(data)
    songinfo.config(text = data)
    mixer.music.play()
    global pauseit
    pauseit = 0
    playstatus()
    
def playall():
    play(prog.finalarr[prog.songindex])
    prog.songindex+=1
    if prog.songindex == 20:
        prog.songindex = 0
        
def pausesong():
    global pauseit
    mixer.music.pause()
    pauseit = 1
    
def resumesong():
    mixer.music.unpause()
    global pauseit
    pauseit = 0
    
def nextsong():
    mixer.music.stop()
    play(prog.finalarr[prog.songindex])
    prog.songindex+=1
    if prog.songindex == 20:
        prog.songindex = 0

root = Tk()
root.geometry('250x300')
root.title('My music player')
root.resizable(0,0)

start = Button(root,text = "play",command = playall)
start.pack(pady = 10)
pause = Button(root,text = "pause",command = pausesong)
pause.pack(pady = 10)
resume = Button(root,text = "resume",command = resumesong)
resume.pack(pady = 10)
next = Button(root,text = "next",command = nextsong)
next.pack(pady = 10)

songinfo = Label(root,text = " ",font=font.Font(size=20))
songinfo.pack()
    
root.update()
root.mainloop()


