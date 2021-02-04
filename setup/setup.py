import sys
import subprocess
import pathlib

l=['requests','pyttsx3','wikipedia','ecapture','wolframalpha',
'SpeechRecognition','winshell','pywin32','youtube-search-python']
for i in range (len(l)):
    subprocess.check_call([sys.executable, "-m", "pip", "install", l[i]])
