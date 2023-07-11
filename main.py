import pyperclip
import unicodedata
import time
from pynput import keyboard
import os

def Is_CJK(char):
    # print(unicodedata.name(char))
    if 'CJK' or 'IDEOGRAPHIC' or 'FULLWIDTH' in unicodedata.name(char):
        # print(1)
        return True
    else:
        return False


file_name = 'text.txt'

try:
    with open(file_name, encoding='utf-8') as file_obj:
        file_content = ''
        chunk = 100
        while True:
            content = file_obj.read(chunk)
            if not content:
                break
            file_content += content
except FileNotFoundError:
    print(f'{file_name} Not Found!')

control = keyboard.Controller()

print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print('Begin!')

page = ''
page_top = 255
now_index = 0
i = 0

while True:
    i = 0
    while i < page_top:
        try:
            if(ord(file_content[now_index]) != 10):
                if Is_CJK(file_content[now_index]):
                    i += 1
        except IndexError:
            print('May be your text is too short or the text is ending, please copy it manually.')
            os._exit(1)
        page = page + file_content[now_index]
        now_index += 1
        i += 1
    time.sleep(1.5)
    pyperclip.copy(page)
    
    with control.pressed(keyboard.Key.ctrl):
        control.press('v')
        control.release('v')
    time.sleep(1.5)
    control.press(keyboard.Key.page_down)
    control.release(keyboard.Key.page_down)
    time.sleep(0.5)
    # print(page)
    page = ''
