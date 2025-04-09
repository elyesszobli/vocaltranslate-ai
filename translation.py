from deep_translator import GoogleTranslator

def translate_text(text, target="en"):
    return GoogleTranslator(source='auto', target=target).translate(text)
