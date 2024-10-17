# # First, ensure you have the lingua library installed:
# # pip install lingua-language-detector

# from lingua import Language, LanguageDetectorBuilder

# # Define the languages you want to detect
# languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]

# # Build the language detector
# detector = LanguageDetectorBuilder.from_languages(*languages).build()

# # Example text to detect language
# text = "hii my name is yogesh."

# # Detect the language
# detected_language = detector.detect_language_of(text)

# # Output the detected language
# if detected_language:
#     print(f"Detected language: {detected_language.name} (ISO 639-1: {detected_language.iso_code_639_1})")
# else:
#     print("Language could not be reliably detected.")
from flask import Flask, render_template, request
from lingua import Language, LanguageDetectorBuilder

app = Flask(__name__)

# Define the languages you want to detect
languages = [
    Language.ENGLISH,
    Language.FRENCH,
    Language.GERMAN,
    Language.SPANISH,
    Language.ITALIAN,
    Language.RUSSIAN,
    Language.CHINESE,
    Language.JAPANESE,
]

# Build the language detector
detector = LanguageDetectorBuilder.from_languages(*languages).build()

@app.route('/', methods=['GET', 'POST'])
def index():
    detected_language = None
    if request.method == 'POST':
        text = request.form['text']
        detected_language = detector.detect_language_of(text)
    return render_template('index.html', detected_language=detected_language)

if __name__ == '__main__':
    app.run(debug=True)
