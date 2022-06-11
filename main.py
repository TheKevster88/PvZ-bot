#plants vs zombies parent automation class
import pyautogui
import dearpygui.dearpygui as dpg
import time
from pause_menus import pause_check
import dave_shop
import sys
import zen_garden_CHILD
import wisdom_tree_CHILD
import slot_machine_CHILD
import extended_zen_garden_CHILD

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

def pvz_main_automation_menu():
    if dpg.does_item_exist("main_menu"):
        dpg.show_item("main_menu")
    else:
        with dpg.window(label="Main Menu",tag="main_menu", width=850,height=500):
            dpg.add_text("Plants Vs. Zombies Main Automation Menu\n\n")
            dpg.add_text("When starting this script, make sure that the game is in windowed mode\nAND that you are at the main menu with the big grave.\n\n")
            dpg.add_checkbox(label="Include slot machine minigame automation",tag="slot_machine")
            dpg.add_input_int(label="Number of minigame wins before moving onto next task",width=100,tag="win_count",default_value=10)
            dpg.add_text("\n")
            dpg.add_checkbox(label="include quick zen garden maintenance automation",tag="zen_garden")
            dpg.add_text("\nZen garden option below include extended zen garden afk automation\n-includes chocolate to snail, and being able to set\n how many hours you wish to afk...")
            dpg.add_checkbox(label="include extended zen garden afk automation (chocolate functionality included",tag="extended_zen_garden")
            dpg.add_input_float(label="How many hours to afk in zen garden?",tag="zen_garden_hours",default_value=1)
            dpg.add_text("\n")
            dpg.add_checkbox(label="include Wisdom tree automation",tag="wisdom_tree")
            
            dpg.add_text("\n\n")
            dpg.add_button(label="start game automation",tag="main_automation",callback=start_automation)



def start_automation():
    while True:
        slot_machine_automation = dpg.get_value("slot_machine")
        win_count = dpg.get_value("win_count")
        zen_garden_automation = dpg.get_value("zen_garden")
        extended_zen_garden_automation = dpg.get_value("extended_zen_garden")
        zen_garden_hours = dpg.get_value("zen_garden_hours")
        wisdom_tree_automation = dpg.get_value("wisdom_tree")
        if zen_garden_hours <.001:
            zen_garden_hours = 1
        
        if zen_garden_automation is not False or slot_machine_automation is not False or wisdom_tree_automation is not False or extended_zen_garden_automation is not False:
            print("at least one option is selected, proceeding with script")
            time.sleep(1)
            if slot_machine_automation is True:
                print("starting slot machine minigame automation, the script will then move to the next items every specified amount of wins")
                selgui.click(r'main_menu/minigames.png',.9)
                slot_machine_CHILD.slot_machine(win_count)
                time.sleep(3)
            if zen_garden_automation is True:
                print("starting zen garden script")
                selgui.click(r'main_menu/zen_garden_icon.png',.9)
                zen_garden_CHILD.zen_garden()
                time.sleep(3)
            if extended_zen_garden_automation is True:
                print("starting extended zen garden automation")
                selgui.click(r'main_menu/zen_garden_icon.png',.9)
                #calculating total zen garden time...
                extended_zen_garden_time = zen_garden_hours * 3600
                print("total afk time in zen garden is " + str(zen_garden_hours) + " hours or " + str(extended_zen_garden_time) + " seconds")
                extended_zen_garden_CHILD.zen_garden(extended_zen_garden_time)
                time.sleep(3)
            if wisdom_tree_automation is True:
                print("starting wisdom tree automation")
                selgui.click(r'main_menu/zen_garden_icon.png',.9)
                time.sleep(1)
                selgui.click(r'main_menu/golden_arrow.png',.9)
                while True:
                    try:
                        selgui.find(r'wisdom_tree/wisdom_tree_text.png',.9)
                        break
                    except:
                        selgui.click(r'main_menu/golden_arrow.png',.9)
                wisdom_tree_CHILD.wisdom_tree()
                time.sleep(3)
            

        else:
            print("no minigames were actively selected, breaking out of loop until the start button is pressed again.")
            break


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


pvz_main_automation_menu()


#this goes at the very end of the script
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()