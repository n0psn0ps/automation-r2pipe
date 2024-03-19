import r2pipe
import time

# launch the iOS DVIA Objective C application https://github.com/prateek147/DVIA
r = r2pipe.open("frida://launch/usb//DVIA")

# Bypass Application Patching checks
# Login Bypass 
r.cmd("s `:ic ApplicationPatchingDetailsVC~+loginMethod[0]`; aaaf")
r.cmd("wx 00 @ `pdr~cbz w0[1]`;wx 00 @ `pdr~cbz w23[1]`") 
print("[X] Application Patching login function now bypassed.\n")

# Jailbreak bypass 
r.cmd(':di0 `:ic NSFileManager~+fileExistsAtPath:[0]`')

# String overwrite bypass
r.cmd("s `:/ I love Google ~+google[0]`; w n0ps was here")
print("[X] Application Patching overwrite string.\n")

# Kill app bypass
r.cmd(":di0 `:ic ApplicationPatchingDetailsVC~+kill[0]`")
print("[X] Application Patching kill app function now bypassed.\n")

# sleep the application
time.sleep(10000)
