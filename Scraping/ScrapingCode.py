import requests
import pickle
with open('files.pickle', 'rb') as f:
    filen = pickle.load(f)
with open('names.pickle', 'rb') as f:
    names = pickle.load(f)

for i in range(len(filen)):
    r = requests.get(filen[i])
    with open('/Users/Flags/Desktop/State Crime/Dataset/Excels/' + names[i] + '.xlsx', 'wb') as f:
        f.write(r.content)