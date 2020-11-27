import socket
import ssl
import threading
import sys
import ctypes

from ctypes import wintypes
from prompt_toolkit import prompt
from prompt_toolkit.patch_stdout import patch_stdout

import console_flash as cf

sock = ssl.wrap_socket(socket.socket(), ca_certs="certs/cert.crt")
PING = 0.01


kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

kernel32.GetConsoleWindow.restype = wintypes.HWND
user32.FlashWindowEx.argtypes = (ctypes.POINTER(cf.FLASHWINFO),)


def flash_console_icon(count=5):
    hwnd = kernel32.GetConsoleWindow()
    if not hwnd:
        raise ctypes.WinError(ctypes.get_last_error())
    winfo = cf.FLASHWINFO(hwnd, count=count)
    previous_state = user32.FlashWindowEx(ctypes.byref(winfo))
    return previous_state


def connect_to_chat():
    hostname = input("(Server?): ")
    try:
        sock.connect((hostname, 7112))
    except socket.gaierror:
        print("Can't connect")
        connect_to_chat()
    except ConnectionRefusedError:
        print("Connection refused")
        connect_to_chat()


connect_to_chat()

nick = input("Введи свой ник: ")
sock.send(nick.encode())

    
def wait_chat():
    while True:
        msg = sock.recv(1024)
        print(f"\r{msg.decode()}")
        flash_console_icon()


t2 = threading.Thread(target=wait_chat, args=())
t2.start()


while True:
    with patch_stdout():
        my_msg = prompt('Me: ')
    if my_msg == "":
        print("Сообщнеие не может быть пустым")
        continue
    sock.send(my_msg.encode())




