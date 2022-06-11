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
def zen_garden():
    i=0
    #the zen garden will go through a loop ten times to find any plants that may need to get water, fertilizer, spray or music. 
    #in that time, if there is a plant that needs any of those items, the counter gets reset. If during that time, there is no plant that needs anything by the time
    #the counter gets to the limit, it will then break from the zen garden automation and go onto the next task to go through within the game.
    while True:
        if i>20:
            print("went through zen garden check " + str(i) + " times and found no plants that need anything, breaking out of loop and onto next main automation task...")
            break
        pause_check.pause_menus()

        try:
            selgui.click(r'zen_garden/zen_garden_text.png',.9)
        except:
            print("zen garden text no longer visible, breaking loop...")
            break
        snail_clicker()
        pause_check.pause_menus()
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
                    time.sleep(2)
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
                    time.sleep(2)
                    selgui.click(r'zen_garden/bug_spray.png',.9)
                selgui.click(r'zen_garden/need_bug_spray.png',.9)
                i=0
                time.sleep(2)
            except:
                print("found no more plants that need bug spray")
                break
        
        i+=1
        print(i)
    #clicks the main menu button to go back to the main menu.
    try:
        selgui.click(r'main_menu_top_right.png',.9)
        time.sleep(2)
    except:
        pass

