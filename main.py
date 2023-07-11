import pyperclip
import unicodedata
import time
import keyboard

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

page = ''
page_top = 255
now_index = 0
i = 0

while True:
    i = 0
    while i < page_top:
        if(ord(file_content[now_index]) != 10):
            if Is_CJK(file_content[now_index]):
                i += 1
        page = page + file_content[now_index]
        now_index += 1
        i += 1
    time.sleep(1.5)
    pyperclip.copy(page)
    keyboard.press_and_release('ctrl+v')
    time.sleep(1.5)
    keyboard.press_and_release('PgDn')
    # pyperclip.paste()
    print(page)
    page = ''


# print(file_content)
