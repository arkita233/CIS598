import pandas as pd
import json
import codecs

csv_data = pd.read_csv("train_cleaned.csv")
csv_data = csv_data.drop(columns='Unnamed: 0')

print(csv_data.head())

path = []
du = []
t = []
d = []

path = csv_data.audio_filepath
du = csv_data.duration
t = csv_data.text

k = 0
while k < len(csv_data):
    if du[k] != "error":
        dic = {"audio_filepath": path[k], "duration": du[k], "text": t[k]}
        d.append(json.dumps(dic))
    k += 1

filename = 'manifest.train'
with codecs.open(filename, 'w', 'utf-8') as f:
    for i in d:
        f.write(str(i) + '\n')
