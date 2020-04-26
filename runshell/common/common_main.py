import mutagen
import pandas as pd
from mutagen.mp3 import MP3

audio_path = "/home/sixiangz/DeepSpeech/dataset/en/clips/"

tsv = pd.read_csv('/home/sixiangz/DeepSpeech/dataset/en/train.tsv', sep='\t')

print(tsv.head())
path = []
dur = []
tex = []
err = []

p = 0
c = 0.0
# song = mediainfo("common_voice_en_18540003.mp3")
# print(song['duration'])

for i in tsv.path:
    st = "./dataset/en/clips/" + i
    path.append(st)
print("path done")

for i in tsv.sentence:
    tex.append(i)
print("tex done")

for i in tsv.path:
    c+=1
    st2 = audio_path + i
    audio_filepath = st2
    try:
        audio = MP3(st2)
    except mutagen.mp3.HeaderNotFoundError:
        dur.append("error")
    else:
        dur.append(audio.info.length)


    p = c*100/len(tsv)
    print('{:.2f}%'.format(p))
print("dur done")

data = {"audio_filepath": path, "text": tex, "duration": dur}

frame = pd.DataFrame(data)
frame.to_csv("train.csv")




# {"audio_filepath": "./dataset/librispeech/dev-clean/LibriSpeech/dev-clean/1272/128104/1272-128104-0000.flac",
# "duration": 5.855, "text": "mister quilter is the apostle of the middle classes and we are glad to welcome his
# gospel"}
