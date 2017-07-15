'''
Created on Jul 15, 2017

@author: Marley Bob
'''
import os
import sys
import csv
sys.path.append('c:\users\marley bob\anaconda3\lib\site-packages\pyglet-1.3.0b1-py2.7.egg')
import pyglet
import OSC
from OSC import *
import time
import threading, math
import pyglet
from psychopy import visual, core, event
from random import choice

def handler(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    calc_value = (data[1]-data[2])
    to_csv = [time.time()]
#    to_csv.extend(data)
    to_csv.append(calc_value)
    with open('data.csv','a') as f:
        writer = csv.writer(f)
#        writer.writerow(time.time())
        writer.writerow(to_csv)
    print(time.time())
    print(txt)

print("WTF")
if __name__ == "__main__":
    print("WTF")
    os.remove('data.csv')
    s = OSC.OSCServer(('127.0.0.1', 5000))  # listen on localhost, port 57120
    s.addDefaultHandlers()
    s.addMsgHandler('/muse/elements/alpha_absolute', handler)     # call handler() for OSC messages received with the /startup address
    
    mywin = visual.Window([800, 600], monitor="testMonitor", units="deg", fullscr=False)
    targets = []
    potatoes = []
    for f in os.listdir("stim"):
        print(f)
        target = visual.ImageStim(win=mywin, image="stim/" + f)
        targets.append(target)
        
        potato = visual.ImageStim(win=mywin, image = "stim-potato/live-preview-potato.png")
        targets.append(potato)
    
    st = threading.Thread(target = s.serve_forever)
    st.start()
    
    try:
        """image = choice(targets)
        image.draw()
        mywin.flip()
        time.sleep(2)"""
        
        for image in targets:
            """num = 0
            
            with open('data.csv','a') as f:
                writer = csv.writer(f)
#               writer.writerow(time.time())
                writer.writerow([time.time(),num])
            num = num + 1"""
            image.draw()
            mywin.flip()
            time.sleep(2)
    except Exception:
        pass
    s.close()
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from numpy import genfromtxt
    
    data = pd.read_csv('data.csv', names=['x','y'])
    x = data['x']
    y = data['y']
    print(len(x))
    plt.plot(x,y)
    plt.show()
    block = np.pad(y, (0, 10-len(y)%10), mode='constant', constant_values=np.mean(y))
    block = np.split(block, 10)
    even = []
    i = 0
    while (i < 10):
        even.append(np.mean(block[i]))
        i = i+ 2
    i = 1
    odd = []
    while (i < 10):
        odd.append(np.mean(block[i]))
        i = i+ 2
    
    print()
    print(np.mean(even))
    print(np.mean(odd))
        #st.join()