import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
from pywikihow import search_wikihow
import pywhatkit as kit


engine=pyttsx3.init('sapi5')
def hindi(command):

    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    engine.say(command)
    # audio=command[0:8]
    # engine.save_to_file(command,audio+".mp3")
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        hindi("शुभ प्रभात! आदर्श जी ")
    elif hour >=12 and hour <17:
        hindi("Good Afternoon sir!")
    else:
        hindi("सुसंध्या! आदर्श जी")
    hindi("जानेमन मैं आपकी कैसे मदद कर सकती हूँ  ")

wishme()

def takecommand():
    listener= sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening............")
            voice=listener.listen(source)
            print("Recognizing..........")
            command=listener.recognize_google(voice,language="hi-In")
            print("You say that:",command)

    except:
        print("say that again sir please")
        return "none"

        # pass
    return command

# query=takecommand()




while True:
    query = takecommand()

    if "शायरी" in query:
        hindi("पत्ते गिरते नहीं हवा गिरा देती है   पत्ते गिरते नहीं हवा गिरा देती है   लड़के बिगड़ते नहीं है   लड़कियां बिगाड़ देती है")



    elif "कैसे हो आप" in query:

        hindi("मै अच्छी हु जानेमन ")
        hindi("मुझे आशा है कि आप स्वस्थ और कुशल मंगल हैं")

    elif "सुहागरात कैसे मनाए" in query:
        max_results = 1
        how_to = search_wikihow(query, max_results, "hi")
        assert len(how_to) == 1
        how_to[0].print()
        hindi(how_to[0])


    elif 'ओपन फेसबुक' in query:
        webbrowser.open("https://www.facebook.com/")

    elif 'ओपन इंस्टाग्रा' in query:
        webbrowser.open("https://www.instagram.com/")


    elif "पसंदीदा गीत बजा" in query or "पसंदीदा गाना बजा" in query:
        from playsound import playsound
        playsound("neele.mp3")

        # music_path = "D:\\English musics\\fav song"
        # songs = os.listdir(music_path)
        # print(songs)
        # os.startfile(os.path.join(music_path, songs[0]))



    elif "बनाने" in query:
        hindi("मुझे बनाने के लिए आपने अपना प्यार खोया है")



    elif "गाना बजा दो" in query:
        music_path = "D:\\English musics\\mymusic"
        songs = os.listdir(music_path)
        print(songs)
        os.startfile(os.path.join(music_path, songs[0]))


    if "play" in query:
        song = query.replace("play", " ")
        hindi(song)
        kit.playonyt(song, True, True)


    elif "क्या समय" in query:
        strTime=datetime.datetime.now().strftime("%I bajkar %M minutes")
        hindi(f"आदर्श जी समय है {strTime}")

    elif "कॉलेज में प्यार" in query:
        hindi("कृपया अपने कॉलेज में प्यार ना करे आप बर्बाद हो जायेंगे")

    elif "दिल में आग लग जाए" in query:
        hindi("हार कैसे मान जाये साहब मेरी माँ कब से मेरी सफलता का इंतज़ार कर रही है")


    elif "चुम्मा" in query:

        from playsound import playsound

        playsound("kiss Sound (2).mp3")

        hindi("आपका और कोई आदेश")


    elif "मेरा रूम पार्टनर" in query:
        hindi("आपका रूम पार्टनर एक नंबर चुतिया है फालतू का ज्ञान देने वाला  इस देश का महा चोमू प्राणी है,   लेकिन हैं तो आपका ही जान")

    elif "आप जा" in query:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            hindi("आपका दिन कुशल मंगल हो,  जानेमन    धन्यवाद!")
        elif hour >= 12 and hour < 17:
            hindi("आपकी रात्रि कुशल मंगल हो,  जानेमन    धन्यवाद!")
        else:
            hindi("आपकी रात्रि कुशल मंगल हो,  जानेमन  आदर्श जी  धन्यवाद!")
        exit()






# query=takecommand()

hindi(query)