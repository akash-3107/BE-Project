from paramiko import SSHClient, AutoAddPolicy
import pyttsx3
import sys
voiceEngine = pyttsx3.init()
 
rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')

voiceEngine.setProperty('rate', 150)
newVolume = 0.1
e=pyttsx3.init()
str1=" Detected"
def Connect(ip, username='pi', pw='raspberry'): 
    '''ssh into the pi'''
    print('connecting to {}@{}...'.format(username, ip))
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(ip, username=username, password=pw)
    print('connection status =', ssh.get_transport().is_active())
    return ssh

def SendCommand(ssh, command, pw='raspberry'):
    '''send a terminal/bash command to the ssh'ed-into machine '''
    print('sending a command... ', command)
    stdin, stdout, stderr = ssh.exec_command( command )
    if "sudo" in command:
        stdin.write(pw+'\n')
    stdin.flush()
    #print('\nstout:',stdout.read().decode('ascii').strip("\n"))
    #print('\nsterr:',stderr.read())
    output=stdout.read().decode('ascii').strip("\n")
    #print(output)
    #ret=stdout.readlines()
    #ret=stdout.read().decode('ascii').strip("\n")
    #ret=sys.stdout
    #print(ret+"hi")
    #print(type(ret))
    #print(type(stdout.read().decode('ascii').strip("\n")))
    #print(type(str1))
    #print (output == "Detected")
    #e.say(ret)
    #e.runAndWait()
    if output == "AlcoholDetected":
    	voiceEngine.say("AlcoholDetected")
    	voiceEngine.runAndWait()
    elif output == "SmokeDetected":
    	voiceEngine.say("SmokeDetected")
    	voiceEngine.runAndWait()
    elif output == "HotBody":
    	voiceEngine.say("contact established It is a hot body")
    	voiceEngine.runAndWait()
    elif output == "ColdBody":
    	voiceEngine.say("contact established It is a cold body")
    	voiceEngine.runAndWait()
    elif output == "NormalBody":
    	voiceEngine.say("contact established The body has normal temperature")
    	voiceEngine.runAndWait()
    else:
    	voiceEngine.say("Please give some input")
    	voiceEngine.runAndWait()
myssh = Connect(ip='172.20.10.2')
while True:
	SendCommand(myssh, command='python3 ~/all.py') 
