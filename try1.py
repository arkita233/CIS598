# audio process Pydub
# Need ffmpeg
from pydub import AudioSegment
from pydub.silence import split_on_silence


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


def text_to_sub(index, text, start_time, end_time):
    string_sub = index + '\n' + start_time + ' --> ' + end_time + '\n' + text + '\n\n'
    return string_sub


# Read sound file
sound_file = AudioSegment.from_file('genevieve.wav')

min_silence_len = 660
silence_thresh = -36
# Cut audio, get 3 lists of pieces, start time and end time
pieces, start_t, end_t = split_on_silence(sound_file, min_silence_len, silence_thresh)

pieces_to_wav(pieces)
