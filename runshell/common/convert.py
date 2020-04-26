from pydub import AudioSegment
import pandas as pd

audio_path = "/home/sixiangz/DeepSpeech/dataset/en/clips/"

tsv = pd.read_csv('/home/sixiangz/DeepSpeech/dataset/en/train.tsv', sep='\t')
print(len(tsv))
k = 0.0
c = 0.0

while k < 20000:
    i = tsv.path[k]
    file_name = i[:-3]
    src = audio_path + i
    dst = audio_path + file_name + "wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    p = k * 100 / 20000
    print('{:.2f}%'.format(p))
    k+=1