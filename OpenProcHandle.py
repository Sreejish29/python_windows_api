import ctypes

# Creating a handle for Kernel32. 
k_handle = ctypes.WinDLL("Kernel32.dll")

# Creating a all access for our handle. 
PROCESS_ALL_ACCESS = ( 0x00F0000    | 0x00100000    | 0xFFF)

# Setting up all require parameters.
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = 0x1DD0 #0x1C9C

#print(dwProcessId, type(dwProcessId))

# Storing the response of our Open Process Function. 
response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)


# Error handling. 
error = k_handle.GetLastError()

if error != 0:
    print(f"Erro Code: {error}")
    exit(1)

# Checking if our response code after calling Open Process Function. 
if response <= 0:
    print("Handle was not created.")
else:
    print(f"Handle was Created! {response}")
