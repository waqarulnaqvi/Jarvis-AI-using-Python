import concurrent.futures
from tkinter import *
from PIL import ImageTk, Image
from subprocess import call #we can call another python program in our program
import datetime#build in module
import speech_recognition as sr # pip install speechRecognition
import pyttsx3 # pip install pyttsx3
import wikipedia# pip install wikepedia
import webbrowser #build in module
from subprocess import call #we can call another python program in our program

# run=1

def script1():
    class GUI_AI(Tk):
        def __init__(self):
            super().__init__()
            my_img1 = ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage1.jpg").resize((700, 700)))
            my_img2 = ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage2.webp").resize((700, 700)))
            my_img3 = ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage3.jpg").resize((700, 700)))
            my_img4 = ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage4.jpg").resize((700, 700)))

            self.imagelist = [my_img1, my_img2, my_img3, my_img4]
            self.i = 0
            self.changeimage()


        def changeimage(self):  # using grid system
            self.bl = Label(self, image=self.imagelist[self.i])
            self.bl.place(x=0, y=0, relwidth=1, relheight=1)

            Label(self, text="What jarvis can do?", relief=SUNKEN, bd=3, borderwidth=3, font="lucida 20 bold",
                  fg="white", bg="green", cursor="man").grid(row=0, column=0, padx=90, pady=20)

            Label(self, text="1)Open youtube", font="lucida 15 bold", fg="white", cursor="spider", bg="red",
                  relief=SUNKEN, bd=3, borderwidth=3).grid(row=1, column=0, padx=5)

            Label(self, text="2)Open linkedin", font="lucida 15 bold", fg="white", cursor="spider", relief=SUNKEN,
                  bg="red", bd=3, borderwidth=3).grid(row=2, column=0, pady=5)

            Label(self, text="3)Open facebook", cursor="spider", relief=SUNKEN, font="lucida 15 bold", fg="white",
                  bg="red", bd=3, borderwidth=3).grid(row=3, column=0, pady=5)

            Label(self, relief=SUNKEN, text="4)Open google", cursor="spider", font="lucida 15 bold", fg="white",
                  bg="red", bd=3, borderwidth=3).grid(row=4, column=0, pady=5)

            Label(self, relief=SUNKEN, text="5)Open stackoverflow", bd=3, cursor="spider", borderwidth=3,
                  font="lucida 15 bold", fg="white", bg="red").grid(row=5, column=0, pady=5)

            Label(self, relief=SUNKEN, text="6)Tell current time", cursor="spider", bd=3, borderwidth=3,
                  font="lucida 15 bold", fg="white", bg="red").grid(row=6, column=0, pady=5)

            Label(self, relief=SUNKEN, text="7)Search in Wikipedia", cursor="spider", bd=3, borderwidth=3,
                  font="lucida 15 bold", fg="white", bg="red").grid(row=7, column=0, pady=5)
            
            Label(self, relief=SUNKEN, text="8)Bye to exit", cursor="spider", bd=3, borderwidth=3, font="lucida 15 bold",
                  fg="white", bg="red").grid(row=8, column=0, pady=5)

            self.i += 1
            if self.i == 4:
                self.i = 0
            self.bl.after(300, self.changeimage)

    if __name__ == "__main__":
        jarvis = GUI_AI()
        jarvis.geometry("500x500")
        jarvis.wm_iconbitmap(r"jarvis images//jarvis.ico")
        jarvis.title("Jarvis A.I")
        # if run == 2:
        #     jarvis.destroy()
        # jarvis.destroy()
        mainloop()

def script2():
    
    engine = pyttsx3.init('sapi5')  # it is used to get voice.
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    class AI:
        # def AI(self):
        # self.open_my_file()

        def open_my_file(self):
            call(["python", "jarvis_GUI.py"])

        def Wishme(self):

            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 5:
                print("Good Night")
                speak("Good Night")
            elif hour >= 5 and hour < 12:
                print("Good Morning")
                speak("Good Morning")
            elif hour >= 12 and hour < 18:
                print("Good Afternoon")
                speak("Good Afternoon")
            else:
                print("Good Evening")
                speak("Good Evening")

            print("I am Jarvis AI,Please tell me how may I help you\n")
            speak("I am Jarvis AI,Please tell me how may I help you")
            # self.open_my_file()


        def takecommand(self):
            # It takes microphone input from the user and returns string output.
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 2
                audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")

            except Exception as e:
                # print(e)
                speak("say that again please..")
                return "None"
            return query

    if __name__ == "__main__":
        jarvis = AI()
        jarvis.Wishme()

        while True:
            query = jarvis.takecommand().lower()
            #     logic for executing tasks based on query
            results = ""
            if "wikipedia" in query:
                speak('Searching Wikipedia...')
                try:
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except:
                    speak(results + " Not found")
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak("Opening youtube by jarvis ai")
            elif 'open linkedin' in query:
                webbrowser.open("linkedin.com")
                speak("Opening linkedin by jarvis ai")
            elif 'open facebook' in query:
                webbrowser.open("facebook.com")
                speak("Opening facebook by jarvis ai")
            elif 'open google' in query:
                webbrowser.open_new_tab("Google.com")
                speak("Opening google by jarvis ai")
            elif 'open stack overflow' in query:
                webbrowser.open_new_tab("stackoverflow.com")
                speak("Opening stackoverflow by jarvis ai")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S:")
                day = datetime.datetime.now().strftime(":%a")
                print(f"Sir, The time is {strTime} and Day is {day}")
                speak(f"Sir, The time is {strTime} and Day is {day}")

            elif "bye" in query:
                print("Thank you sir IT'S MY HONOUR TO HELP YOU!")
                speak("Thank you sir IT'S MY HONOUR TO HELP YOU!")
                # global run
                # run=2
                exit()
   
        
if __name__ == "__main__":
    # Using ThreadPoolExecutor to run scripts concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submitting the functions to the executor
        future1 = executor.submit(script1)
        future2 = executor.submit(script2)

        # Wait for both scripts to complete
        concurrent.futures.wait([future1, future2])

        # Accessing the result of each script (if needed)
        result1 = future1.result()
        result2 = future2.result()

          
        

    