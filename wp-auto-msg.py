print("""************************************************


Whatsapp Otomatik Mesaj Gönderme Uygulaması...


************************************************|\n""")

import pywhatkit
import pyautogui

try:
    telefon_no = input("Telefon Numarasını Girin...\n" "(Başına '+90' eklemeyi unutmayın !!! )\n")
    mesaj = input("Mesajınızı Girin...\n")
    SAAT = int(input("Saati Girin...\n"))
    DAKİKA = int(input("Dakika Girin....\n"))
    pywhatkit.sendwhatmsg(telefon_no,mesaj,SAAT,DAKİKA,40)
    pyautogui.press('enter')
    print("Mesaj GÖnderildi")
except:
    print("HATA !")


