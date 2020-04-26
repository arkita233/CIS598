from pydub import AudioSegment
import pandas as pd

audio_path = "/home/sixiangz/DeepSpeech/dataset/en/clips/"

tsv = pd.read_csv('/home/sixiangz/DeepSpeech/dataset/en/train.tsv', sep='\t')

c = 0.0
for i in tsv.path:
    c += 1
    file_name = i[:-3]
    src = audio_path+i
    dst = file_name + "wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    p = c * 100 / len(tsv)
    print('{:.2f}%'.format(p))
