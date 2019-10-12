from NaiveBayes import  Pool
import os
import pyttsx3
import random
from PIL import Image,ImageTk
import time
import speech_recognition as sr
import random
import time
from tkinter import *
from texttospeech import speech11
import speech_recognition as sr
root=Tk()
root.title("HEALTH MONITORING SYSTEM")
root.geometry("1600x800")

DClasses = ["a","allergies","c","f","h","s","u"]
f="plz"
base = "learn/"
p = Pool()
for i in DClasses:
    print(i)
    p.learn(base + i, i)
base = "test/"
print("Enter what is your problem: ")
#s=input("enter here: ")
'''
def recognize_speech_from_mic(recognizer, microphone):
  
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

   
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
    
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
    
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
  
    WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 1
    PROMPT_LIMIT = 5

   
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

   
    word = random.choice(WORDS)

   
    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)
    #print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
     
        for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            guess1=format(guess["transcription"])
            print(guess1)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

       
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

       
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        
        if guess_is_correct:
            print("Correct! You win!".format(word))
            break
        elif user_has_more_attempts:
            print("Incorrect. Try again.\n")
        else:
            print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
            break         
s=guess1'''
s=input("enter here")
l30=Label(root,text=s,font=('arial',15,'bold'))
l30.pack()
#print(s)
r=0.1
rr=r
rrr=r
rrrr=r
img = PhotoImage(file="human.png")
img1=PhotoImage(file="computer.png")
root.configure(background="black")

background_image = PhotoImage(file="keeee.gif")

background = Label(root, image=background_image, bd=0)
background.pack()  
text_file=open("test/plz/ot.txt","w")
text_file1=open("test/plz/ot1.html","w")
text_file.write(s)
text_file1.write(s)
text_file.close()
#text_file.write()
text_file.close()
try:
 for i in range(0,5,1):
  with open("test/plz/ot.txt","a") as text_file:
   text_file.write('\n')
   
   dir = os.listdir(base + f)
   for file in dir:
      res = p.Probability(base + f + "/" + file)
      if(file=="ot.txt"):
        #print(f + ": " + file + ": " +str(res))
        req=str(res[0])
        #print(req[2])
        count_n=0
        for i in range(0,3,1):
           l='learn/'
           c="Chatbot.txt"
           manu=str(res[0])
           k2=manu[2]
           k1=k2+c
           tt=k1
           l30['text']=k1
           #print(k1)
           fp=open(l+k2+"/"+k1)
           lines=fp.read().split("\n")
           l2=Label(root,text=lines[i],font=('arila',15,'bold'))
           l2.place(relx=0.5,rely=rr,anchor=CENTER)
           rr+=0.1
           imglabel = Label(root, image=img1)
           imglabel.place(relx=0.1,rely=rrr,anchor=CENTER)
           rrr+=0.1
           #print(lines[i])
           engine = pyttsx3.init()
           k=''
           #k=input('enter the text u want to speak out')
           k=lines[i]
           engine.say(k)
           engine.setProperty('rate',45)
           engine.setProperty('volume', 5)
           engine.runAndWait()
           in1=input("Enter here: yes/no:")
           l3=Label(root,text=in1,font=('arial',15,'bold'))
           l3.place(relx=0.7,rely=r,anchor=CENTER)
           r+=0.1
           imglabel1 = Label(root, image=img)
           imglabel1.place(relx=0.8,rely=rrrr,anchor=CENTER)
           rrrr+=0.1
           #in1=speechtotext123()
           if(in1=="no"):
                count_n +=1
        l3=Label(root,text="it is a disease name",font=('arial',15,'bold'))
        l3.place(relx=0.5,rely=0.9,anchor=CENTER)        
        if(count_n<=1):	
            print(manu[2])
            if(manu[2]=='f'):
                a123="you might have fever"
                l3['text']=a123
                speech11(a123)
            if(manu[2]=='a'):
                a123="you might have acute"
                l3['text']=a123
                speech11(a123)
            if(manu[2]=='h'):
                a123="you might have heart problem"
                l3['text']=a123
                speech11(a123)
            if(manu[2]=='c'):
                a123="you might have cancer"
                l3['text']=a123
                speech11(a123)
            if(manu[2]=='s'):
                a123="you might have signs problem"
                speech11(a123)
            if(manu[2]=='u'):
                a123="you might have ulser"
                l3['text']=a123
                speech11(a123)
            root.mainloop()
            time.sleep(1)     
            exit() 			                
        else:
           l='learn/'
           c="Chatbot.txt"
           manu=str(res[1])
           k2=manu[2]
           k1=k2+c
           print(k1)
           l30['text']=tt+" "+k1
           count_n1=0
           for i in range(0,3,1):
              fp=open(l+k2+"/"+k1)
              lines=fp.read().split("\n")
              newQ=" "
              rkv=lines[i]
              l2=Label(root,text=lines[i],font=('arila',15,'bold'))
              l2.place(relx=0.5,rely=rr,anchor=CENTER)
              rr+=0.1
              imglabel = Label(root, image=img1)
              imglabel.place(relx=0.1,rely=rrr,anchor=CENTER)
              rrr+=0.1
              #print(lines[i])
              engine = pyttsx3.init()
              k=''
              #k=input('enter the text u want to speak out')
              k=lines[i]
              engine.say(k)
              engine.setProperty('rate',45)
              engine.setProperty('volume', 5)
              engine.runAndWait()
              new=lines[i]
              in1=input("Enter here: yes/no")
              l3=Label(root,text=in1,font=('arial',15,'bold'))
              l3.place(relx=0.7,rely=r,anchor=CENTER)
              r+=0.1
              imglabel1 = Label(root, image=img)
              imglabel1.place(relx=0.8,rely=rrrr,anchor=CENTER)
              rrrr+=0.1
              #in1=speechtotext()
              if(in1=="yes"):
                for i in range(10,len(new),1):
                     newQ=newQ+new[i]
                print(newQ)
                text_file=open("test/plz/ot.txt","a")
                text_file.write(newQ)
                break
              count_n1 +=1
           if(count_n1!=0):
             
            print("Please Enter one of your symptoms: ")
            def recognize_speech_from_mic(recognizer, microphone):
             if not isinstance(recognizer, sr.Recognizer):
                   raise TypeError("`recognizer` must be `Recognizer` instance")

             if not isinstance(microphone, sr.Microphone):
                   raise TypeError("`microphone` must be `Microphone` instance")

   
             with microphone as source:
                     recognizer.adjust_for_ambient_noise(source)
                     audio = recognizer.listen(source)

   
             response = {
                               "success": True,
                               "error": None,
                               "transcription": None
             }

    
             try:
                response["transcription"] = recognizer.recognize_google(audio)
             except sr.RequestError:
       
                  response["success"] = False
                  response["error"] = "API unavailable"
             except sr.UnknownValueError:
       
                  response["error"] = "Unable to recognize speech"

             return response


            if __name__ == "__main__":
               WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
               NUM_GUESSES = 1
               PROMPT_LIMIT = 5

   
               recognizer = sr.Recognizer()
               microphone = sr.Microphone()

   
               word = random.choice(WORDS)

               instructions = (
                            "I'm thinking of one of these words:\n"
                            "{words}\n"
                            "You have {n} tries to guess which one.\n"
               ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    
               #print(instructions)
               time.sleep(3)
               for i in range(NUM_GUESSES):
       
                    for j in range(PROMPT_LIMIT):
                         print('Guess {}. Speak!'.format(i+1))
                         guess = recognize_speech_from_mic(recognizer, microphone)
                         guess1=format(guess["transcription"])
                         print(guess1)
                         if guess["transcription"]:
                             break
                         if not guess["success"]:
                             break
                         print("I didn't catch that. What did you say?\n")

        
                    if guess["error"]:
                         print("ERROR: {}".format(guess["error"]))
                         break

       
                    guess_is_correct = guess["transcription"].lower() == word.lower()
                    user_has_more_attempts = i < NUM_GUESSES - 1

                    if guess_is_correct:
                      print("Correct! You win!".format(word))
                      break
                    elif user_has_more_attempts:
                      print("Incorrect. Try again.\n")
                    else:
                      print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
                      break
except:
	pass                                         
new=guess1
text_file=open("test/plz/ot.txt","a")
text_file.write(new1)                
