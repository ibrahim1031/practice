import pyttsx3

def text_to_audio(text, language='en', file_name='output.mp3'):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties to use a male voice (if available)
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'male' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    # Convert text to speech and save the audio to a file
    engine.save_to_file(text, file_name)
    engine.runAndWait()

    print(f"Audio file '{file_name}' generated successfully.")

if __name__ == "__main__":
    text_input = input("Enter the text you want to convert to audio: ")
    language_code = input("Enter the language code (e.g., en, en-us, fr, es, etc.): ")

    output_file_name = "output_audio.mp3"
    
    text_to_audio(text_input, language=language_code, file_name=output_file_name)
