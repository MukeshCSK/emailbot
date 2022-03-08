import smtplib
import speech_recognition as sr
import pyttsx3
import pyautogui
from time import sleep
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talking(text):
    engine.say(text)
    engine.runAndWait()
    
def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    a = pyautogui.prompt(text='Enter your MailID', title='Login Page' , default='mukeshshankar2001@gmail.com')
    b = pyautogui.password(text='Enter your password', title='Login Page', default='', mask='*')
    server.login(a, b)
    email = EmailMessage()
    email['From'] = a
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    
email_list = {
    'abhinav' : 'xblaze2002@gmail.com',
    'daddy' : 'pandushankar@gmail.com',
    'kamlesh' : 'kamalesh1804@gmail.com',
    'monica' : 'mounikanesamani@gmail.com',
    'another mukesh' : 'mukeshkolappan@gmail.com',
    'nandini' : 'nanthuvm@gmail.com',
    'derin' : 'nitheshdjn@gmail.com',
    'home' : 'omktroj25@gmail.com',
    'rudresh' : 'jee.rudresh@gmail.com',
    'smk' : 'selvamuthukannan@gmail.com',
    'sunita' : 'bsunithareach123@gmail.com',
    'swetha' : 'swethakalaiyappan@gmail.com',
    'sweater' : 'swethakalaiyappan@gmail.com',
    'vasundhara' : 'tvasundara123@gmail.com',
    'vijay raju' : 'vijayarajur31@gmail.com',
    'vishal' : 'vishalstunner03@gmail.com',
    'yashwin' : 'yaswin95040@gmail.com',
    'ashwin' : 'yaswin95040@gmail.com'
}

def get_email_info():
    talking('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talking('What is the subject of your email?')
    subject = get_info()
    talking('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talking('Email Sent!')
    talking('Do you want to send more?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()
