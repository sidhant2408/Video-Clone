from vidstream import *
import threading as thd
import socket as sk
import tkinter as tk

local_ip_add= sk.gethostbyname(sk.gethostname())

server=StreamingServer(local_ip_add,7000)
receiver=AudioReceiver(local_ip_add,6000)

def start_meeting():
    t1=thd.Thread(target=server.start_server)
    t2=thd.Thread(target=server.start_server)
    t1.start()
    t2.start()

def camera():
    client_camera=CameraClient(text_ip_add.get(1.0,'end-1c'),9000)
    t3=thd.Thread(target=client_camera.start_stream)
    t3.start()

def screen_share():
    client_screen_share=ScreenShareClient(text_ip_add.get(1.0,'end-1c'),9000)
    t4=thd.Thread(target=client_screen_share.start_stream)
    t4.start()

def mic():
    client_mic=AudioSender(text_ip_add.get(1.0,'end-1c'),8000)
    t5=thd.Thread(target=client_mic.start_stream)
    t5.start()


window = tk.Tk()
window.title("Client Side")
window.geometry('300x200')

label_ip_add= tk.Label(window, text="IP Add")
label_ip_add.pack()

text_ip_add=tk.Text(window, height=1)
text_ip_add.pack()

start_btn=tk.Button(window, text='Start Meeting', width=30, command=start_meeting)
start_btn.pack(anchor=tk.CENTER, expand=True)

camera_btn=tk.Button(window, text='Camera', width=30,command=camera)
camera_btn.pack(anchor=tk.CENTER, expand=True)

screen_share_btn=tk.Button(window, text="Screen Share", width=30,command=screen_share)
screen_share_btn.pack(anchor=tk.CENTER, expand=True)

mic_btn=tk.Button(window,text='Mic',width=30, command=mic)
mic_btn.pack(anchor=tk.CENTER, expand=True)

window.mainloop()