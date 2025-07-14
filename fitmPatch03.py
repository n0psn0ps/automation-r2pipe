#patch 2
import r2pipe
import time

# launch the android application
r = r2pipe.open("frida://spawn/usb//com.8ksec.FridaInTheMiddle")

# split output and store in array
add_output = r.cmd('s `:il~+debug[0]`;s `:iE~+canary[0]`; e anal.slow = false; e anal.nopskip = true; e emu.str = true; afr.; afna.;pdr.~+add[1]').splitlines()

# sleep 
time.sleep(2)

# overwrite second add instruction
r.cmd('wao nop @ ' + add_output[2] +';:dc')

# sleep the application
time.sleep(10000)
