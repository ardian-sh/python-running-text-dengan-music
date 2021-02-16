from playsound import playsound
from time import sleep
from threading import Thread
import os

def music():
    song = 'Hingga Akhir Waktu.mp3'
    playsound(song)

def run_text(text):
    for i in text:
        print(i, end="", flush=True)
        sleep(0.09)

def list_text():
    text_list = ["Aku tak pandai merangkai sebuah kata\n",
        "Aku pun tak pandai dalam hal bercerita\n",
        "Jika diizinkan bercerita apa yang aku bisa\n",
        "Akupun bingung harus jawab apa\n\n",

        "Tapi yang ku tahu aku punya rindu\n",
        "Rindu pada seseorang yang sudah lama tidak bertemu\n",
        "Bertemu pun entah kapan\n",
        "Entah akan jadi kenyataan atau hanya sebuah harapan\n\n",

        "Nama dia adalah ???????????\n",
        "Gadis yang ku kenal melalui Kuliah Kerja Nyata\n",
        "Gadis ngeselin kadang juga ngangenin\n",
        "Yang selalu membuat ku emosi kadang tertawa\n\n",

        "Semoga suatu hari nanti kita bisa bertemu\n",
        "Agar rindu ini terbalaskan tidak membatu\n",
        "Membuat cerita nyata Kembali tanpa halu\n",
        "Hingga akhirnya ku bisa berucap I LOVE YOU\n"
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