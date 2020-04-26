import pandas as pd


csv_data = pd.read_csv("train.csv")

print(csv_data.head())

csv_data["text"] = csv_data["text"].str.replace(r'[^\w\s\']+', '')
csv_data["text"] = csv_data["text"].str.lower()

csv_data = csv_data.drop(columns='Unnamed: 0')

csv_data.to_csv("train_cleaned.csv")

print(csv_data.head())