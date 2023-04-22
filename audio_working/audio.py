import speech_recognition


def recognize():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as micro:
        recognizer.adjust_for_ambient_noise(source=micro)
        audio = recognizer.listen(source=micro)
        query = recognizer.recognize_google(audio_data=audio, language="ru-RU")
    return query
