import requests
import json
import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np
from playsound import playsound


FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

pa = pyaudio.PyAudio()

stream = pa.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

playsound('25-Dec_-14.28_.mp3')

print('start recording')

seconds = 5
frames = []
second_tracking = 0
second_count = 0
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)
    second_tracking += 1
    if second_tracking == RATE/FRAMES_PER_BUFFER:
        second_count += 1
        second_tracking = 0
        print(f'Time Left: {seconds - second_count} seconds')


stream.stop_stream()
stream.close()
pa.terminate()

obj = wave.open('lemaster_tech.flac', 'wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(pa.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b''.join(frames))
obj.close()


file = wave.open('lemaster_tech.flac', 'rb')

sample_freq = file.getframerate()
frames = file.getnframes()
signal_wave = file.readframes(-1)

file.close()
API_URL = "https://api-inference.huggingface.co/models/vodiylik/xls-r-uzbek-cv10-full"
API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

output = query("lemaster_tech.flac")






AI = output['text'].split()
print(AI)

if 'boshqa' in AI or 'raqamga' in AI:
    # playsound('yulduzcha.mp3')
    print("Javob yulduzcha yulduzcha yigirma bir va so'ng plus va telefon raqami mamlakat kodi bilan kiritasiz va oxirida panjara va qo'ng'iroq tugmasini bosing")



elif 'diyas' in AI or 'tez' in AI or 'nima' in AI:
    # playsound('deis.mp3')
    print('Men avtamatiklashtirilgan suniy intelektga assolangan koll sentrman')


elif 'ishlab' in AI or 'chiqqan' in AI:
    playsound('men_suniy_entilukt.mp3')



elif 'tariflar' in AI:
#    playsound('abenet_tulov.mp3')
    print("Abanent to'lovi bir yuzi to'qqizming so'm evaziga yigirma megabayt sekundiga va bir yuzi sakson daqiqa qo'ng'iroq qilish imkoniga ega bo'lasiz")


elif 'uztelecom' in AI or 'haqida' in AI:
    # playsound('uztelecom.mp3')
    print("O'zbektelekom” aksiyadorlik kompaniyasi O'zbekistondagi eng yirik telekommunikatsiya operatori bo'lib, o'z tarmog'i bilan butun respublika hududini qamrab oladi.")


else:
    print("Bizda unaqa savol haqaida malumot yuq")