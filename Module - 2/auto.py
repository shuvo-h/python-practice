import pyautogui
import time
# pyautogui.alert("This is an alert from py auto gui")
time.sleep(5)
pyautogui.write("Thi is ato written text",interval=0.05)


def functionStructureTryRx():
    try:
        print(f'I am working')
    except:
        print(f'I am throwing error')
    finally:
        print(f'I am always working after finishing TRY EXCEPT')

