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

def snail_clicker():
    try:
        print("finding snail to click")
        selgui.click(r'zen_garden/click_snail.png',.9)
    except:
        print("did not find snail")
        pass
def diamond_checker():
    while True:
        try:
            selgui.click(r'zen_garden/diamond.png',.9)
            print("clicked a diamond.")
            time.sleep(1)
        except:
            print("no diamonds detected.")
            break
def zen_garden(extended_zen_garden_time):
    t_end = time.time() + extended_zen_garden_time
    while time.time()<t_end:
        pause_check.pause_menus()

        
        snail_clicker()
        pause_check.pause_menus()
        try:
            print("finding chocolate")
            selgui.click(r'zen_garden/chocolate.png',.9)
            print("found some chocolate")
            try:
                print("finding snail that needs chocolate")
                selgui.find(r'zen_garden/need_chocolate.png',.9)
                print("found need chocolate icon...")
                selgui.click(r'zen_garden/click_snail.png',.9)
                print("clicked on the snail to give it some chocolate")
            except:
                print("did not find snail that needs chocolate, clicking on bottom of screen to return chocolate to top of panel")
                selgui.click(r'zen_garden/zen_garden_text.png',.9)
        except:
            print("did not find any chcolate, skipping over that function...")
            pass
        while True:
            try:
                diamond_checker()
                print("finding water plants")
                selgui.click(r'zen_garden/need_water.png',.9)
                print("grabbing water can and clicking back on water icon...")
                selgui.click(r'zen_garden/water_can.png',.9)
                selgui.click(r'zen_garden/need_water.png',.9)
                time.sleep(2)
                i=0
            except:
                print("found no more plants that need water")
                break
        snail_clicker()
        pause_check.pause_menus()
        while True:
            try:
                diamond_checker()
                print("finding plants that need music")
                selgui.click(r'zen_garden/need_music.png',.9)
                print("grabbing fertilizer and clicking back on plants that need music...")
                try:
                    selgui.click(r'zen_garden/music.png',.9)
                except:
                    pass
                selgui.click(r'zen_garden/need_music.png',.9)
                i=0
                time.sleep(2)
            except:
                print("found no more plants that need music")
                break
        snail_clicker()
        pause_check.pause_menus()
        while True:
            try:
                diamond_checker()
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
                    time.sleep(240)
                    selgui.click(r'zen_garden/fertilizer_bag.png',.9)
                selgui.click(r'zen_garden/need_fertilizer.png',.9)
                i=0
                time.sleep(2)
            except:
                print("found no more plants that need fertilizer")
                break
        snail_clicker()
        pause_check.pause_menus()
        while True:
            try:
                diamond_checker()
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
                    time.sleep(240)
                    selgui.click(r'zen_garden/bug_spray.png',.9)
                selgui.click(r'zen_garden/need_bug_spray.png',.9)
                i=0
                time.sleep(2)
            except:
                print("found no more plants that need bug spray")
                break
        
        time_left = t_end - time.time()
        time_left_hours = time_left/3600
        print("time remaining: " + str(time_left) + " seconds or " + str(time_left_hours) + " hours.")
    #clicks the main menu button to go back to the main menu.
    try:
        selgui.click(r'main_menu_top_right.png',.9)
        time.sleep(2)
    except:
        pass

