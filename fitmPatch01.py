# patch 1
import r2pipe
import time

# launch the iOS application
r = r2pipe.open("frida://spawn/usb//com.8ksec.FridaInTheMiddle")

# seek to function addr 
r.cmd('s `:il~+debug[0]`;:di0 `:iE~+canary[0]`')

# sleep the application
time.sleep(10000)
