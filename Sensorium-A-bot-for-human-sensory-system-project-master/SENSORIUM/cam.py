import cv2
import os
import pyttsx3
import speech_recognition as sr
e=pyttsx3.init()
rate = e.getProperty('rate')
e.setProperty('rate', 100)
#e.say("Please show the image")

def show_webcam(mirror=False):
	cam = cv2.VideoCapture(0)
	while True:
		ret_val, img = cam.read()
		if mirror: 
			img = cv2.flip(img, 1)
		cv2.imshow('my webcam', img)
		
		e.say("Is this the image")
		e.runAndWait()
		r=sr.Recognizer()
		with sr.Microphone() as source:
			print('Say Something:')
			audio=r.listen(source)
		#try:
		#print ('text='+r.recognize_google(audio))			
		ret=r.recognize_google(audio)
		print ('text=' +ret)
		if ret in ('yes') :
			cv2.imwrite("test.jpg",img) # writes im
			e.runAndWait()
			os.system('cp test.jpg ~/tensorflow-for-poets-2/tf_files')
			os.system('python3 ~/tensorflow-for-poets-2/tf_files/label_image.py ~/tensorflow-for-poets-2/tf_files/test.jpg')
			break
		else :
			e.say("Please show some image")		
		#except:
			#pass
				
		#v2.imshow("Test Picture", img) # displays captured image
		
		#if cv2.waitKey(1) == 27: 
		#	break  # esc to quit
	cv2.destroyAllWindows()

def main():
	show_webcam(mirror=True)

main()
