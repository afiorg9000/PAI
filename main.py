import openai
import os
from gtts import gTTS
from task_creator import create_task
from code_handler import extract_code, save_to_file, generate_filename, get_file_extension
from focus_time_handler import start_focus_mate_session
import speech_recognition as sr
import pyttsx3
import matplotlib.pyplot as plt


openai.api_key = os.environ['OPENAI_API_KEY']

def say(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('afplay output.mp3')

def get_input_mode():
    while True:
        mode = input("Choose input mode (speak/type): ")
        if mode.lower() == "speak" or mode.lower() == "type":
            return mode.lower()
        else:
            print("Invalid input mode. Please choose 'speak' or 'type'.")

def recognize_speech():
    r = sr.Recognizer()

    # Adjust the microphone device index if needed
    mic_device_index = 0

    with sr.Microphone(device_index=mic_device_index) as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        user_input = r.recognize_google(audio)
        print("You:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing the speech recognition service.")
        return ""

def ask_question():
    input_mode = get_input_mode()

    while True:
        if input_mode == "speak":
            user_input = recognize_speech()
        elif input_mode == "type":
            user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        messages = [
            {
                "role": "system",
                "content": "You are PAI, A personalized conversational AI assistant tailored to my needs, designed to assist me in achieving self-actualization by enhancing my productivity, integrity, and accomplishments."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]

        if "create task" in user_input.lower():
            create_task()
            continue

        if "focusmate" in user_input.lower() or "focus mate" in user_input.lower():
            start_focus_mate_session()
            continue

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500
        )

        assistant_response = response.choices[0].message['content']
        print("SofAI:", assistant_response)

        if "code" in user_input.lower():
            code_only = extract_code(assistant_response)
            file_extension = get_file_extension(user_input)
            save_to_file(code_only, file_extension)

# Main program flow
ask_question()  # Initial prompt
