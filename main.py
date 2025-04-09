from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from transcription import transcribe_audio
from translation import translate_text

app = FastAPI()

# Autoriser les appels de ton backend Spring Boot
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tu peux restreindre plus tard
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Transcrire
    original = transcribe_audio(contents)
    
    # Traduire
    translated = translate_text(original)
    
    return {"original": original, "translated": translated}
