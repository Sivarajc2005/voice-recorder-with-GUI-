import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter.   filedialog import askdirectory

add="  "


def file_path():
    global add
    add=askdirectory()
    print(add)

def save_file():
    global add
    try:
      time=int(sec.get())
      addr=add+"/"+"demo.wav"
      showinfo(title="start",message="rec start")
      rece=sounddevice.rec((time*44100),samplerate=44100,channels=2)
      sounddevice.wait()
      write(addr,44100,rece)
      showinfo(title="stop",message="rec stop")
    
    except:
        showwarning(title="time",Message="wrong formate time")


def main_window():
    global sec
    win=Tk()
    win.geometry("550x600")
    win.resizable(False,False)
    win.title("audio recorder")
    win.configure(bg="violet")

    img1=PhotoImage(file="sound wave.png")
    l1=Label(win,image=img1)
    l1.place(x=50,y=20,height=200,width=400)

    #entry box
    sec=Entry(win,font=(20))
    sec.place(x=150,y=300,height=50,width=200)

    l2=Label(win,text="time in sec",font=("time new roman",20),bg="yellow")
    l2.place(x=150,y=240,height=50,width=200)

    #button
    btn=Button(win,text="path",font=("time new roman",20),command=file_path)
    btn.place(x=150,y=340,height=50,width=200)

    img2=PhotoImage(file="mic.png")

    start=Button(win,image=img2,command=save_file)
    start.place(x=150,y=400,height=110,width=100)

    win.mainloop()

main_window()


'''procedure to use 
  step 1 : enter the dration you need to recode on second formate in the white box 
  step 2 : click the path button and chose the path to store your recorded audio
  step 3 : after chosing the path click the mic icon button
  step 4 :then you receive notification to start the record click start to start the record '''