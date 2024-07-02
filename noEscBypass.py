import r2pipe
import time

# launch the ios application
r = r2pipe.open("frida://spawn/usb//com.mobilehackinglab.No-Escape")

# mov overwrite
print("## Bypassing mov instructions")
r.cmd('s `:iE~+jail[0]`');
mov = r.cmd('pd~mov[1]');
arMov = mov.split();
r.cmd('s ' + arMov[0] + '; wx 00008052; s ' + arMov[1] + '; wx 00008052; s ' + arMov[2] + '; wx 00008052');

# tbz overwrite  
print("## Bypassing tbz instructions")
r.cmd('s `:iE~+jail[0]`');
tbz = r.cmd('pd~tbz[1]');
arTbz = tbz.split();
r.cmd('s ' + arTbz[0] + '; wx 00008052; s ' + arTbz[1] + '; wx 00008052; s ' + arTbz[2] + '; wx 00008052'+ arTbz[3] + '; wx 00008052');

# continue
r.cmd(':dc')

# sleep the application
time.sleep(10000)
