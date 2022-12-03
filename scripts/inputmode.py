import time
import keyboard
import VoiceRun as vr
from rich import print

def mode_select():
	vr.Speak("please select an input Mode.")
	print("Please Select in wich input Mode you want to Use the Assistant :  ")
	print("1.Press 't' for Text Input Mode\n2.Press 's' for Speech Input Mode ")

	while True : 
		if keyboard.is_pressed('t'):
			print('You have successfully Selected : Text Input Mode')
			vr.Speak("text input Mode Selected.")
			mode_var= 0
			time.sleep(0.6)
			break
		elif keyboard.is_pressed('s'):
			print('You have successfully Selected : Speech Input Mode')
			vr.Speak("speech input Mode Selected.")
			mode_var= 1
			time.sleep(0.6)
			break		    
	return mode_var