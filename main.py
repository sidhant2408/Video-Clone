from vidstream import *
import requests as rq
import tkinter as tk
import socket as sk
import threading as thd

#getting the local ip for hosting the meeting
local_ip_add= sk.gethostbyname(sk.gethostname())

#public ip address
# public_ip_add=rq.get('https://api.ipfy.org').text
# print(public_ip_add)


#creating connections for receiver and sender
server= StreamingServer(local_ip_add, 9000)
receiver=AudioReceiver(local_ip_add,8000)

#functions for the buttons created below
def start_meeting():
    t1= thd.Thread(target=server.start_server)
    t2=thd.Thread(target=server.start_server)
    t1.start()
    t2.start()

def camera():
    client_camera= CameraClient(text_ip_add.get(1.0,'end-1c'), 7000)
    t3= thd.Thread(target=client_camera.start_stream)
    t3.start()

def share_screen():
    client_share_screen=ScreenShareClient(text_ip_add.get(1.0,'end-1c'), 7000)
    t4=thd.Thread(target=client_share_screen.start_stream)
    t4.start()

def mic():
    client_mic=AudioSender(text_ip_add.get(1.0,'end-1c'), 6000)
    t5=thd.Thread(target=client_mic.start_stream)
    t5.start()


#creating GUI
    #creating window
window = tk.Tk()
window.title("Sender's Side")
window.geometry('300x200')

    #adding input fields
label_ip_add = tk.Label(window, text='Target IP')
label_ip_add.pack()

text_ip_add = tk.Text(window, height=1)
text_ip_add.pack()

    #adding buttons
start_btn= tk.Button(window, text='Start Meeting', width=30, command=start_meeting)
start_btn.pack(anchor=tk.CENTER, expand=True)

cam_btn= tk.Button(window, text='Camera', width = 30, command=camera)
start_btn.pack(anchor=tk.CENTER, expand=True)

screen_share_btn=tk.Button(window,text='Share Screen',width=30, command=share_screen)
screen_share_btn.pack(anchor=tk.CENTER,expand=True)

mic_btn=tk.Button(window,text='Mic',width=30, command=mic)
mic_btn.pack(anchor=tk.CENTER, expand=True)

window.mainloop()
