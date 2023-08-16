import sounddevice as sd
import soundfile as sf
import openai  # Don't forget to import the necessary library
import threading  # Import threading for handling user input in parallel

openai.api_key = "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"
# Set up your OpenAI API key

recording = True  # A flag to indicate if recording is active

def stop_recording():
    global recording
    input("Press Enter to stop recording...")
    recording = False

def record_audio(filename, duration, samplerate):
    global recording
    
    print("Listening... Press Enter to stop recording.")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    
    recording_thread = threading.Thread(target=stop_recording)
    recording_thread.start()  # Start the thread to listen for user input
    
    sd.wait()  # Wait for recording to finish
    recording = False  # Ensure recording is stopped after waiting
    sf.write(filename, audio_data, samplerate)
    print("Recording stopped.")
    
    with open(filename, 'rb') as audio_file:
        print("Recognizing...")
        transcript = openai.Audio.transcribe("whisper-1", file=audio_file)
    
    return transcript["text"]

