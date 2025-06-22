import pyautogui 
import serial 
import time
import threading



xspeed=0
yspeed=0

package=[]
cleaned_data=[]
"""
This function run parallel with while loop
Base on the frame received from mpu, we move or drag the mouse or stay at current position. 
"""
def mouse_thread():
    global xspeed
    global yspeed
    global cleaned_data
    while True:
        try:
            if cleaned_data[0]=='m':
                pyautogui.moveRel(xOffset=xspeed,yOffset=yspeed)
            elif cleaned_data[0]=='d':
                pyautogui.dragRel(xOffset=xspeed,yOffset=yspeed)
        except:
            pass     
        print(pyautogui.position())

"""
Open serial port with connect to bluetooth
If we fail, we will try multiple time until we can open the serial port 
"""
while True:
    try:
        ser=serial.Serial("COM13",baudrate=9600,timeout=1)
        if ser.is_open==True:
            thread1=threading.Thread(target=mouse_thread)
            thread1.daemon=True
            thread1.start()
            break
    except Exception as e:
        print(e)
"""
while loop
Receive frame from MCU, determine the speed of the mouse
"""
while(True):
    try:
        if(ser.is_open==True):
            data=ser.readline().decode('utf-8')
            package=data.split('/')
            cleaned_data = [item.replace('\x00', '').strip() for item in package]
            print(cleaned_data)
            roll=int(cleaned_data[1])
            pitch=int(cleaned_data[2])
            if roll>30:
                xspeed=-10
            elif roll<-30:
                xspeed=10
            else:
                xspeed=0
            if pitch>30:
                yspeed=10
            elif pitch<-30:
                yspeed=-10
            else:
                yspeed=0
        else:        
            xspeed=0
            yspeed=0
            try:
                ser=serial.Serial("COM13",baudrate=9600,timeout=1)
                print('Ngu')
            except Exception as e:
               print(e) 
    except:
        pass
        

            
    


