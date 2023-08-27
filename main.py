# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr


# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    return Query


# creating Speak() function to giving Speaking power
# to our voice assistant 
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()


# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        if "okay" or "thank you" or "exit" in command:
            Speak("Sure! Have a nice day, bye")
            break
        if "hello" in command:
            Speak("Hello ! What you want to know about CodeClause")
        if "internship" in command:
            Speak("Virtual Internship Program in emerging technologies with CodeClause. Get Certified, Trained by Experts, Explore Opportunities, Gain Experience.")
        if "do" in command:
            Speak("At CodeClause, we have experience helping our customers solve key business challenges to achieve their goals with solutions in real-world applications. Find your path to faster success.")