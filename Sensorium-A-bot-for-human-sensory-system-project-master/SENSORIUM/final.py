import speech_recognition as sr
import nltk
import os
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
#from nltk.corpus import state_union
from nltk.tree import Tree
import pyttsx3
voiceEngine = pyttsx3.init()
 
rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')

voiceEngine.setProperty('rate', 125)
newVolume = 0.1

voiceEngine.say("Hello everyone Sensorium at your service!")
voiceEngine.runAndWait()

voiceEngine.say("How can I help you?")
voiceEngine.runAndWait()


flag1=flag2=flag3=flag4=flag5=flag6=flag7=0


r=sr.Recognizer()
while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print ('Say something:')
		audio=r.listen(source)

	#train_text =("What is colour and shape")
	try:
		train_text=r.recognize_google(audio)

	except:
		pass



	Stopwords=['i','me','my','myself','we','our','ours','ourselves','you','the','and',"you're","you've","you'll","you'd",'your','yours','yourself','yourselves','he','him','his','himself','she',"she's",'her','hers','herself','it',"it's",'its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that',"that'll",'these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don',"don't",'should',"should've",'now','d','ll','m','o','re','ve','y','ain','aren',"aren't",'couldn',"couldn't",'didn',"didn't",'doesn',"doesn't",'hadn',"hadn't",'hasn',"hasn't",'haven',"haven't",'isn',"isn't",'ma','mightn',"mightn't",'mustn',"mustn't",'needn',"needn't",'shan',"shan't",'shouldn',"shouldn't",'wasn',"wasn't",'weren',"weren't",'won',"won't",'wouldn',"wouldn't"]

	myset=set(('what','which','is'))
	stopnew = set(Stopwords)-myset

	words1 = word_tokenize(train_text)
	filsent = []
	keyword = []
	for w in words1:
		if w not in stopnew:
			filsent.append(w)
	print (filsent)
	k="is"
	exclud = []
	exclud.append(k)
	print(exclud)
	if filsent[0] in exclud:
		#keyword.append(filsent)
		keyword = set(filsent)
	
	else:
		keyword = set(filsent) - set(exclud)
	
	print (keyword)

	for i in keyword:
		if(i in ('what')):
			flag1=1
		if(i in ('image')):
			flag2=1
		if(i in ('object')):
			flag3=1
		if(i in ('smell')):
			flag4=1
		if(i in ('is')):
			flag5=1
		if(i in ('contact')):
			flag6=1

		if(i in ('exit')):
			flag7=1

	if(flag1==1 and flag2==1 or flag3==1):
		print("Image")
		os.system('python3 ~/tensorflow-for-poets-2/tf_files/cam.py ')
		flag1=flag2=flag3=0

	if(flag1==1 and flag4==1):
		print("Smell")
		os.system('python3 connect.py')
		flag1=flag4=0

	if(flag5==1 and flag6==1):
		print("Touch")
		os.system('python3 connect1.py')
		flag5=flag6=0

	if(flag7==1):
		break

	

'''
str1=''.join(keyword)

out_text = PunktSentenceTokenizer(str1)

tk = out_text.tokenize(str1)
'''
	


