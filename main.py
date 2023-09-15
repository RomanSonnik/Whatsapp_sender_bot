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
        print("[INFO] Exiting")
        subprocess.call(['script.bat'])


def display_csv_with_line_numbers(file_path):
    with open(file_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line_number, row in enumerate(csv_reader, start=1):
            print(f"{line_number}: {', '.join(row)}")


def first_setup(FirstSetup):
    while not FirstSetup:
        try:
            from settings import x1, x2, x3, x4, y1, y2, y3, y4, Settings_imported
            print('[INFO] ', Settings_imported)
            FirstSetup = True
        except ModuleNotFoundError:
            print('[INFO] Settings file not found, running first setup!')
            msg_ask = input("[INFO] Type your message here:")
            with open('settings.py', 'w', encoding='utf-8') as file:
                file.write('# System settings, edit carefully\n')
                file.write('\n')
                file.write('import pyautogui # DONT EDIT THIS\n')
                file.write(f'msg_text = \'{msg_ask}\' # Message text\n')
                file.write('Settings_imported = "Settings imported successful!" #Service setting\n')
                print('[INFO] Creating settings file completed!')
                print('[INFO] Lets continue first setup!')
                print('\n\n\n[INFO] Choose point for browser icon in taskbar!')
                print('[INFO] When you are redy just press RIGHT SHIFT button')
                keyboard.wait("right shift")
                coordinates = str(pyautogui.position())
                cleaned_string = coordinates.strip('()')
                cleaned_string = re.sub(r'[^0-9, ]', '', cleaned_string)
                x_str, y_str = cleaned_string.split(', ')
                x = int(x_str)
                y = int(y_str)
                file.write(f'x1, y1 = {x}, {y} # Browser icon coordinates\n')
                print('\n\n\n[INFO] Point for browser icon set successful!')
                print('[INFO] Choose point for browser new tab button!')
                print('[INFO] When you are redy just press RIGHT SHIFT button')
                keyboard.wait("right shift")
                coordinates = str(pyautogui.position())
                cleaned_string = coordinates.strip('()')
                cleaned_string = re.sub(r'[^0-9, ]', '', cleaned_string)
                x_str, y_str = cleaned_string.split(', ')
                x = int(x_str)
                y = int(y_str)
                file.write(f'x3, y3 = {x}, {y} # Browser new tab coordinates\n')
                print('\n\n\n[INFO] Point for browser new tab button set successful!')
                print('[INFO] Choose point for browser close 1 tab button!')
                print('[INFO] When you are redy just press RIGHT SHIFT button')
                keyboard.wait("right shift")
                coordinates = str(pyautogui.position())
                cleaned_string = coordinates.strip('()')
                cleaned_string = re.sub(r'[^0-9, ]', '', cleaned_string)
                x_str, y_str = cleaned_string.split(', ')
                x = int(x_str)
                y = int(y_str)
                file.write(f'x2, y2 = {x}, {y} # Browser close 1-st tab coordinates\n')
                print('\n\n\n[INFO] Point for browser close 1 tab button set successful!')
                print('[INFO] Choose point for whatsapp type message text box!')
                print('[INFO] When you are redy just press RIGHT SHIFT button')
                keyboard.wait("right shift")
                coordinates = str(pyautogui.position())
                cleaned_string = coordinates.strip('()')
                cleaned_string = re.sub(r'[^0-9, ]', '', cleaned_string)
                x_str, y_str = cleaned_string.split(', ')
                x = int(x_str)
                y = int(y_str)
                file.write(f'x4, y4 = {x}, {y} # Whatsapp type message text box coordinates\n')
                print('\n\n\n[INFO] Point for whatsapp type message text box set successful!')
                file.write('Custom_csv_file_name = "numbers.csv"\n')
                print('[INFO] First setup complete!')


def filter_input(input_string):
    pattern = r'[\d+]+'
    filtered_values = re.findall(pattern, input_string)
    return ','.join(filtered_values)


def select_mode():
    print(
        "|--------------------------------------------------------------Select option---------------------------------------------------------|")
    print(
        "|1 - start script  2 - Rerun first setup  3 - Add numbers to database  4 - Clear numbers from database  5 - Check database  6 - quit |")
    mode = input(
        "|------------------------------------------------------------------------------------------------------------------------------------|\n")
    mode_new = re.findall(r'\d+', mode)
    mode = ''.join(mode_new)
    mode = int(mode)
    return mode


mode_gl = select_mode()
first_setup(False)
while mode_gl > 0:
    if mode_gl == 1:
        try:
            from settings import x1, x2, x3, x4, y1, y2, y3, y4, Custom_csv_file_name, msg_text
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
        mode_gl = select_mode()
    elif mode_gl == 2:
        try:
            os.remove('settings.py')
            time.sleep(5)
        except FileNotFoundError:
            pass
        subprocess.run('main.exe')
        subprocess.call(['script.bat'])
    elif mode_gl == 5:
        print("[INFO] Checking database file")
        from settings import Custom_csv_file_name
        print(display_csv_with_line_numbers(Custom_csv_file_name))
        mode_gl = select_mode()
    elif mode_gl == 3:
        print("[INFO] Checking database")
        try:
            from settings import Custom_csv_file_name
            with open(Custom_csv_file_name, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                while True:
                    values = input("[INFO] Enter numbers (or enter 'q' for exit editing): ")
                    if values.lower() == 'q':
                        break
                    filtered_values = filter_input(values)
                    if filtered_values:
                        values_list = filtered_values.split(',')
                        csv_writer.writerow(values_list)
        except FileNotFoundError:
            print('[ERROR] File not found')
            input("")
        mode_gl = select_mode()
    elif mode_gl == 4:
        from settings import Custom_csv_file_name
        print(display_csv_with_line_numbers(Custom_csv_file_name))
        lines_to_delete = input("[INFO] Enter row number to delete, or type many of them separating with a comma\n")
        lines_to_delete = [int(line) for line in lines_to_delete.split(',')]
        rows_to_keep = []
        with open(Custom_csv_file_name, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line_number, row in enumerate(csv_reader, start=1):
                if line_number not in lines_to_delete:
                    rows_to_keep.append(row)
        with open(Custom_csv_file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(rows_to_keep)
        print(display_csv_with_line_numbers(Custom_csv_file_name))
        mode_gl = select_mode()
    elif mode_gl == 6:
        sys.exit(0)
    else:
        print('[ERROR] Unknown mode, please retry')
        mode_gl = select_mode()
        pass
