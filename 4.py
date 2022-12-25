import requests
import wave
import json
API_URL = "https://api-inference.huggingface.co/models/vodiylik/xls-r-uzbek-cv10-full"
API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

output = query("lemaster_tech.flac")
# output = query("ccc.wav")
print(output)