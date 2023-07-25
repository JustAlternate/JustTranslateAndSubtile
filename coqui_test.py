from TTS.api import TTS

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
# models = TTS.list_models()
# print(models)

tts = TTS("tts_models/en/ljspeech/vits")

f = open("output.txt", "r")
lines = f.readlines()
entire_text = ""
for line in lines:
    entire_text += line
print(entire_text)
f.close()

tts.tts_to_file(text=entire_text,
                file_path="final.wav")
