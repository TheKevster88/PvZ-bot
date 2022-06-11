#crazy dave shopping code
#this will be an imported class to other parent files where the target element is passed into this function and searches. 
#there will be error checking for insufficient funds and return that back to the script

import pyautogui
import time
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

class Dave_Store:
    def buy_request(item):
        if item not in ['fertilizer','bug_spray','crap_plant','wisdom_fertilizer','garden_rake']:
            print("invalid item buy request.")
            shop_result = "invalid"
            return shop_result
        else:
            time.sleep(3)
            print("check for specific request made.")
            #if the item locations are static, a class could probably be made to shuffle through he 'next' and 'previous' blinker lights to find where the item is located.
            if item == 'fertilizer':
                print("finding fertilizier")
                while True:
                    try:
                        selgui.click(r'dave_shop/fertilizer.png',.9)
                        break
                    except:
                        selgui.click(r'dave_shop/next.png',.9)
                Dave_Store.insufficient_funds_check()
            if item == 'bug_spray':
                print("finding bug spray")
                while True:
                    try:
                        selgui.click(r'dave_shop/bug_spray.png',.9)
                        break
                    except:
                        selgui.click(r'dave_shop/next.png',.9)
                Dave_Store.insufficient_funds_check()
            if item == 'crap_plant':
                print("finding the cheap plant")
            if item == 'wisdom_fertilizer':
                print("finding the wisdom tree fertilizer")
                while True:
                    try:
                        selgui.click(r'dave_shop/wisdom_fertilizer.png',.9)
                        break
                    except:
                        selgui.click(r'dave_shop/next.png',.9)
                Dave_Store.insufficient_funds_check()
            if item == 'garden_rake':
                print("finding the garden rake")

    def insufficient_funds_check():
        try:
            selgui.find(r'dave_shop/insufficient_funds.png',.9)
            print("ur 2 poor m8")
            selgui.click(r'dave_shop/ok.png',.9)
            shop_result = "insufficient"
        except:
            print("insufficient prompt not detect, going to click yes to buy.")
            selgui.find(r'dave_shop/buy_item_prompt.png',.9)
            selgui.click(r'dave_shop/yes.png',.9)
            shop_result = "successfully"   
        selgui.click(r'dave_shop/go_back.png',.9)
        return shop_result
