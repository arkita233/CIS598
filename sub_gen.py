# audio process Pydub
# Need ffmpeg
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import subprocess
import os
import sys

FILE_PATH = sys.argv[1]


# convert pieces to wav with Pydub and ffmpeg
def pieces_to_wav(audio_pieces):
    for index, value in enumerate(audio_pieces):
        value.export('tmp/%d.wav' % index, format='wav')


def audio_to_text(audio_path):
    audio_pieces = sr.AudioFile(audio_path)
    with audio_pieces as p:
        audio = r.record(p)
        result = r.recognize_google(audio)
    return result


def ms_to_s(ms):
    m_p = ms % 1000
    m_p = str(m_p).zfill(3)
    s_p = (ms // 1000) % 60
    s_p = str(s_p).zfill(2)
    m_part = (ms // 1000) // 60
    m_part = str(m_part).zfill(2)

    # srt time
    s_type = "00:" + m_part + ":" + s_p + "," + m_p
    return s_type


def text_to_str(index, context, start_time, end_time):
    texts = str(index) + '\n' + ms_to_s(start_time) + ' --> ' + ms_to_s(end_time) + '\n' + text + '\n' + '\n'
    return texts


def str_to_file(texts):
    with open('out.srt', 'a') as fp:
        fp.write(texts)
        fp.close()


def remove_file(path):
    l = os.listdir(path)
    for i in l:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            remove_file(c_path)
        else:
            os.remove(c_path)


if __name__ == '__main__':
    print("program start")
    remove_file('tmp/')
    r = sr.Recognizer()

    if not os.path.exists('test.wav'):
        # -i: input -vn: video not -f: format
        print("start extracting")
        subprocess.call('ffmpeg -i '+FILE_PATH+' -vn -f wav test.wav')

    # Read sound file
    sound_file = AudioSegment.from_file('test.wav')

    min_silence_len = 200
    silence_thresh = -45

    print("start cutting audio to pieces")
    # Cut audio, get 3 lists of pieces, start time and end time
    pieces, start_t, end_t = split_on_silence(sound_file, min_silence_len, silence_thresh)

    if os.path.exists("out.srt"):
        os.remove("out.srt")

    print("start exporting pieces")
    pieces_to_wav(pieces)
    print("export over, start contact with API")

    for inx, val in enumerate(pieces):
        # get text
        try:
            text = audio_to_text('tmp/%d.wav' % inx)
        except sr.UnknownValueError:
            continue
        else:

            # print(text)
            text_2 = text_to_str(inx, text, start_t[inx], end_t[inx])

            str_to_file(text_2)
            p = (inx * 100 / len(pieces))

            o = '{:.2f}%'.format(p)
            print("\b" * len(o), end='', flush=True)
            print(o, end='')
