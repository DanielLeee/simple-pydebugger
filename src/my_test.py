import my_debugger
from my_debugger_defines import *

debugger = my_debugger.debugger()

pid = input("Enter the PID of the process to attach to: ")

debugger.attach(int(pid))

printf_address = debugger.func_resolve(b"msvcrt.dll", b"printf")

print("[*] Address of printf: 0x%08x" % printf_address)

debugger.bp_set_mem(printf_address, 10)

debugger.run()

# debugger.detach()