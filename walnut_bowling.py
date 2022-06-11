#walnut bowling script

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
def walnut_bowling_menu():
    if dpg.does_item_exist("main_menu"):
        dpg.show_item("main_menu")
    else:
        with dpg.window(label="Main Menu",tag="main_menu", width=850,height=500):
            dpg.add_text("Plants Vs. Zombies Sun clicker automation tool\n\n")
            dpg.add_checkbox(label="start walnut bowling script",tag="auto_walnut_bowling",callback=walnut_bowling)
class place_walnut:
    def grab_walnut():
        pause_check.pause_menus()

        try:
            print("finding exploding walnut")
            selgui.click(r'Plants/exploding_walnut_seed.png',.9)
            print("walnut found")
            pass
        except:
            print("exploding walnut not found")
            
            try:
                print("finding regular walnut")
                selgui.click(r'Plants/walnut_seed.png',.9)
                print("walnut found")
                pass
            except:
                print("regular walnut not found, looping again...")
    def find_zombie():
        print("finding zombie now...")
        print("finding zombies in column 2...")
        try:
            print("c2r1")
            selgui.find(r'Day_Regular_Field/c2r1.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r1()
        try:
            print("c2r2")
            selgui.find(r'Day_Regular_Field/c2r2.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r2()
        try:
            print("c2r3")
            selgui.find(r'Day_Regular_Field/c2r3.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r3()
        try:
            print("c2r4")
            selgui.find(r'Day_Regular_Field/c2r4.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r4()
        try:
            print("c2r5")
            selgui.find(r'Day_Regular_Field/c2r5.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r5()
        print("finding zombies in column 3...")
        try:
            print("c3r1")
            selgui.find(r'Day_Regular_Field/c3r1.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r1()
        try:
            print("c3r2")
            selgui.find(r'Day_Regular_Field/c3r2.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r2()
        try:
            print("c3r3")
            selgui.find(r'Day_Regular_Field/c3r3.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r3()
        try:
            print("c3r4")
            selgui.find(r'Day_Regular_Field/c3r4.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r4()
        try:
            print("c3r5")
            selgui.find(r'Day_Regular_Field/c3r5.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r5()
        print("finding zombies in column 4...")
        try:
            print("c4r1")
            selgui.find(r'Day_Regular_Field/c4r1.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r1()
        try:
            print("c4r2")
            selgui.find(r'Day_Regular_Field/c4r2.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r2()
        try:
            print("c4r3")
            selgui.find(r'Day_Regular_Field/c4r3.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r3()
        try:
            print("c4r4")
            selgui.find(r'Day_Regular_Field/c4r4.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r4()
        try:
            print("c4r5")
            selgui.find(r'Day_Regular_Field/c4r5.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r5()
        print("finding zombies in column 5...")
        try:
            print("c5r1")
            selgui.find(r'Day_Regular_Field/c5r1.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r1()
        try:
            print("c5r2")
            selgui.find(r'Day_Regular_Field/c5r2.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r2()
        try:
            print("c5r3")
            selgui.find(r'Day_Regular_Field/c5r3.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r3()
        try:
            print("c5r4")
            selgui.find(r'Day_Regular_Field/c5r4.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r4()
        try:
            print("c5r5")
            selgui.find(r'Day_Regular_Field/c5r5.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r5()
        print("finding zombies in column 6...")
        try:
            print("c6r1")
            selgui.find(r'Day_Regular_Field/c6r1.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r1()
        try:
            print("c6r2")
            selgui.find(r'Day_Regular_Field/c6r2.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r2()
        try:
            print("c6r3")
            selgui.find(r'Day_Regular_Field/c6r3.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r3()
        try:
            print("c6r4")
            selgui.find(r'Day_Regular_Field/c6r4.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r4()
        try:
            print("c6r5")
            selgui.find(r'Day_Regular_Field/c6r5.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r5()
        print("finding zombies in column 7...")
        try:
            print("c7r1")
            selgui.find(r'Day_Regular_Field/c7r1.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r1()
        try:
            print("c7r2")
            selgui.find(r'Day_Regular_Field/c7r2.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r2()
        try:
            print("c7r3")
            selgui.find(r'Day_Regular_Field/c7r3.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r3()
        try:
            print("c7r4")
            selgui.find(r'Day_Regular_Field/c7r4.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r4()
        try:
            print("c7r5")
            selgui.find(r'Day_Regular_Field/c7r5.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r5()
        print("finding zombies in column 8...")
        try:
            print("c8r1")
            selgui.find(r'Day_Regular_Field/c8r1.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r1()
        try:
            print("c8r2")
            selgui.find(r'Day_Regular_Field/c8r2.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r2()
        try:
            print("c8r3")
            selgui.find(r'Day_Regular_Field/c8r3.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r3()
        try:
            print("c8r4")
            selgui.find(r'Day_Regular_Field/c8r4.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r4()
        try:
            print("c8r5")
            selgui.find(r'Day_Regular_Field/c8r5.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r5()
        print("finding zombies in column 9...")
        try:
            print("c9r1")
            selgui.find(r'Day_Regular_Field/c9r1.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r1()
        try:
            print("c9r2")
            selgui.find(r'Day_Regular_Field/c9r2.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r2()
        try:
            print("c9r3")
            selgui.find(r'Day_Regular_Field/c9r3.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r3()
        try:
            print("c9r4")
            selgui.find(r'Day_Regular_Field/c9r4.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r4()
        try:
            print("c9r5")
            selgui.find(r'Day_Regular_Field/c9r5.png',.9)
        except:
            print("zombie likely")
            place_walnut.grab_walnut()
            place_walnut.place.r5()

    class place:
        def r1():
            print("placing on row 1")
            try:
                selgui.click(r'Day_Regular_Field/c1r1.png',.9)
                print("walnut clicked on row1")
            except:
                print("failed to place walnut")
                pass
        def r2():
            print("placing on row 2")

            try:
                selgui.click(r'Day_Regular_Field/c1r2.png',.95)
                print("walnut clicked on row2")
            except:
                print("failed to place walnut")
                pass
        def r3():
            print("placing on row 3")

            try:
                selgui.click(r'Day_Regular_Field/c1r3.png',.9)
                print("walnut clicked on row3")
            except:
                print("failed to place walnut")
                pass
        def r4():
            print("placing on row 4")

            try:
                selgui.click(r'Day_Regular_Field/c1r4.png',.9)
                print("walnut clicked on row4")
            except:
                print("failed to place walnut")
                pass
        def r5():
            print("placing on row 5")

            try:
                selgui.click(r'Day_Regular_Field/c1r5.png',.9)
                print("walnut clicked on row5")
            except:
                print("failed to place walnut")
                pass

def walnut_bowling():
    while True:
        pause_check.pause_menus()
        auto_walnut_bowling = dpg.get_value("auto_walnut_bowling")
        if auto_walnut_bowling==True:
            print("finding places on field where a zombie may be...")
            place_walnut.find_zombie()
        else:
            print("auto walnut bowling checkbox is now false, ending loop.")
            break


    



dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

walnut_bowling_menu()

#this goes at the very end of the script
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()