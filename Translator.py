from google_trans_new import google_translator

def translategl(text):
    translator = google_translator()
    translation = translator.translate(text, lang_tgt='en')
    print(f"Translated Text: {translation}")
    return translation
