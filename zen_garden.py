import pyautogui
import dearpygui.dearpygui as dpg
import time
from pause_menus import pause_check
import dave_shop


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

def zen_garden_menu():
    if dpg.does_item_exist("main_menu"):
        dpg.show_item("main_menu")
    else:
        with dpg.window(label="Main Menu",tag="main_menu", width=850,height=500):
            dpg.add_text("Plants Vs. Zombies Zen Garden automation tool\n\n")
            dpg.add_checkbox(label="start automatic sun collection",tag="zen_garden_automation",callback=zen_garden)
def snail_clicker():
    try:
        print("finding snail to click")
        selgui.click(r'zen_garden/click_snail.png',.9)
    except:
        print("did not find snail")
        pass
def zen_garden():
    
    while True:
        pause_check.pause_menus()
        sun_clicker_checkbox = dpg.get_value("zen_garden_automation")
        if sun_clicker_checkbox==True:
            try:
                selgui.click(r'zen_garden/zen_garden_text.png',.9)
            except:
                print("zen garden text no longer visible, breaking loop...")
                break
            snail_clicker()
            pause_check.pause_menus()
            while True:
                try:
                    print("finding water plants")
                    selgui.click(r'zen_garden/need_water.png',.9)
                    print("grabbing water can and clicking back on water icon...")
                    selgui.click(r'zen_garden/water_can.png',.9)
                    selgui.click(r'zen_garden/need_water.png',.9)
                    time.sleep(2)
                except:
                    print("found no more plants that need water")
                    break
            snail_clicker()
            pause_check.pause_menus()
            while True:
                try:
                    print("finding plants that need fertilizer")
                    selgui.click(r'zen_garden/need_fertilizer.png',.9)
                    print("grabbing fertilizer and clicking back on plants that need fertilizer...")
                    try:
                        selgui.click(r'zen_garden/fertilizer_bag.png',.9)
                    except:
                        print("couldn't click fertilizer")
                        selgui.find(r'dave_shop/fertilizer_empty.png',.9)
                        selgui.click(r'dave_shop/zen_garden_shop_button.png',.9)
                        dave_shop.Dave_Store.buy_request('fertilizer')
                        time.sleep(2)
                        selgui.click(r'zen_garden/fertilizer_bag.png',.9)
                    selgui.click(r'zen_garden/need_fertilizer.png',.9)
                    time.sleep(2)
                except:
                    print("found no more plants that need fertilizer")
                    break
            snail_clicker()
            pause_check.pause_menus()
            while True:
                try:
                    print("finding plants that need bug spray")
                    selgui.click(r'zen_garden/need_bug_spray.png',.9)
                    print("grabbing bug spray and clicking back on plants that need bug spray...")
                    try:
                        selgui.click(r'zen_garden/bug_spray.png',.9)
                    except:
                        print("couldn't click bug spray")
                        selgui.find(r'dave_shop/bug_spray_empty.png',.9)
                        selgui.click(r'dave_shop/zen_garden_shop_button.png',.9)
                        dave_shop.Dave_Store.buy_request('bug_spray')
                        time.sleep(2)
                        selgui.click(r'zen_garden/bug_spray.png',.9)
                    selgui.click(r'zen_garden/need_bug_spray.png',.9)
                    time.sleep(2)
                except:
                    print("found no more plants that need bug spray")
                    break
            snail_clicker()
            pause_check.pause_menus()
            while True:
                try:
                    print("finding plants that need music")
                    selgui.click(r'zen_garden/need_music.png',.9)
                    print("grabbing fertilizer and clicking back on plants that need music...")
                    try:
                        selgui.click(r'zen_garden/music.png',.9)
                    except:
                        pass
                    selgui.click(r'zen_garden/need_music.png',.9)
                    time.sleep(2)
                except:
                    print("found no more plants that need music")
                    break
        else:
            print("breaking loop...")
            break


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


zen_garden_menu()


#this goes at the very end of the script
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()