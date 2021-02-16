from playsound import playsound
from time import sleep
from threading import Thread
import os

def music():
    song = 'judul lagu.mp3' #ganti judul lagu sesuai keinginan
    playsound(song)

def run_text(text):
    for i in text:
        print(i, end="", flush=True)
        sleep(0.09)

def list_text():
    text_list = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n", #sesuaikan dengan kalimat yang  diinginkan
        "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
        ]
    for i in text_list:
        run_text(i)
        sleep(1.5)

while(True):
    a = input("enter : ")
    if(a == ""):
        os.system("cls")

        musik = Thread(target=music)
        musik.start()

        teks = Thread(target=list_text)
        teks.start()
    else:
        print("please enter \n")
