import json
import csv
import pandas

with open('skinship_text.psb.m.json', 'r') as f:
    data = json.load(f)

texts = []
for key1, value1 in data.items():
    for key2, value2 in value1.items():
        for item in value2: 
            texts.append(item['text'].replace('\n', '\\n'))

df = pandas.DataFrame({'ogtextss': texts})

df.to_csv('skinship_text.psb.m.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)