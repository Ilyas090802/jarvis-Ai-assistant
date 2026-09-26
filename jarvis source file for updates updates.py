import pyttsx3 #pip install pyttsx3 #pip install pyaudio
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import smtplib
import re
from locd import address_of_command
#from word2number import w2n

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def msgencoder():
        while True:
            encode_or_decode = input("\nEncode a massage or Decode a massage OR Q to quit: ")
            if "q" in encode_or_decode.lower():
                break
            massage = input("\nEnter the massage: ")

            #encodeing section
            if "encode" in encode_or_decode.lower():
    
    
                if(len(massage)<=3):
                    encode_of_3_characters = massage[::-1]    
                    massage = encode_of_3_characters
                    print(f"The code of massage is {massage}")
    
                else:
                    key_for_massage = input("Enter key for you massage of 4 latters: ")
                    while len(key_for_massage) > 4:
                        print("The encoder support key of 4 only.")
                        key_for_massage = input("Try again: ")
                    massage = massage[len(massage)-3:] + massage[:len(massage)-3]
                    massage = re.sub( " ", "💀", massage)
                    massage = re.sub( "a", "😊", massage)
                    massage = re.sub( "b", "😶", massage)
                    massage = re.sub( "c", "🙄", massage)
                    massage = re.sub( "k", "🫥", massage)
                    massage = re.sub( "i", "🤐", massage)
                    massage = re.sub( "l", "😯", massage)
                    massage = re.sub( "n", "😪", massage)
                    massage = re.sub( "w", "😫", massage)
                    massage = re.sub( "x", "🫡", massage)
                    massage = re.sub( "z", "😙", massage)
                    encoded_massage_pending = massage[0] + key_for_massage[0] + massage[1] + key_for_massage[1] + massage[2] + key_for_massage[2] + massage[3] + key_for_massage[3]
                    encoded_massage = encoded_massage_pending + massage[4:]
                    encoded_massage = encoded_massage[::-1]
                    print(f"The massage is encoded as '{encoded_massage}'")
                    continue

            #decoding section
            elif "decode" in encode_or_decode.lower():
    
        
                if(len(massage)<3):
                    decode_of_3_characters = massage[::-1]
                    massage = decode_of_3_characters
                    print(f"The massage is {massage}")

                else:
                    key_for_massage = input("Enter key of your massage: ")
                    key_index = massage[-2] + massage[-4] + massage[-6] + massage[-8]
        
        
                    if key_for_massage != key_index:
                        while key_for_massage != key_index:
                            print("\nIncorrect key.")
                            key_for_massage = input("Try enter key again or Enter q to stop: ")
                            if key_for_massage == "q":
                                break
            
                            elif key_for_massage == key_index:
                                print("\nCorrect key!")
                                massage = massage[::-1]
                                massage = massage[6] + massage[8] + massage[9:] + massage[0] + massage[2] + massage[4]
                                massage = re.sub( "💀"," ", massage)
                                print(f"The massage is '{massage}'")
                                break
                    else:
                        print("\nCorrect key!")
                        massage = massage[::-1]
                        massage = massage[6] + massage[8] + massage[9:] + massage[0] + massage[2] + massage[4]
                        massage = re.sub("💀", " ", massage)
                        massage = re.sub("🫡", "x", massage)
                        massage = re.sub("😊", "a", massage)
                        massage = re.sub("😙", "z", massage)
                        massage = re.sub("🫥", "k", massage)
                        massage = re.sub("😶‍🌫️", "b", massage)
                        massage = re.sub("🙄", "c", massage)
                        massage = re.sub("🤐", "i", massage)
                        massage = re.sub("😯", "l", massage)
                        massage = re.sub("😪", "n", massage)
                        massage = re.sub("😫", "w", massage)
                        print(f"The massage is '{massage}'")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    elif hour>=18 and hour<24:
        speak("good night sir")   

    else:
        speak("Good Evening sir!")  

    speak("how can I help you")       


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='er-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("\nSay that again please...") 
        speak("Say that again please.")
        return ""
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sudais090802@gmail.com', 'your-password')
    server.sendmail('sudais090802@gmail.com', to, content)
    server.close()


def close_app(process_name):
    try:
        os.system(f"taskkill /f /im {process_name}.exe")
    except Exception as e:
        print(f"An error occurred: {e}")


def start_app(appname):
        dir = address_of_command("app",appname)
        os.startfile(os.path.join(dir))


def start_web(web):
        address = address_of_command("web",web)
        webbrowser.open(address)


def removing_str(remove,sentance):
    re.sub(remove, "", sentance)
    return re.sub(remove, "", sentance)


def search_in_web(search_in,query):
        search = removing_str(f"search in {search_in}",query)
        Url = address_of_command("search in web", search_in)
        address = f"{Url}{search}"
        address1 = removing_str("\"",address)
        webbrowser.open(address1)


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = input("Enter query: ")#takeCommand()

        # Logic for executing tasks based on query
        if 'search in youtube' in query.lower():
            search_in_web("youtube",query)


        elif 'search in google' in query.lower():
            search_in_web("google",query)
                

        elif 'open youtube' in query:
            start_web("youtube")
            print("seccessful opening youtube.")
                

        elif 'open google' in query:
            start_web("google")
            print("seccessful opening Google.")

            
        elif 'open hd movies 2' in query:
            start_web("hd movies 2")
            print("seccessful opening HD movies 2.")

            
        elif 'play music' in query:
            music_dir = "G:\SONGS\ENGLISH\VIDEO"
            songs = os.listdir(music_dir)
            songs.sort() 
            for sln,swn in enumerate(songs):
                print(f"{sln}:  {swn}") if sln<100 else print(f"{sln}: {swn}")
            try:
                speak("say the index please.")
                numofindex = takeCommand().lower()
                #inint = w2n.word_to_num(numofindex)
                print(f'opening music {songs[int(numofindex)]}...')    
                #os.startfile(os.path.join(music_dir, songs[int(inint)]))
                print(f'Successful playing {songs[int(numofindex)]}.')
                    
            except Exception as e:
                #print(f"You said {inint}")
                print(f"The final song's index is: {len(songs) - 1}.")

        elif 'play the music' in query.lower():
            querp1 = re.sub("play the music", "", query.lower())
            music_dir = "G:\SONGS\ENGLISH\VIDEO"
            songs = os.listdir(music_dir)
            songs.sort()
            songs_lower = list(map(str.lower, songs))
            print("List of all songs.")
            sln = 0
            for swn in songs:
                print(f"{sln}: {swn}")
                sln = sln+1
            index = None
            for i, name in enumerate(songs_lower):
                if querp1 in name:
                    index = i
                    break

            if index is not None:
                print(f'\nopening music {songs_lower[index]}...')    
                os.startfile(os.path.join(music_dir, songs_lower[index]))
                print(f"\nYou said {query}")
                print(f'\nSuccessful playing {songs_lower[index]}.')
                
            else:
                print(f"\nNo music matched for{querp1}")
                
        elif 'play some music' in query:
            music_dir1 = ""
            songs1 = os.listdir(music_dir1)
            inint1 = random.randint(0,(len(songs1) - 1))
            os.startfile(os.path.join(music_dir1, songs1[inint1]))
            speak("listen this music sir.")
            print(f'\n \nSuccessful playing {songs1[inint1]}.')

        elif 'stop music' in query:
            speak("ok sir.")
            close_app("vlc")
            print("\n \nSuccessful close VLC player.")

        elif 'stop movie' in query:
            speak("ok sir.")
            close_app("vlc")
            print("\n \nSuccessful close VLC player.")

 
        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'\n \nSir the time is {strTime}')
            speak(f"Sir, the time is {strTime}")

            
        elif 'email to cxn' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sudais090802@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ilyas. I am not able to send this email")  

                
        elif 'open free fire' in query:
            start_app("free_fire_bluestack")

       

        elif 'close free fire' in query:
            speak("ok sir.")
            close_app("msi app player")
            print("\n \nSuccessful close msi app player.")


        elif 'task manager' in query:
            start_app("task manager")
            print("\n \nSuccessful run task manager.")

       


        elif 'close task manager' in query:
            speak("ok sir.")
            close_app("task manager")
            print("\n \nSuccessful close task manager.")



        
        elif 'open whatsApp' in query:
            start_app("whatsApp")
           
        elif'close whatsApp'   in query:
            speak("ok sir.") 
            close_app("whtasApp")
            print("\n \nSuccessful close whatsApp.")
        
           
        elif 'command prompt' in query:
            start_app("cmd")
            print("\n \nSuccessful run command prompt.")

        elif 'close command prompt' in query:
            speak("ok sir.")
            close_app("command prompt")
            print("\n \nSuccessful close command prompt.")


        elif 'control panel' in query:
            start_app("control panel")
            print("\n \nSuccessful run control panel.")

        elif 'close control panel' in query:
            speak("ok sir.")
            close_app("control panel")
            print("\n \nSuccessful close control panel.")


        elif 'system information' in query:
            start_app("sys info")
            print("\n \nSuccessful run system information.")

        elif 'close system information' in query:
            speak("ok sir.")
            close_app("system information")
            print("\n \nSuccessful close system information.")


        elif 'photo screen' in query:
            start_app("screen saver")

        
        elif 'regestory editor' in query:
            start_app("reg edit")
            print("\n \nSuccessful run regestory editor.")

        elif 'close regestory editor' in query:
            speak("ok sir.")
            close_app("regestory editor")
            print("\n \nSuccessful close regestory editor.")

            
        elif 'ribbon screen' in query:
            start_app("ribbon screen saver")


        elif 'volume mixer' in query:
            start_app("volume mixer")
        elif 'close volume mixer' in query:
            speak("ok sir.")
            close_app("volume mixer")
            print("\n \nSuccessful close volume mixer.")


        elif 'windows explorer' in query:
            start_app("explorer")
            

        elif 'open chrome' in query:
            start_app("chrome")

        elif 'close chrome' in query:
            speak("ok sir.")
            close_app("chrome")
            print("\n \nSuccessful close chrome.")


        elif 'open opera' in query:
            start_app("opera")

        elif 'close opera' in query:
            speak("ok sir.")
            close_app("opera")
            print("\n \nSuccessful close opera.")


        elif 'massage encoder' in query:
            msgencoder()
           


        #Chatting
        elif'what is your favrate friend'in query.lower():
            print("my best friend is you sir i love you")    
            speak("my best friend is you sir i love you")
        elif'do you knowe my name'in query.lower():
            print("yes sir your name is muhammad ilyas khan")    
            speak("yes sir your name is muhammad ilyas khan")
       
        elif'what are you from' in query.lower():
            print("i am frome your hand sir")
            speak("i am frome your hand sir")    
        elif 'how are you' in query.lower():
            print("I am fine alhamdulillah sir what about you")
            speak("I am fine alhamdulillah sir what about you")
        elif 'are you fine' in query.lower():
            print("I am fine alhamdulillah sir what about you")
            speak("I am fine alhamdulillah sir what about you")
        elif 'how you are' in query.lower():
            print("I am fine alhamdulillah sir what about you")
            speak("I am fine alhamdulillah sir what about you")
        elif'aj may apko kaysa lag raha ho'in query.lower():
            print("buhut acha sir")
            speak("buhut acha sir")
        elif 'whats your faverate player in pakistan team' in query.lower():
            print("my faverate player is babar azam")
            speak("my faverate player is babar azam")
        elif 'i love you' in query.lower():
            print("I am just a machine sir i don\'t have feelings")
            speak("I am just a machine sir, i don\'t have feelings")
        elif 'you are my love' in query.lower():
            print("I am just a machine sir i don\'t have feelings")
            speak("I am just a machine sir, i don\'t have feelings")
        elif 'i kiss you' in query.lower():
            print("I am just a machine sir i don\'t have feelings")
            speak("I am just a machine sir, i don\'t have feelings")  
        elif 'whats your name' in query.lower():
            print("my name is computer laptop sir")
            speak("my name is computer laptop sir")
        elif'jan' in query.lower():
            print(" G SIR")   
            speak("G SIR")
        elif'what country are you like'  in query.lower():
            print("i like pakistan, pakistan is so very beutiful country i love my country i love pakistan and i love you ilyaas ") 
            speak("i like pakistan, pakistan is so very beutiful country i love my country i love pakistan and i love you ilyaas") 
     



        else:
            if (len(query)>8):
                print("Searching in Wikipedia....")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print("\n\nAccording to Wikipedia:")
                print(f"\n{results}")
                speak(results)

            