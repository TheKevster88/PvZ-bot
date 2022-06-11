#checks if pause mmenu(s) are open and will stop script until menus are gone...
import pyautogui

class pause_check:
    def find(element):
        x, y = pyautogui.locateCenterOnScreen(element)
    def pause_menus():
        try:
            print("checking pause menus...")
            pause_check.find(r'pause_menus/menu.png')
            print("pause menu detected, pausing automation...")
            while True:
                try:
                    pause_check.find(r'pause_menus/menu.png')
                except:
                    print("pause menu no longer detected.")
                    break
        except:
            print("did not find pause menu")
            pass
        try:
            pause_check.find(r'pause_menus/game_paused.png')
            print("game paused popup detected, pausing automation...")
            while True:
                try:
                    pause_check.find(r'pause_menus/game_paused.png')
                except:
                    print("popup no longer detected.")
                    break
        except:
            print("did not find game paused popup")
            pass
