"""
File: app.py
A simple web-based application
for Bahasa Indonesia - Basa Sunda translation

Author : William Fu
"""
from flask import Flask, request, render_template
from translate import dictionary, translator


# Initialize a Flask application
app = Flask(__name__)

# Initialize translator for Bahasa Indonesia - Basa Sunda and vice versa
ind_to_sunda = translator.Translator(dictionary.create_dictionary("./res/indonesia.txt"))
sunda_to_ind = translator.Translator(dictionary.create_dictionary("./res/sunda.txt"))
    
# Initialize stopwords
ind_stopwords = ["sih", "deh", "kah", "lah", "pun", "tah", "loh", "lho"]
sun_stopwords = ["teh", "tea", "mah"]
ind_to_sunda.set_stopwords(ind_stopwords)
sunda_to_ind.set_stopwords(sun_stopwords)


@app.route("/", methods=['GET', 'POST'])
def home():
    """ Tampilan utama aplikasi translator """
    
    global ind_to_sunda
    global sunda_to_ind
    
    result = "Terjemahan disini . . ."

    if request.form.get("text") and request.form.get("lang") and request.form.get("alg") :
        
        alg = str(request.form.get("alg"))
        text = str(request.form.get("text"))


        if request.form.get("lang") == "ind":
            ind_to_sunda.set_text(text[27:])
            result = ind_to_sunda.translate_text(alg)
        else:
            sunda_to_ind.set_text(text[27:])
            result = sunda_to_ind.translate_text(alg)

    return render_template("index.html", translation=result)


if __name__ == "__main__":
    app.run(debug=True)
