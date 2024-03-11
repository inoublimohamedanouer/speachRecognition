import speech_recognition as sr

# Create a recognizer instance
recognizer = sr.Recognizer()

# Use the microphone as audio source
with sr.Microphone() as source:
    print("Speak something:")
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)
    print("You said:", text)

