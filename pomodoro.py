from playsound import playsound
import time
print("""
    pomodoro = 1.0
    tavsiye set sayısı 4'dür
""")
while True:
    tur = input("Kaç set yapmak istersiniz:")
    if tur == "q" or tur == "Q":
        print("Çıkış yapıldı.")
    calisma  = input("Çalışma sürenizi giriniz:")
    if calisma == "q" or calisma == "Q":
        print("Çıkış yapıldı")
        break
    dinlen   = input("Dinlenme süresini giriniz:")
    if dinlen == "q" or dinlen == "Q":
        print("Çıkış yapıldı.")
        break
    try:
        sayi1 = int(calisma)
        sayi2 = int(dinlen)
        turr  = int(tur)
        sayi1x = sayi1 * 60
        sayi2x = sayi2 * 60
        sayi1 = sayi1x
        sayi2 = sayi2x
        break
    except ValueError:
        print("Lütfen tam sayı giriniz örnek(1,5,8,6,4,3)")
    except ZeroDivisionError:
        print("Çalışmanız bitmişdir:")
        break
for i in range(turr):
    playsound('bildir.mp3')
    for i in range(sayi1):
        time.sleep(1)
        sayi1 -= 1
        print("Çalışmanın bitmesine:",sayi1)
        if sayi1 == 0:
            playsound('bildir,mp3')
            for i in range(sayi2):
                time.sleep(1)
                sayi2 -= 1
                print("Dinlenme kalan süre:",sayi2)
    if turr == turr:
        print("Çalışmanız bitmiştir")
        playsound('bildir.mp3')