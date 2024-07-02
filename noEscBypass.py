import r2pipe
import time

# launch the ios application
r = r2pipe.open("frida://spawn/usb//com.mobilehackinglab.No-Escape")

def patch_instruction(address):
    r.cmd(f"s {address}")
    r.cmd("wa mov w0, 0")

print("## Bypassing mov & tbz instructions")

mov_output = r.cmd('s `:iE~+jail[0]`; pd~mov[1]]').splitlines()
mov_addresses = [line.split()[0] for line in mov_output]

tbz_output = r.cmd('s `:iE~+jail[0]`; pd~tbz[1]').splitlines()
tbz_addresses = [line.split()[0] for line in tbz_output]
# Patch 'tbz' instructions
for addr in tbz_addresses:
    patch_instruction(addr)

# Patch 'mov w0, 1' instructions
for addr in mov_addresses:
    patch_instruction(addr)

# continue
print("No Escape successfully bypassed")
r.cmd(':dc')

# sleep the application
time.sleep(10000)
