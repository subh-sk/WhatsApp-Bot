import pyautogui as pt  #pip install pyautogui
import pyperclip as pc  #pip install pyperclip
from pynput.mouse import Button,Controller
from time import sleep
import keyboard  # pip install keyboard
import wikipedia as wiki
import requests
import random

pt.FAILSAFE=True
mouse=Controller()

# Navigate to any image

def nav_to_img(image,clicks,off_x=0,off_y=0):
    position=pt.locateCenterOnScreen(image,confidence=.8)  #.8 is for checking image is matching 80% than it will procced
    if position is None:
        print(f"Image not found...",clicks)
        return 0
    else:
        pt.moveTo(position,duration=.3)  #.5 sec.
        pt.moveRel(off_x,off_y,duration=.1)
        pt.click(clicks=clicks,interval=.1)
        
    
def get_message():
    nav_to_img('WhatsApp_bot_img\media.png',0,off_y=-80) #-80 is my pixle from media icon to go up our cursor 
    mouse.click(Button.left,3) #3 mean number of left-mouse click
    pt.rightClick()
    copy = nav_to_img('WhatsApp_bot_img\copy.png',1)#1 mean number of mouse click
    sleep(.5)
    return pc.paste() if copy !=0 else 0

def send_message(msg,*args):
    nav_to_img('WhatsApp_bot_img\media.png',2,off_x=150) #150 is my pixle from media icon to go up our cursor 
    pt.typewrite(msg,interval=.1)
    for i in range(len(args)):
        if "keyboard.press_and_release('shift+enter')" in i:
            keyboard.press_and_release('shift+enter')
        else:
        # pt.typewrite(f"{msg}",interval=.1)
            pt.typewrite(args,interval=.1)
    
    pt.typewrite('\n')  #used as enter to send msg 

def close_reply_box():
    nav_to_img('WhatsApp_bot_img\cancel.png',2) #2 mean number of mouse click
    
def process_message(msg):
    raw_msg=msg.lower()
    if raw_msg=='hello' or raw_msg=='hii' or raw_msg=='hi':
        x="keyboard.press_and_release('shift+enter')"
        y="How can I help you"
        # return "hello there how are you. {keyboard.press_and_release('shift+enter')} How can I help you."
        print("hello there how are you",x,y)
        return "hello there how are you",x,y
    elif raw_msg=="yes":
        return "Bot says you wrote yes."
    elif 'how are you' in raw_msg or 'fine and you' in raw_msg or 'good and you' in raw_msg or 'what about you' in raw_msg:
        return f"I'm also fine, Thankyou for asking :) {keyboard.press_and_release('shift+enter')} How can I help you."
    elif ('what' in raw_msg or 'who' in raw_msg or 'when' in raw_msg or 'how' in raw_msg or 'where' in raw_msg or 'why' in raw_msg):
        info =wiki.summary(msg,2) #2 mean number of line
        return f"according to wikipedia {info}"
    elif 'thankyou' in raw_msg or 'thank you' in raw_msg:
        return "It's my pleasure that I am able to help you"
    # elif ''
    else:
        return "I did not understand what you wrote."
def open_wp():
    keyboard.press_and_release('win')
    sleep(1)
    nav_to_img(r'WhatsApp_bot_img\search.png',1)
    pt.typewrite('Whatsapp',interval=.1)
    sleep(1)
    nav_to_img(r"WhatsApp_bot_img\whatsapp_logo.png",2,off_y=50)
    # sleep(10)
    

last_msg=''


#opening whatsapp
sleep(2)
open_wp()
sleep(12)
while True:
    
    # check for new messages
    nav_to_img(r"WhatsApp_bot_img\unread.png",2,off_x=-150)
    # close_reply_box()
    messgae=get_message()
    sleep(.2)
    if messgae!=0 and messgae!=last_msg:
        last_msg=messgae
        send_message(process_message(messgae))
    else:
        print('There are no new messages')
    close_reply_box()
    sleep(5) #sleep for 10 sec than again looping start
    




    
# sleep(3)
            # checking all the function is working or not
            
# nav_to_img(r"PYTHON\Projects\AI\WhatsApp_Bot\WhatsApp_bot_img\unread.png",0)
# nav_to_img('WhatsApp_bot_img\cancel.png',0)
# nav_to_img('WhatsApp_bot_img\media.png',0)
# nav_to_img('WhatsApp_bot_img\media_1.png',0) #backup_img for media icon
# nav_to_img('WhatsApp_bot_img\copy.png',0)

# nav_to_img(r"WhatsApp_bot_img\unread_light.png",0)
# nav_to_img('WhatsApp_bot_img\media_light.png',0)
# nav_to_img('WhatsApp_bot_img\media_1__light.png',0)
# nav_to_img('WhatsApp_bot_img\cancel_light.png',0)