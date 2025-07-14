# patch 2
import r2pipe
import time

# launch the android application
r = r2pipe.open("frida://spawn/usb//com.8ksec.FridaInTheMiddle")

# seek to func location - emulate - analyze func
r.cmd('s `:il~+debug[0]`; s `:iE~+canary[0]`; e anal.slow = false; e anal.nopskip = true; e emu.str = true; afr.; afna.')

# sleep 1
time.sleep(2)

# locate tbz instruction and nop
r.cmd('wao nop @ `pdr.~+tbz[1]`')
r.cmd(':dc')

# sleep the application
time.sleep(10000)
