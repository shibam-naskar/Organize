import time
import sys

def progressbar(total,current):
    percent = (current/total)*100
    sys.stdout.write("\r[{0:50s}] {1:.1f}%".format('#'*int(percent/2),percent))
    sys.stdout.flush()


for i in range(200):
    progressbar(200,i)
    time.sleep(0.1)
    
