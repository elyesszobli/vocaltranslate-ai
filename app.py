from fastapi import FastAPI, File, UploadFile, Query
from transcription import transcribe_audio
from translation import translate_text

app = FastAPI()

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...), target_lang: str = Query("fr")):
    audio_path = f"temp_{file.filename}"

    with open(audio_path, "wb") as buffer:
        buffer.write(await file.read())

    original = transcribe_audio(audio_path)
    translated = translate_text(original, target_lang)

    return {
        "original_text": original,
        "translated_text": translated,
        "target_language": target_lang
    }
