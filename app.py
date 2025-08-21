# app.py
from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        input_text = request.form["input_text"]
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]

        try:
            translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(input_text)
        except Exception as e:
            translated_text = f"Error: {str(e)}"

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
