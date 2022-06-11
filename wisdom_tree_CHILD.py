import pyautogui
import dearpygui.dearpygui as dpg
import time
from pause_menus import pause_check
import dave_shop
import sys


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

def wisdom_tree():
    
    while True:
        pause_check.pause_menus()
        try:
            selgui.click(r'wisdom_tree/wisdom_fertilizer.png',.9)
            pass
        except:
            try:
                selgui.click(r'dave_shop/wisdom_fertilizer_empty.png',.9)
                #click the shop button then execute crazy dave shop buy function
                selgui.click(r'dave_shop/zen_garden_shop_button.png',.9)
                shop_result = "null"
                dave_shop.Dave_Store.buy_request('wisdom_fertilizer')
                try:
                    selgui.find(r'dave_shop/wisdom_fertilizer_empty.png',.9)
                    print("purchase function failed, most likely due to insufficient funds, breaking out of wisdom tree loop.")
                    break
                except:
                    pass
            except:
                pass
        try:
            selgui.click(r'wisdom_tree/plant_1.png',.9)
        except:
            try:
                selgui.click(r'wisdom_tree/plant_2.png',.9)
            except:
                try:
                    selgui.click(r'wisdom_tree/plant_3.png',.95)
                except:
                    try:
                        selgui.click(r'wisdom_tree/plant_4.png',.9)
                    except:
                        try:
                            selgui.click(r'wisdom_tree/plant_5.png',.9)
                        except:
                            pass
                    
    #clicks the main menu button to go back to the main menu.
    try:
        selgui.click(r'main_menu_top_right.png',.9)
        time.sleep(2)
    except:
        pass
