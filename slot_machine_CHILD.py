#Plants VS Zombies Sunflower autoclicker
import pyautogui
import dearpygui.dearpygui as dpg
import time
from pause_menus import pause_check
class selgui:
    def click(element,confidence_value):
        x, y = pyautogui.locateCenterOnScreen(element, confidence=confidence_value)
        pyautogui.moveTo(x, y)
        pyautogui.click()
    def find(element,confidence_value):
        x, y = pyautogui.locateCenterOnScreen(element,confidence=confidence_value)    
class mouse_coords:
    def goto_coords(mousex,mousey): 
        pyautogui.moveTo(mousex,mousey)

class place_plant:
    def find_plants():
        try_again_prompt()
        print("finding plants")
        while True:
            try:
                print("finding sunflower")
                selgui.click(r'slot_machine/sunflower.png',.9)

                place_plant.sunflower()
                place_plant.find_plants()
            except:
                pass
            try:
                print("finding walnut")
                selgui.click(r'slot_machine/walnut.png',.9)
                print("walnut found")
                place_plant.walnut()
                place_plant.find_plants()
            except:
                pass
            try:
                print("finding peashooter")
                selgui.click(r'slot_machine/peashooter.png',.9)
                print("peashooter found.")
                place_plant.peashooter()
                place_plant.find_plants()
            except:
                pass
            try:
                print("finding freezing peashooter")
                selgui.click(r'slot_machine/frozen_peashooter.png',.9)
                print("frozen peashooter found.")
                place_plant.peashooter()
                place_plant.find_plants()
            except:
                break

    def sunflower():
        place_plant.c1_check()
    def walnut():
        place_plant.c8_check()
    def peashooter():
        place_plant.c1_check()

    def c1_check():
        print("finding open spot in column 1 to place plant...")
        try:
            selgui.click(r'slot_machine/c1r1.png',.9)
        except:
            print("c1r1 not available")
            try:
                selgui.click(r'slot_machine/c1r2.png',.9)
            except:
                print("c1r2 not available")
                try:
                    selgui.click(r'slot_machine/c1r3.png',.9)
                except:
                    print("c1r3 not available")
                    try:
                        selgui.click(r'slot_machine/c1r4.png',.9)
                    except:
                        print("c1r4 not available")
                        try:
                            selgui.click(r'slot_machine/c1r5.png',.9)
                        except:
                            print("c1r5 not available")
                            place_plant.c2_check()
    def c2_check():
        print("finding open spot in column 2 to place plant...")
        try:
            selgui.click(r'slot_machine/c2r1.png',.9)
        except:
            print("c2r1 not available")
            try:
                selgui.click(r'slot_machine/c2r2.png',.9)
            except:
                print("c2r2 not available")
                try:
                    selgui.click(r'slot_machine/c2r3.png',.9)
                except:
                    print("c2r3 not available")
                    try:
                        selgui.click(r'slot_machine/c2r4.png',.9)
                    except:
                        print("c2r4 not available")
                        try:
                            selgui.click(r'slot_machine/c2r5.png',.9)
                        except:
                            print("c2r5 not available")
                            place_plant.c3_check()
    def c3_check():
        print("finding open spot in column 3 to place plant...")
        try:
            selgui.click(r'slot_machine/c3r1.png',.9)
        except:
            print("c3r1 not available")
            try:
                selgui.click(r'slot_machine/c3r2.png',.9)
            except:
                print("c3r2 not available")
                try:
                    selgui.click(r'slot_machine/c3r3.png',.9)
                except:
                    print("c3r3 not available")
                    try:
                        selgui.click(r'slot_machine/c3r4.png',.9)
                    except:
                        print("c3r4 not available")
                        try:
                            selgui.click(r'slot_machine/c3r5.png',.9)
                        except:
                            print("c3r5 not available")
                            place_plant.c4_check()
    def c4_check():
        print("finding open spot in column 4 to place plant...")
        try:
            selgui.click(r'slot_machine/c4r1.png',.9)
        except:
            print("c4r1 not available")
            try:
                selgui.click(r'slot_machine/c4r2.png',.9)
            except:
                print("c4r2 not available")
                try:
                    selgui.click(r'slot_machine/c4r3.png',.9)
                except:
                    print("c4r3 not available")
                    try:
                        selgui.click(r'slot_machine/c4r4.png',.9)
                    except:
                        print("c4r4 not available")
                        try:
                            selgui.click(r'slot_machine/c4r5.png',.9)
                        except:
                            print("c4r5 not available")
                            place_plant.c5_check()
    def c5_check():
        print("finding open spot in column 5 to place plant...")
        try:
            selgui.click(r'slot_machine/c5r1.png',.9)
        except:
            print("c5r1 not available")
            try:
                selgui.click(r'slot_machine/c5r2.png',.9)
            except:
                print("c5r2 not available")
                try:
                    selgui.click(r'slot_machine/c5r3.png',.9)
                except:
                    print("c5r3 not available")
                    try:
                        selgui.click(r'slot_machine/c5r4.png',.9)
                    except:
                        print("c5r4 not available")
                        try:
                            selgui.click(r'slot_machine/c5r5.png',.9)
                        except:
                            print("c5r5 not available")
                            place_plant.c6_check()
    def c6_check():
        print("finding open spot in column 6 to place plant...")
        try:
            selgui.click(r'slot_machine/c6r1.png',.9)
        except:
            print("c6r1 not available")
            try:
                selgui.click(r'slot_machine/c6r2.png',.9)
            except:
                print("c6r2 not available")
                try:
                    selgui.click(r'slot_machine/c6r3.png',.9)
                except:
                    print("c6r3 not available")
                    try:
                        selgui.click(r'slot_machine/c6r4.png',.9)
                    except:
                        print("c6r4 not available")
                        try:
                            selgui.click(r'slot_machine/c6r5.png',.9)
                        except:
                            print("c6r5 not available")
                            place_plant.c7_check()
    def c7_check():
        print("finding open spot in column 7 to place plant...")
        try:
            selgui.click(r'slot_machine/c7r1.png',.9)
        except:
            print("c7r1 not available")
            try:
                selgui.click(r'slot_machine/c7r2.png',.9)
            except:
                print("c7r2 not available")
                try:
                    selgui.click(r'slot_machine/c7r3.png',.9)
                except:
                    print("c7r3 not available")
                    try:
                        selgui.click(r'slot_machine/c7r4.png',.9)
                    except:
                        print("c7r4 not available")
                        try:
                            selgui.click(r'slot_machine/c7r5.png',.9)
                        except:
                            print("c7r5 not available")
                            place_plant.c8_check()
    def c8_check():
        print("finding open spot in column 4 to place plant...")
        try:
            selgui.click(r'slot_machine/c8r1.png',.9)
        except:
            print("c8r1 not available")
            try:
                selgui.click(r'slot_machine/c8r2.png',.9)
            except:
                print("c8r2 not available")
                try:
                    selgui.click(r'slot_machine/c8r3.png',.9)
                except:
                    print("c8r3 not available")
                    try:
                        selgui.click(r'slot_machine/c8r4.png',.9)
                    except:
                        print("c8r4 not available")
                        try:
                            selgui.click(r'slot_machine/c8r5.png',.9)
                        except:
                            print("c8r5 not available")
                            place_plant.c9_check()
    def c9_check():
        print("finding open spot in column 9 to place plant")
        try:
            selgui.click(r'slot_machine/c9r1.png',.9)
        except:
            print("c9r1 not available")
            try:
                selgui.click(r'slot_machine/c9r2.png',.9)
            except:
                print("c9r2 not available")
                try:
                    selgui.click(r'slot_machine/c9r3.png',.9)
                except:
                    print("c9r3 not available")
                    try:
                        selgui.click(r'slot_machine/c9r4.png',.9)
                    except:
                        print("c9r4 not available")
                        try:
                            selgui.click(r'slot_machine/c9r5.png',.9)
                        except:
                            print("c9r5 not available")
                            try_again_prompt()
def try_again_prompt():
    try:
        selgui.click(r'slot_machine/try_again.png',.9)
    except:
        pass
def slot_machine(win_count):
    i=0
    while True:
        if i>=win_count:
            print("automation has won " + str(i) + " times, exiting minigame automation to next major task.")
            time.sleep(10)
            break
        try:
            selgui.click(r'slot_machine/slot_machine_minigame.png',.9)
            selgui.click(r'slot_machine/new_game.png',.9)
            selgui.click(r'slot_machine/new_game.png',.9)
        except:
            pass
        try_again_prompt()
        pause_check.pause_menus()
        try:
            selgui.click(r'slot_machine/chocolate.png',.9)
            print("clicked chocolate")
        except:
            pass
        try:
            selgui.click(r'present_box.png',.9)
            print("clicked present")
        except:
            pass
        try:
            selgui.click(r'slot_machine/trophybag.png',.9)
            time.sleep(1)
            try:
                selgui.click(r'slot_machine/trophybag.png',.9)
            except:
                pass
            print("trophy found and clicked, level ended.")
            i+=1
            print(i)
        except:
            try:
                selgui.click(r'slot_machine/trophybag.png',.9)
            except:
                pass
        try:
            selgui.click(r'slot_machine/diamond.png',.9)
        except:
            print("did not find a diamond.")
            pass
        try:
            try_again_prompt()
            
            print("finding sunflower")
            selgui.click(r'Sun.png',.8)
            pyautogui.click(clicks=5, interval=0.1)
            print("clicked sunflower")
            time.sleep(.1)
            
        except KeyboardInterrupt:
            print("keyboard interruption detected. stopping automation")
            break
        except:
            print("did not see sunflower")
            try:
                mousex, mousey = pyautogui.position()
                print("finding handle")
                while True:
                    selgui.click(r'slot_machine/spin_handle.png',.8)
                    print("clicked SpinHandle")
                    mouse_coords.goto_coords(mousex,mousey)
                    j=0
                    while True:
                        try_again_prompt()
                        try:
                            print("finding sunflower")
                            selgui.click(r'Sun.png',.8)
                            pyautogui.click(clicks=5, interval=0.1)
                            print("clicked sunflower")
                            j+=1
                        except:
                            break
                        
                    try:
                        selgui.find(r'slot_machine/spin_again.png',.7)
                        print("sping again text detected, clicking handle again...")
                    except:
                        break
                place_plant.find_plants()
            except:
                print("did not see handle")
    time.sleep(1)
    selgui.click(r'main_menu/back_to_main_menu_bottom_left.png',.9)