import sys
import subprocess
import pathlib
print(str(pathlib.Path().absolute())+'\setup')

l=['requests','pyttsx3','wikipedia','ecapture','wolframalpha',
'SpeechRecognition','winshell','pywin32']
for i in range (len(l)):
    subprocess.check_call([sys.executable, "-m", "pip", "install", l[i]])
