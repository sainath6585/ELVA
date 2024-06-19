import tkinter as tk
from PIL import Image, ImageSequence  
from PIL import Image, ImageTk
from tkinter import scrolledtext
import pyttsx3
import speech_recognition as sr
import randfacts
from pyjokes import *
import datetime
import webbrowser
import requests
from tkinter import scrolledtext
from tkinter import ttk
import threading
import tkinter as tk
from PIL import Image, ImageTk
import wikipedia
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)  # Adjust the value as needed (default rate is 200)

# Function to speak out the provided text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    output_text.insert(tk.END, audio + '\n\n')  # Insert spoken text into the output text area
    output_text.see(tk.END)  # Scroll the output text area to show the latest text


# Function to greet the user based on the time of day
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("how can ,I help you boss")

# Function to recognize voice command using the microphone
def VoiceCommand(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Recognizing...")
        r.pause_threshold = 0.5
        audio = r.listen(source) 
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None" 


# Function to process voice commands
def process_voice_command(work):
    news_headlines = None  # Initialize news_headlines with a default value

    if work:
        # Process the voice command
        if 'hello' in work:
            speak('Yes boss, I am here. How can I assist you?')

        if 'hey elva' in work:
            speak('hii boss how are you')
        if 'Iam fine what about you ' in work:
            speak('iam also fine boss,how can i help for you today')
        
        if "search" in work:
            speak("Searching answers...")
            work = work.replace("wikipedia", "")
            results = wikipedia.summary(work, sentences=3)
            try:
                results = wikipedia.summary(work, sentences=3)
                print(results)
            except wikipedia.exceptions.DisambiguationError as e:
                print("Disambiguation error:", e)
            except wikipedia.exceptions.PageError as e:
                print("Page error:", e)
            except wikipedia.exceptions.WikipediaException as e:
                print("Wikipedia error:", e)
            except Exception as e:
                print("An unexpected error occurred:", e)
            speak("According to wikipedia")
            print(results)
            speak(results)
            # Display the result in the GUI
            output_text.insert(tk.END, results + '\n\n')

        elif 'what is weather status' in work:
            speak("Please specify the city name.")
            city_name = VoiceCommand().capitalize()
            api_key = 'af44bbde530a0789541206098896b636'
            weather_info = get_weather(city_name, api_key)
            speak(weather_info)
            output_text.insert(tk.END, weather_info + '\n\n')

        elif 'what is today news' in work:
            speak("Fetching the latest news headlines...")
            api_key = 'ee417aaf9a5d479288fbb4247420e059'  # Replace with your actual News API key
            news_headlines = get_news(api_key)
            if news_headlines:
                speak_news(news_headlines)
                output_text.insert(tk.END, "Here are the latest news headlines:\n")
                for headline in news_headlines:
                    output_text.insert(tk.END, headline + '\n')
                output_text.insert(tk.END, '\n')

        elif 'what is today news' in work:
            speak("Fetching the latest news headlines...")
            api_key = 'ee417aaf9a5d479288fbb4247420e059'  # Replace with your actual News API key
            news_headlines = get_news(api_key)
        if news_headlines:
           speak_news(news_headlines)          
        
        elif "funny" in work:
            speak("Get ready for some chuckles")
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "your name" in work:
            speak("My name is Next genn Optimal Voice Assistant ELVA")

        elif "fact" in work:

              speak("Sure sir , ")
              x = randfacts.getFact()
              speak("Did you know that," + x)
              print(x)
              
        elif 'open notepad' in work:
            speak('opening notepad for you.......')
            path = ("c:\\windows\\system32\\notepad.exe")
            os.startfile(path)
        elif 'close notepad' in work:
            speak('closing notepad wait.....')
            os.system('c:\\windows\\system32\\taskkill.exe /F /IM notepad.exe')

        elif 'open youtube' in work:
          speak("Opening YouTube...")
          webbrowser.open("https://www.youtube.com/")
          speak("What would you like to search for?")
          search_query = VoiceCommand().lower()
          if search_query:
             speak(f"Searching for {search_query} on YouTube...")
             youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"
             webbrowser.open(youtube_search_url)


        elif 'open google' in work:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/")
            speak("What would you like to search for?")
            search_query = VoiceCommand().lower()
            if search_query:
                speak(f"Searching for {search_query} on Google...")
                google_search_url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(google_search_url)
            else:
                speak("Sorry, I didn't catch that. Please try again.")
            
        elif 'close youtube' in work:
            speak("closing youtube")

        elif 'play music' in work :
            speak('opening music player....')
            path = ("C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")
            os.startfile(path)
            
        elif 'open mail' in work:
            speak("Here you go to mail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        
        elif 'open whatsapp' in work:
            speak("opening whatsapp for you")
            webbrowser.open("https://web.whatsapp.com/")
        
        elif 'exit' in work:
            speak("Thanks for giving me your time. Have a nice day!")
            exit()

        

# Function to get weather information
def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return f"The weather in {city_name} is {weather_description}. Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s."
    else:
        return "Sorry, I couldn't fetch the weather information at the moment."
    
def get_news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        headlines = [article['title'] for article in articles]
        return headlines
    else:
        return []
def speak_news(headlines):
    if headlines:
        speak("Here are the latest news headlines:")
        for headline in headlines:
            speak(headline)
    else:
        speak("Sorry, I couldn't fetch the latest news headlines at the moment.")

# Create and configure GUI elements
root = tk.Tk()
root.title("Full Screen Background Image")
root.geometry("900x850")


# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load the image
image_path = "www/assets/img/Screenshot (227).png"  # Replace with your image file path
image = Image.open(image_path)

# Resize the image to fit the screen
resized_image = image.resize((screen_width, screen_height), Image.LANCZOS)

# Convert the image to a Tkinter-compatible format
photo_image = ImageTk.PhotoImage(resized_image)

# Create a label with the image
background_label = tk.Label(root, image=photo_image)
background_label.pack(fill=tk.BOTH, expand=True)

# Configure the label to occupy the entire window
background_label.place(x=0, y=0, relwidth=1, relheight=1)


  

# Create a scrolled text widget for displaying output
output_text = scrolledtext.ScrolledText(root, width=40, height=200, )
output_text.pack(side=tk.RIGHT)



# Configure the style of the text box
output_text.configure(bg="black", fg="black", font=("Arial", 12), highlightthickness=0)

processing = False  # Global variable to control the processing loop

def handle_voice_command():
    global processing
    greet()
    while processing: 
        work = VoiceCommand().lower()
        if not processing:
            break
        process_voice_command(work)  # Pass the 'work' argument here

# Function to start processing voice commands when the button is clicked
def start_processing():
    global processing, processing_thread
    output_text.delete(1.0, tk.END)  # Clear previous output
    speak("Welcome, I am your personal assistant")
    # Disable the start button
    button_start.config(state=tk.DISABLED)
    # Enable the stop button
    button_stop.config(state=tk.NORMAL)
    processing = True
    processing_thread = threading.Thread(target=handle_voice_command)
    processing_thread.start()  # Start processing voice commands in a separate thread


# Function to stop processing voice commands when the button is clicked
def stop_processing():
    global processing
    processing = False
    engine.stop()  # Stop the speech engine
    # Enable the start button
    button_start.config(state=tk.NORMAL)
    # Disable the stop button
    button_stop.config(state=tk.DISABLED)





# Style for the buttons
button_style = {
    "bg": "blue",       # Background color
    "fg": "white",         # Text color
    "font": ("Arial", 12), # Font
    "width": 10,           # Button width
    "height": 2,           # Button height
    "bd": 0,               # Border width
    
}


# Create a frame to contain the buttons
button_frame = tk.Frame(root,  bg="black")
button_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Create the start button
button_start = tk.Button(button_frame, text="Speak", command=start_processing, **button_style)
button_start.pack(side=tk.BOTTOM, anchor=tk.CENTER, padx=100, pady=20)



# Create the stop button
button_stop = tk.Button(button_frame, text="Stop", command=stop_processing, **button_style)
button_stop.pack(side=tk.BOTTOM, padx=200, pady=20)








# Main loop
root.mainloop()
