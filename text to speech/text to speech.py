from gtts import gTTS
import playsound
import pyperclip
text=pyperclip.paste()
text=str(text)
audio=gTTS(text)
audio.save('temp2.mp3')
playsound.playsound('temp2.mp3')