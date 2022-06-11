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

def wisdom_tree_menu():
    if dpg.does_item_exist("main_menu"):
        dpg.show_item("main_menu")
    else:
        with dpg.window(label="Main Menu",tag="main_menu", width=850,height=500):
            dpg.add_text("Plants Vs. Zombies Wisdom Tree Automation\n\n")
            dpg.add_checkbox(label="start zen tree growth automation",tag="zen_tree_automation",callback=wisdom_tree)
def wisdom_tree():
    
    while True:
        pause_check.pause_menus()
        zen_tree_automation = dpg.get_value("zen_tree_automation")
        if zen_tree_automation==True:
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
                pass
        else:
            break
    #clicks the golden arrow button to go back to the zengarden.
    try:
        selgui.click(r'main_menu_top_right.png',.9)
    except:
        pass
dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


wisdom_tree_menu()


#this goes at the very end of the script
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()