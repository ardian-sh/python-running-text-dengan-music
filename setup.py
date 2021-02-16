import simpleaudio as sa
from time import sleep
import os

def music():
    global play_obj
    song = 'hingga-akhir-waktu.wav' #hanya bisa  memutar audio dengan format wav,
    wave_obj = sa.WaveObject.from_wave_file(song)
    play_obj = wave_obj.play()

def run_text(text):
    for i in text:
        print(i, end="", flush=True)
        sleep(0.09)

def list_text():
    text_list = ["Aku tak pandai merangkai sebuah kata\n",
        "Aku pun tak pandai dalam hal bercerita\n",
        "Jika diizinkan bercerita apa yang aku bisa\n",
        "Akupun bingung harus jawab apa\n\n"

        "Tapi yang ku tahu aku punya rindu\n",
        "Rindu pada seseorang yang sudah lama tidak bertemu\n",
        "Bertemu pun entah kapan\n",
        "Entah akan jadi kenyataan atau hanya sebuah harapan\n\n",

        "Nama dia adalah ???????????\n",
        "Gadis yang ku kenal melalui pesan WA\n",
        "Gadis ngeselin kadang juga ngangenin\n",
        "Yang selalu membuat ku emosi kadang tertawa\n\n",

        "Semoga suatu hari nanti kita bisa bertemu\n",
        "Agar rindu ini terbalaskan tidak membatu\n",
        "Membuat cerita nyata Kembali tanpa halu\n",
        "Hingga akhirnya ku bisa berucap I LOVE YOU\n\n"
        ]
    for i in text_list:
        run_text(i)
        sleep(1.5)

play_obj = "variabel global, nantinya akan di replace dengan value yang ada di function music"

while(True):
    a = input("enter kalau mau mulai (^_^) : ")
    if (a == ""):
        os.system("cls")

        music()

        list_text()

        print("dah gitu aja, bingung mau apa lagi :v")
        b = input("enter aja kalau mau berhenti : ")
        if (b == "" or b !=""):
            play_obj.stop()
            break
    else:
        print("harus enter sayang ku jangan yang lain -_- \n")
