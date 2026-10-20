import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper


SAMPLE_RATE = 16000  
MODEL_NAME = "base.en"

print("Loading Whisper model...")
model = whisper.load_model(MODEL_NAME)

print("\nReady to record.")
input("Press ENTER to start recording...")

audio_chunks = []

def audio_callback(indata, frames, time_info, status):
    if status:
        print("Audio status:", status)
    audio_chunks.append(indata.copy())

print("Recording... Press ENTER again to stop.")

with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="int16", callback=audio_callback):
    input() # dtypy makes difference

print("Recording stopped.")

# Combine audio chunks
audio = np.concatenate(audio_chunks, axis=0)

# Save audio
write("recording.wav", SAMPLE_RATE, audio)

print("Recording saved to recording.wav")
print("Transcribing...")

# Transcribe with Whisper
result = model.transcribe("recording.wav", fp16=False)

text = result["text"].strip()

print("\nRecognized text:")
print(text)

# Save transcription
with open("transcription.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nTranscription saved to transcription.txt")

