import eel
import voice_assistant
import speech_recognition as sr

# Specify the root folder where your HTML files are located
eel.init('www')

recognizer = sr.Recognizer()
microphone = sr.Microphone()

@eel.expose
def process_voice(input_text=None):
    if input_text is not None:
        # This block is for handling calls from JavaScript
        try:
            voice_data = input_text
            print(f"Received from JavaScript: {voice_data}")
            result = voice_assistant.process_voice(voice_data)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        # This block is for handling calls from Python
        with microphone as source:
            print("Say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        try:
            voice_data = recognizer.recognize_google(audio)
            print(f"Recognized: {voice_data}")
            result = voice_assistant.process_voice(voice_data)
            print(result)
            return result
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
            return "Error: Speech Recognition could not understand audio"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return f"Error: {e}"

# Start the application
eel.start('index.html', mode='chrome', port=0, cmdline_args=['--no-sandbox'], block=True)

