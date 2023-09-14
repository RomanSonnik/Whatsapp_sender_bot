import csv
import re
import time
import pyautogui
import keyboard
import subprocess
import sys
import os


def on_key_event(event):
    if event.name == 'r' and event.event_type == keyboard.KEY_DOWN:
        print("Exiting")
        subprocess.call(['script.bat'])


def first_setup(FirstSetup):
    while not FirstSetup:
        try:
            from settings import x1, x2, x3, x4, y1, y2, y3, y4, Settings_imported
            print(Settings_imported)
            FirstSetup = True
        except ModuleNotFoundError:
            print('File not found, running first setup!')
            msg_ask = input("Type your message here:")
            with open('settings.py', 'w', encoding='utf-8') as file:
                file.write('# System settings, edit carefully\n')
                file.write('\n')
                file.write('import pyautogui # DONT EDIT THIS\n')
                file.write(f'msg_text = \'{msg_ask}\' # Message text\n')
                file.write('Settings_imported = "Settings imported successful!" #Service setting\n')
                print('Creating settings file completed!')
                print('Lets continue first setup!')
                print('Choose point for browser icon in taskbar!')
                print('When you are redy just press RIGHT SHIFT button')
                keyboard.wait("right shift")
                coordinates = str(pyautogui.position())
                cleaned_string = coordinates.strip('()')
                cleaned_string = re.sub(r'[^0-9, ]', '', cleaned_string)
                x_str, y_str = cleaned_string.split(', ')
                x = int(x_str)
                y = int(y_str)
                file.write(f'x1, y1 = {x}, {y} # Browser icon coordinates\n')
                print('Point for browser icon set successful!')
                print('Choose point for browser new tab button!')
                print('When you are redy just press RIGHT SHIFT button')
                keyboard.wait("right shift")
                coordinates = str(pyautogui.position())
                cleaned_string = coordinates.strip('()')
                cleaned_string = re.sub(r'[^0-9, ]', '', cleaned_string)
                x_str, y_str = cleaned_string.split(', ')
                x = int(x_str)
                y = int(y_str)
                file.write(f'x3, y3 = {x}, {y} # Browser new tab coordinates\n')
                print('Point for browser new tab button set successful!')
                print('Choose point for browser close 1 tab button!')
                print('When you are redy just press RIGHT SHIFT button')
                keyboard.wait("right shift")
                coordinates = str(pyautogui.position())
                cleaned_string = coordinates.strip('()')
                cleaned_string = re.sub(r'[^0-9, ]', '', cleaned_string)
                x_str, y_str = cleaned_string.split(', ')
                x = int(x_str)
                y = int(y_str)
                file.write(f'x2, y2 = {x}, {y} # Browser close 1-st tab coordinates\n')
                print('Point for browser close 1 tab button set successful!')
                print('Choose point for whatsapp type message text box!')
                print('When you are redy just press RIGHT SHIFT button')
                keyboard.wait("right shift")
                coordinates = str(pyautogui.position())
                cleaned_string = coordinates.strip('()')
                cleaned_string = re.sub(r'[^0-9, ]', '', cleaned_string)
                x_str, y_str = cleaned_string.split(', ')
                x = int(x_str)
                y = int(y_str)
                file.write(f'x4, y4 = {x}, {y} # Whatsapp type message text box coordinates\n')
                print('Point for whatsapp type message text box set successful!')
                file.write('Custom_csv_file_name = "numbers.csv"\n')
                print('First setup complete!')


def select_mode():
    print(
        "-----------------------------------------------------------Select option-------------------------------------------------------------")
    mode = input(
        "1 - start script                  2 - Rerun first setup                          3 - Check database                          4 - quit\n")
    print(mode)
    mode_new = re.findall(r'\d+', mode)
    mode = ''.join(mode_new)
    mode = int(mode)
    return mode

first_setup(False)
mode_gl = select_mode()
while mode_gl > 0:
    if mode_gl == 1:
        try:
            from settings import x1, x2, x3, x4, y1, y2, y3, y4, Settings_imported, Custom_csv_file_name, msg_text
            with open(Custom_csv_file_name, 'r') as csvfile:
                time.sleep(5)
                keyboard.hook(on_key_event)
                csvreader = csv.reader(csvfile)
                pyautogui.moveTo(x1, y1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x3, y3)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x2, y2)
                pyautogui.click()
                for row in csvreader:
                    try:
                        row = str(row[0])
                        temp = re.sub(r'[^0-9+]', '', row)
                        time.sleep(1)
                        temp2 = 'https://wa.me/' + temp
                        time.sleep(1)
                        keyboard.write(temp2)
                        time.sleep(1)
                        pyautogui.press('enter')
                        time.sleep(10)
                        pyautogui.moveTo(x4, y4)
                        pyautogui.click()
                        time.sleep(1)
                        keyboard.write(msg_text)
                        time.sleep(5)
                        pyautogui.press('enter')
                        time.sleep(1)
                        pyautogui.moveTo(x1, y1)
                        pyautogui.click()
                        time.sleep(1)
                        pyautogui.moveTo(x3, y3)
                        pyautogui.click()
                        time.sleep(1)
                        pyautogui.moveTo(x2, y2)
                        pyautogui.click()
                    except IndexError:
                        pass
        except FileNotFoundError:
            print('[ERROR] File not found error')
            input("")
        select_mode()
        mode_gl = select_mode()
    elif mode_gl == 2:
        try:
            os.remove('settings.py')
            time.sleep(5)
            #first_setup(False)
        except FileNotFoundError:
            pass
        subprocess.run('main.exe')
        subprocess.call(['script.bat'])

    elif mode_gl == 3:
        print("[INFO] Checking database")
        try:
            from settings import x1, x2, x3, x4, y1, y2, y3, y4, Settings_imported, Custom_csv_file_name, msg_text
            with open(Custom_csv_file_name, 'r') as csvfile:
                csvreader1 = csv.reader(csvfile)
                print('[INFO] Printing all database numbers\n')
                for row1 in csvreader1:
                    try:
                        row1 = str(row1[0])
                        temp1 = re.sub(r'[^0-9+]', '', row1)
                        print(row1)
                    except IndexError:
                        pass
        except FileNotFoundError:
            print('[ERROR] File not found')
            input("")
        select_mode()
        mode_gl = select_mode()
    elif mode_gl == 4:
        mode_gl = select_mode()
        sys.exit(0)
    else:
        print('[ERROR] Unknown mode, please retry')
        print(mode_gl)
        input('')
        select_mode()
        mode_gl = select_mode()
