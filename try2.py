import speech_recognition as sr


def audio_to_text(audio_path):
    audio_pieces = sr.AudioFile(audio_path)
    with audio_pieces as p:
        audio = r.record(p)
        result = r.recognize_google(audio)
    return result


r = sr.Recognizer()
print(audio_to_text('genevieve.wav'))