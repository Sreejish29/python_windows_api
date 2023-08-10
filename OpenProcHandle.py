import ctypes

# Creating a handle for Kernel32. 
u_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")



# Creating a all access for our handle. 
PROCESS_ALL_ACCESS = ( 0x00F0000    | 0x00100000    | 0xFFF)

# Setting up all require parameters.
pid = int(input("Enter PID: "))
dwProcessId = ctypes.c_ulong()
dwProcessId = pid
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False

# Storing the response of our Open Process Function. 
proc_hWnd = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)



# Error handling. 
if proc_hWnd <= 0:
    print(f"Erro Code: {k_handle.GetLastError()}. Response code: {proc_hWnd}. Could not grab Privilege Handle.")
    exit(1)
else:
    print("Got the handle!")

