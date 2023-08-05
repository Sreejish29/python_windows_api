# https://github.com/Sreejish29/python_windows_api

import ctypes

# we are use Ctypes in turn as a proxy to reference whatever API calls we want, that reside inside of user32.dll.
user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

# Setting up parameters for API call
hWnd = None
lpText = "Hello World"
lpCaption = "Message"
uType = 0x00000001

# Catching the response after calling the function.
response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

# Error handling. 
error = k_handle.GetLastError()

if error != 0:
    print(f"Erro Code: {error}")
    exit(1)

# printing message based on the response of user action.
if response == 1:
    print("User clicked Ok!")
elif response == 2:
    print("User clicked Cancel.")
