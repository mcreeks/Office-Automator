
from time import sleep     # Import sleep Library
import RPi.GPIO as GPIO    # Import GPIO Library
GPIO.setmode(GPIO.BOARD)   # Use Physical Pin Numbering Scheme
button1=18                 # Button 1 is connected to physical pin 16
button2=16                 # Button 2 is connected to physical pin 12
button3=12
LED1=26                    # LED 1 is connected to physical pin 22
LED2=24                    # LED 2 is connected to physical pin 18
LED3=22
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button1 an input, Activate Pull UP Resistor
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 2 an input, Activate Pull Up Resistor
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 3 an input, Activate Pull Up Resistor
GPIO.setup(LED1,GPIO.OUT,) # Make LED 1 an Output
GPIO.setup(LED2,GPIO.OUT)  # Make LED 2 an Output
GPIO.setup(LED3,GPIO.OUT)  # Make LED 3 an Output
BS1=False                  # Set Flag BS1 to indicate LED is initially off
BS2=False                  # Set Flag BS2 to indicate LED is initially off
BS3=False                  # Set Flag BS3 to indicate LED is initially off
while(1):                  # Create an infinite Loop
        if GPIO.input(button1)==0:            # Look for button 1 press
                print("Button 1 Was Pressed:")
                if BS1==False:                # If the LED is off
                        GPIO.output(LED1,True)# turn it on
                        BS1=True              # Set Flag to show LED1 is now On
                        sleep(.5)             # Delay
                else:                         # If the LED is on
                        GPIO.output(LED1,False) # Turn LED off
                        BS1=False               # Set Flag to show LED1 is now Off
                        sleep(.5)
        if GPIO.input(button2)==0: #Repeat above for LED 2 and button 2
                print("Button 2 Was Pressed:")
                if BS2==False:
                        GPIO.output(LED2,True)
                        BS2=True
                        sleep(.5)
                else:
                        GPIO.output(LED2,False)
                        BS2=False
                        sleep(.5)
        if GPIO.input(button3)==0: #Repeat above for LED 3 and button 3
                print("Button 3 Was Pressed:")
                if BS3==False:
                        GPIO.output(LED3,True)
                        BS3=True
                        sleep(.5)
                else:
                        GPIO.output(LED3,False)
                        BS3=False
                        sleep(.5)
