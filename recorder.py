import sounddevice as sd
import soundfile as sf
import openai  # Don't forget to import the necessary library
import threading  # Import threading for handling user input in parallel

openai.api_key = "YOUR_API_KEY"
# Set up your OpenAI API key

def record_audio(filename, duration, samplerate):
    print("Listening... Press Enter to stop recording.")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    
    sd.wait()  # Wait for recording to finish
    sf.write(filename, audio_data, samplerate)
    print("Recording stopped.")
    
    with open(filename, 'rb') as audio_file:
        print("Recognizing...")
        transcript = openai.Audio.transcribe("whisper-1", file=audio_file)
    
    return transcript["text"]

