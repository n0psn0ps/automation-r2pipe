import r2pipe
import time

# launch the iOS DVIA Objective C application https://github.com/prateek147/DVIA
r = r2pipe.open("frida://attach/local//DVIA")
# Jailbreak bypass 1
r.cmd(":di0 `:ic JailbreakDetectionVC~Jailbroken[0]`")
print("[X] Bypass jailbreak check one.\n")

# Jailbreak bypass 2
r.cmd("s `:/ bin~bash[0]`; wx 222f787963220a ; s `:/ usr~sbin[0]`; wx 222f787963220a")
print("[X] Bypass jailbreak check two.\n")

# Login Bypass 
r.cmd("s `:ic ApplicationPatchingDetailsVC~+loginMethod[0]`; af")
r.cmd("wx 00 @ `pdr~cbz w0[1]`;wx 00 @ `pdr~cbz w23[1]`") 
print("[X] Application Patching login function now bypassed.\n")

# String overwrite bypass
r.cmd("s `:/ I love Google ~+google[0]`; w n0ps was here")
print("[X] Application Patching overwrite string.\n")

# Kill app bypass
r.cmd(":di0 `:ic ApplicationPatchingDetailsVC~+kill[0]`")
print("[X] Application Patching kill app function now bypassed.\n")

# Bypass Piracy Check
print("[X] Piracy check bypassed.\n")
out = r.cmd(":ic SFAntiPiracy~[2]")

addr = out.split()
for addrs in addr:
    r.cmd(f":di0 `:ic SFAntiPiracy~+{addrs}`")

# sleep the application
time.sleep(10000)
