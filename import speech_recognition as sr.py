import librosa
import numpy as np
import joblib
import speech_recognition as sr
import pyttsx3
from sklearn.preprocessing import StandardScaler

# Load the trained model from the file
loaded_model = joblib.load('trained_model.joblib')

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice for the text-to-speech engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech input
def recognize_speech():
    y = None
    sr = None
    
    try:
        print('Speak now...')
        audio = sd.rec(int(44100 * 5), samplerate=44100, channels=1, dtype='int16')
        sd.wait()
        y = audio.flatten()
        sr = 44100
        text = r.recognize_google(audio)
        print(f'You said: {text}')
    except Exception as e:
        print(f'Sorry, could not recognize your voice. Error: {e}')

    return y, sr

# Define a function to extract features from speech input
def extract_features(y, sr):
    # Convert audio data to floating-point
    y = y.astype(float)

    # Extract the Mel-frequency cepstral coefficients (MFCCs) from the audio
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

    # Flatten the MFCCs into a 1D array
    features = mfccs.flatten()

    return features

# Define a function to classify the emotion from speech input
def classify_emotion(y, sr):
    if y is not None and sr is not None:
        features = extract_features(y, sr)
        features = scaler.transform([features])
        emotion = loaded_model.predict(features)[0]
        return emotion
    else:
        return None

# Define a function to generate a response based on the classified emotion
def generate_response(emotion):
    if emotion == 'happy':
        return 'I am glad to hear that!'
    elif emotion == 'sad':
        return 'I am sorry to hear that.'
    elif emotion == 'angry':
        return 'Please calm down.'
    else:
        return 'I did not understand your emotion.'

# Load the scaler object from the file
scaler = joblib.load('/path/to/scaler.joblib')

# Main loop for the chatbot
while True:
    y, sr = recognize_speech()
    emotion = classify_emotion(y, sr)
    response = generate_response(emotion)
    speak(response)