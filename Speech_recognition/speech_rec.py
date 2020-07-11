import speech_recognition as sr



r=sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print('speak Anything :')
        audio=r.listen(source)

        try:
            text=r.recognize_google(audio)
            print('here is your text: {}'.format(text))
        except:
            print('Sorry could not recognise')
        print("Quit:y/n")
        x=input()
        if x=='y' or x=='Y':
            break
        else:
            continue