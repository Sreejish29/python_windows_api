# Process Killer:
'''

1. Firstly, get User and Kernel Handle to interact with Windows API.
2. Get the application's or Window handle using FindWindowA function.
    1) You need to pass Window name as a pointer which will return a reference handle of the currently open Window.
    2) Check if Returned Window Handle is Zero or not.
3. Use the Window Handle to get the Process ID using Fucntion named GetWindowThreadProcessId.
    1) This function takes 2 arguments, a Window Handle and a DWORD type variable which need to be passed as reference.
    2) Make sure to declare the Process ID variable as a DWORD type and then pass it as a reference so the fucntion can update it.
4. Once the function updates Process ID object we need to pass it along with Desired Access and Handle Inheritance (which is a boolean) to OpenProcess Function, 
   which will return us the actual Handle with the Desired Access Token.
5. Then we'll call TerminateProcess Function and pass our Handle and Exit code to terminate the targeted process.

'''



import ctypes

# User and Kernel handle.
u_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")



# Getting Window Handle.
lpClassName = None
lpWindowName = ctypes.c_char_p(input("Enter Window Name to Kill: ").encode('utf-8'))

window_handle = u_handle.FindWindowA(lpClassName, lpWindowName)

if window_handle == 0:
    print(f"Erro Code: {window_handle} Could not grab the handle {k_handle.GetLastError()}")
    exit(1)
else:
    print("Got the Handle...")



# Getting the actual process ID. 
lpdwProcessID = ctypes.c_ulong()

thread_id = u_handle.GetWindowThreadProcessId(window_handle, ctypes.byref(lpdwProcessID))

if thread_id == 0:
    print(f"Erro Code: {k_handle.GetLastError()} Could not grab the PID.")
    exit(1)
else:
    print("Got PID of the Window...")
    


# Getting the process handle. 
PROCESS_ALL_ACCESS = ( 0x00F0000    | 0x00100000    | 0xFFF)

bInheritHandle = False
dwProcessId = lpdwProcessID

proc_hWnd = k_handle.OpenProcess(PROCESS_ALL_ACCESS, bInheritHandle, dwProcessId)

if proc_hWnd <= 0:
    print(f"Erro Code: {k_handle.GetLastError()} Could not grab Privilege Handle.")
    exit(1)
else:
    print("Got the handle!")
    


# Terminate Process
uExitCode = 0x1
response = k_handle.TerminateProcess(proc_hWnd, uExitCode)

if response <= 0:
    print(f"Erro Code: {k_handle.GetLastError()} Could not terminate the process.")
    exit(1)
else:
    print("Process terminated successfully!")












