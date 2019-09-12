from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
import tkinter
import urllib
import re
import wget
import time
import platform

the_OS = platform.system()
keyboard = Controller()
the_list_of_urls = []


# http://omz-software.com/pythonista/docs/ios/clipboard.html
# https://pywinauto.readthedocs.io/en/latest/index.html
# https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
# http://docs.activestate.com/activepython/2.5/pywin32/win32clipboard.html


def please_input_url():
    the_chosen_url = input("\n----\n\nPlease input instagram url: ")
    number_of_iterations = int(input("\nHow many picture do you want to download: "))
    return the_chosen_url, number_of_iterations


def get_tree(url):
    source = urllib.request.urlopen(url).read()
    tree = BeautifulSoup(source, "html.parser")
    return tree


def get_data_from_div(soup):
    string_with_data = ""
    for t in soup.findAll("script", {"type": "text/javascript"}):
        temp_text = t.text
        temp_text = temp_text.replace("\n", "")
        temp_text = temp_text.replace(" ", "")
        string_with_data += temp_text

    return string_with_data


def remove_everything_including_this(data, there=re.compile(re.escape('u0026') + '.*')):
    return there.sub('', data)


def clean_up_data(string_with_data):
    teh_text = string_with_data
    remove_everything_before = re.sub('^(.*)(?=[0-9]},{"src":")', "", teh_text)
    clean_text = remove_everything_including_this(remove_everything_before)
    clean_text = re.sub('[0-9]},{"src":"', '', clean_text)
    clean_text = clean_text[:-1]

    return(clean_text)


def pick_up_the_pic(the_url):
    wget.download(the_url)


def copy_url_of_next_pic():
    if the_OS == "Windows":
        with keyboard.pressed(Key.ctrl):
            keyboard.press("l")
            keyboard.release("l")

            time.sleep(0.14)

            with keyboard.pressed(Key.ctrl):
                keyboard.press("c")
                keyboard.release("c")

    elif the_OS == "Darwin":
        with keyboard.pressed(Key.cmd):
            keyboard.press("l")
            keyboard.release("l")

        time.sleep(0.14)

        with keyboard.pressed(Key.cmd):
            keyboard.press("c")
            keyboard.release("c")

    the_copied_url = tkinter.Tk().clipboard_get()

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    return(the_copied_url)


def next_pls():
    keyboard.press(Key.right)
    keyboard.release(Key.right)


def get_the_picture(user_url):
    tree = get_tree(user_url)
    sorted_tree = get_data_from_div(tree)
    the_url_of_pic = clean_up_data(sorted_tree)
    copy_url_of_next_pic()


def get_the_picture(user_url):
    tree = get_tree(user_url)
    sorted_tree = get_data_from_div(tree)
    the_url_of_pic = clean_up_data(sorted_tree)
    the_list_of_urls.append(the_url_of_pic)


def download_the_picture(the_url):
    tree = get_tree(the_url)
    sorted_tree = get_data_from_div(tree)
    the_url_of_pic = clean_up_data(sorted_tree)
    wget.download(the_url_of_pic)


def move_to_next_pic_and_copy_url(number_of_iterations):
    for iterations in range(number_of_iterations):
        the_next_url = copy_url_of_next_pic()
        get_the_picture(the_next_url)
        next_pls()


def download_from_list(the_list):
    for item in the_list:
        wget.download(item)

def main():
    the_chosen_url, number_of_iterations = please_input_url()
    print("Go to browser with active Instagram tab and leave it open during execution.")
    time.sleep(0.5)      # during this time, make Instagram tab active in webbrowser

    start_time = time.time()

    get_the_picture(the_chosen_url)
    next_pls()
    move_to_next_pic_and_copy_url(number_of_iterations)
    # print("\ngood print for debugging\n", the_list_of_urls, "\ngood print for debugging\n")
    the_list_of_urls.pop(0)
    download_from_list(the_list_of_urls)

    print("\n\n[ ---- Completed in: ---- ]\n \t %s seconds" % round(time.time() - start_time, 2))


if __name__ == '__main__':
    main()
