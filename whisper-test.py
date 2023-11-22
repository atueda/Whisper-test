import whisper

def post_process_transcription(text):
    # この例では何も処理を行わず、そのままテキストを返します。
    return text

# whisper モデルを読み込みます
model = whisper.load_model("large")
lang = "ja"

# Load audio
audio = whisper.load_audio("/Users/atsushi.ueda/Whisper/CorporateMessage_2023-11-21.mp4")

result = model.transcribe(audio, verbose=True, language=lang)

# Write into a text file
fileName = "test"
with open(f"/Users/atsushi.ueda/Whisper/{fileName}.txt", "w") as f:
  f.write(f"▼ Transcription of {fileName}\n")
  f.write(result["text"])
