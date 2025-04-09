import whisper
import tempfile

model = whisper.load_model("base")  # tu peux tester avec "small", "medium"...

def transcribe_audio(audio_bytes):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp:
        temp.write(audio_bytes)
        temp.flush()
        result = model.transcribe(temp.name)
        return result['text']
