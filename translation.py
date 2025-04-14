from deep_translator import GoogleTranslator

def translate_text(text: str, target_lang: str = "fr") -> str:
    try:
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except Exception as e:
        return f"Translation failed: {e}"
