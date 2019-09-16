import time
import sys
import os


animation = "|/-\\"

for n in range(100):
    for i in range(6):
        sys.stdout.write("\r\n" + animation[n % len(animation)])
        sys.stdout.flush()
    time.sleep(0.5)
    os.system('clear')
print("End!")
