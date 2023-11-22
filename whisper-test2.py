import whisper

def post_process_transcription(text):
    # この例では何も処理を行わず、そのままテキストを返します。
    return text

# whisper モデルを読み込みます
model = whisper.load_model("large")

# ファイルを読み込んで文字起こしを実行します
result = model.transcribe("/Users/atsushi.ueda/Whisper/CorporateMessage_2023-11-21.mp4")

# 出力ファイルを開きます（'output.txt'は任意のファイル名に変更可能）
with open('output.txt', 'w') as f:
    # セグメントごとに表示
    for seg in result["segments"]:
        text = seg["text"]
        # ポストプロセッシング関数を適用
        processed_text = post_process_transcription(text)
        
        # テキストをファイルに書き込みます
        f.write(processed_text + '\n')
        
        # コンソールにも表示します
        print(processed_text)