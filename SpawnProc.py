'''
CreateProcessW function
PROCESS_INFORMATION structure
STARTUPINFOW structure
'''


import ctypes
from ctypes.wintypes import HANDLE, DWORD, LPWSTR, WORD, LPBYTE

# Created a kernel handle.
k_handle = ctypes.WinDLL("Kernel32.dll")


# Created a structure to gain process info.
class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
    ]


# Created a structure to gain startup info of the target application.
class STARTUPINFO(ctypes.Structure):
    _fields_ = [
        ("cb", DWORD),
        ("lpReserved", LPWSTR),
        ("lpDesktop", LPWSTR),
        ("lpTitle", LPWSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE)
    ]


# Setting up parameter to create a process. 
lpApplicationName = "C:\\Windows\\System32\\cmd.exe"
lpCommandLine = None
lpProcessAttributes = None
lpThreadAttributes = None
bInheritHandles = None
lpEnvironment = None
lpCurrentDirectory = None
dwCreationFlags = 0x00000010
lpStartupInfo = STARTUPINFO()
lpProcessInformation = PROCESS_INFORMATION()

lpStartupInfo.wShowWindow = 0x1
lpStartupInfo.dwFlags = 0x1



# Calling the CreateProcess function using Windows API.
response = k_handle.CreateProcessW(
    lpApplicationName,
    lpCommandLine,
    lpProcessAttributes,
    lpThreadAttributes,
    bInheritHandles,
    dwCreationFlags,
    lpEnvironment,
    lpCurrentDirectory,
    ctypes.byref(lpStartupInfo),
    ctypes.byref(lpProcessInformation)
)


# Error handling.
if response > 0:
    print(f"Process is running! PID is {lpProcessInformation.dwProcessId}.")
else:
    print(f"Proc creation failed. Erro Code: {k_handle.GetLastError()}")
    exit(1)
