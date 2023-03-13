import pywhatkit
import pyautogui

try:
    TELEFON_NO = input("Telefon Numarasını Girin...\n" "(Başına '+90' eklemeyi unutmayın !!! )\n")
    MESAJ = input("Mesajınızı Girin...\n")
    SAAT = int(input("Saati Girin...\n"))
    DAKIKA = int(input("Dakika Girin....\n"))
    pywhatkit.sendwhatmsg(TELEFON_NO,MESAJ,SAAT,DAKIKA,40)
    pyautogui.press('enter')
    print("Mesaj GÖnderildi")
except:
    print("HATA !")


