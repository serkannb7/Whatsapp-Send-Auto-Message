import pywhatkit
import pyautogui

try:
    PHONE_NUMBER = input("Enter Phone Number...\n" "(Don't forget to add 'calling codes (+90 for TURKEY )' at the beginning!!! )\n")
    MESSAGE = input("Enter your message...\n")
    HOUR = int(input("Enter hour...\n"))
    MINUTE = int(input("Enter minute....\n"))
    pywhatkit.sendwhatmsg(PHONE_NUMBER, MESSAGE, HOUR, MINUTE, 40)
    pyautogui.press('enter')
    print("Message Sent")
except:
    print("ERROR!")



