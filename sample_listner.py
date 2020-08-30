#An example of listening to the user command and performs the task accordingly
#A Basic listener using pyhton which helps the user to open C and D drives in pc and makes serache of any word that user speaks
#Some how reduces the manual work of the user,It not a complete project (work in progress)
#It uses speechRecognition,webbrowser,playsound,gtts packages in python. 



import  speech_recognition as sr #giving an alias name as sr just to make simple
import webbrowser as wb #giving the alias name as wb
import playsound as ps
from gtts import gTTS
#initalize the Recoginzer class  which helps to listen to the audio
def speak(text):
    audio=gTTS(text=text,lang='en',slow=False)
    audio.save('temp.mp3')
    ps.playsound('temp.mp3')


r=sr.Recognizer()

def access_my_pc():
    import os
    print('accessing your pc')
    with sr.Microphone() as source:
        print('waiting for the command')
        audio=r.listen(source)
        text = r.recognize_google(audio)
        if text=='open desktop':
            os.startfile(r"Desktop\\")#using the raw string so that it accepts the escape sequences (\\'')etc
        elif text=='open D drive':
            os.startfile(r'D:\\')
        elif text=='open C drive':
            os.startfile(r"C:\\")
        else:
            print('access is denied for other drives')

with sr.Microphone() as source:
    #in the above line we are using the microphone as our source to here the audio
    print('listening')
    #handling if the audio is not audible
    try:
        #using the listen function to listen the audio
        audio=r.listen(source,phrase_time_limit=4)
        text = r.recognize_google(audio)#converting the returned object to text using googes apis
        if text=='access my computer':
            speak('accessing my computer')
            access_my_pc() # calling the function
        elif text=='search in internet':
            speak('query to search')
            audio = r.listen(source,phrase_time_limit=4)
            text = r.recognize_google(audio)
            print(text)
            wb.open(text)#using the open() from the webbrowser package to search or open in the query in internet
        else:
            raise sr.UnknownValueError

    except sr.UnknownValueError:
        print('voice is not audible')
    except sr.RequestError:
        print(' conversion problem,please check your internet connection')



