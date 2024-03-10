import r2pipe
import time

def open_app_with_r2frida(target_app):
        bundle_id = target_app

# launch the android application
r = r2pipe.open(f"frida://launch/usb//com.optiv.ndkcrackme")

# search library, split addr, print address
addr = r.cmd(':dc');
addr = r.cmd(':il~+libnative-lib');
splitAddr = addr.split(" ", 1)[0]

# seek to addr 
r.cmd("s " + splitAddr)
# split function address 
eAddr = r.cmd(':iE~Java_com_optiv_ndkcrackme_MainActivity_b').split(" ", 1)[0]
# dynamic inst at eAddr
r.cmd(':di1 ' + eAddr)
print("[X] Function bypassed. Any password now accepted.")

# sleep the application
time.sleep(10000)

if __name__ == "__main__":
    target_app = "com.optiv.ndkcrackme"  
    open_app_with_r2frida(target_app)
