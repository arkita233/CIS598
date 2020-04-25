# audio process Pydub
# Need ffmpeg
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
from moviepy.editor import *


# convert files to wav with Pydub and ffmpeg
def file_to_wav(audio, name):
    audio.export("%s.wav" % name, format="wav")


# convert pieces to wav with Pydub and ffmpeg
def pieces_to_wav(audio_pieces):
    for index, value in enumerate(audio_pieces):
        value.export('%d.wav' % index, format='wav')


def write_to_txt(text):
    with open('sub.txt', 'a') as f:
        f.write(text)
        f.close()


# read pieces audio file
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def text_to_sub(index, text, start_time, end_time):
    string_sub = index + '\n' + start_time + ' --> ' + end_time + '\n' + text + '\n\n'
    return string_sub


def audio_to_text(audio_path):
    audio_pieces = sr.AudioFile(audio_path)
    with audio_pieces as p:
        audio = r.record(p)
        result = r.recognize_google(audio)
    return result


def ms_to_s(ms):
    ms_part = ms % 1000
    ms_part = str(ms_part).zfill(3)
    s_part = (ms // 1000) % 60
    s_part = str(s_part).zfill(2)
    m_part = (ms // 1000) // 60
    m_part = str(m_part).zfill(2)

    # srt time
    s_type = "00:" + m_part + ":" + s_part + "," + ms_part
    return s_type


def text_to_str(index, context, start_time, end_time):
    texts = str(index) + '\n' + ms_to_s(start_time) + ' --> ' + ms_to_s(end_time) + '\n' + text + '\n' + '\n'
    return texts


def str_to_file(texts):
    with open('out.txt', 'a') as fp:
        fp.write(texts)
        fp.close()


if __name__ == '__main__':
    r = sr.Recognizer()
    # Read sound file
    # sound_file = AudioSegment.from_file('out_file/genevieve.wav')
    video = VideoFileClip('video/test.mp4')
    audio = video.audio
    audio.write_audiofile('video/test.mp3')
    sound_file = AudioSegment.from_file('video/test.mp3')

    min_silence_len = 600
    silence_thresh = -65

    # Cut audio, get 3 lists of pieces, start time and end time
    pieces, start_t, end_t = split_on_silence(sound_file, min_silence_len, silence_thresh)

    pieces_to_wav(pieces)
    for inx, val in enumerate(pieces):
        # get text
        text = audio_to_text('%d.wav' % inx)
        # print(text)
        text_2 = text_to_str(inx, text, start_t[inx], end_t[inx])
        str_to_file(text_2)
        print(str((inx * 100 / len(pieces))) + '%')
