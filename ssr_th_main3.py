import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep
import os

gpio=[11,12,13,15,16,18]
pin_id=[]
for i in range(0,len(gpio)):
  pin_id.append(str(gpio[i]))
path=[]
for i in range(0,len(gpio)):
  path.append('./go'+pin_id[i]+'.txt')
#  print(path[i])
#exit()
ton=[1,1,1,1,1,1]
toff=[1,1,1,1,1,1]
qu=[]
for i in range(0,len(gpio)):
  qu.append(queue.Queue())
#  print(qu[i])
#exit()
#
th=[]
for i in range(0,len(gpio)):
  th.append("")
while True:
  try:
    if threading.active_count()==len(gpio):
      continue
    elif threading.active_count()<len(gpio):
      for i in range(0,len(gpio)):
        is_file=os.path.isfile(path[i])
        if is_file:
          th[i]=threading.Thread(target=ssr,args=(gpio[i],ton[i],toff[i],qu[i]),name=pin_id[i],daemon=True)
          th[i].start()
          print(th[i].name)
    else:
       continue
#       print("go??.txt not found")
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    GPIO.cleanup()
    exit()
