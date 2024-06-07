import r2pipe
import time

# launch the iOS DVIA Objective C application https://github.com/prateek147/DVIA
r = r2pipe.open("frida://attach/local//DVIA")
# Jailbreak bypass 1
r.cmd(":di0 `:ic JailbreakDetectionVC~Jailbroken[0]`")
print("[X] Bypass jailbreak check one.\n")

# Jailbreak bypass 2?
#r.cmd(':di0 `:ic NSFileManager~+fileExistsAtPath:[0]`')
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

# iOS check
#r.cmd(":di0 `:ic SFAntiPiracy~+isTheApplicationCracked`; :di0 `:ic SFAntiPiracy~+isTheDeviceJailbroken`; :di0 `:ic SFAntiPiracy~+isTheApplicationTamperedWith`; :di0 `:ic SFAntiPiracy~+urlCheck`; :di0 `:ic SFAntiPiracy~+cydiaCheck`; :di0 `:ic SFAntiPiracy~+inaccessibleFilesCheck`; :di0 `:ic SFAntiPiracy~+plistCheck`; :di0 `:ic SFAntiPiracy~+processesCheck`; :di0 `:ic SFAntiPiracy~+fstabCheck`; :di0 `:ic SFAntiPiracy~+systemCheck`; :di0 `:ic SFAntiPiracy~+symbolicLinkCheck`; :di0 `:ic SFAntiPiracy~+filesExistCheck`; :di0 `:ic SFAntiPiracy~+isPirated`; :di0 `:ic SFAntiPiracy~+isJailbroken`; :di0 `:ic SFAntiPiracy~+killApplication`; :di0 `:ic SFAntiPiracy~+runningProcesses`")

# sleep the application
time.sleep(10000)
