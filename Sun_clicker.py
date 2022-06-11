#Plants VS Zombies Sunflower autoclicker
import pyautogui
import dearpygui.dearpygui as dpg
import time
class selgui:
    def click(element,confidence_value):
        try:
            x, y = pyautogui.locateCenterOnScreen(element, confidence=confidence_value)
            pyautogui.moveTo(x, y)
            pyautogui.click()
        except:
            print("failed to click")
  
def sun_clicker_menu():
    if dpg.does_item_exist("main_menu"):
        dpg.show_item("main_menu")
    else:
        with dpg.window(label="Main Menu",tag="main_menu", width=850,height=500):
            dpg.add_text("Plants Vs. Zombies Sun clicker automation tool\n\n")
            dpg.add_checkbox(label="start automatic sun collection",tag="auto_sun_collection",callback=sun_clicker)
def sun_clicker():
    while True:
        sun_clicker_checkbox = dpg.get_value("auto_sun_collection")
        if sun_clicker_checkbox==True:
            print("auto sun clicker enabled, beginning automation")
            try:
                selgui.click(r'Sun.png',.8)
                print("clicked sunflower")
                time.sleep(.1)
            except KeyboardInterrupt:
                print("keyboard interruption detected. stopping automation")
                break
            except:
                print("couldn't do thing")
        else:
            print("auto clicker turned off. canceling automation")
            break
    
dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


sun_clicker_menu()


#this goes at the very end of the script
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()