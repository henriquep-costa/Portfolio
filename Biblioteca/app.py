import json
import os
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')

def home():
    if os.path.exists("biblioteca.json"):
        with open("biblioteca.json", "r") as f:
            livros = json.load(f)
    else:
        livros = []
    return render_template("index.html", livros=livros)


@app.route("/add", methods=["POST"])

def add_livro():
     
     if os.path.exists("biblioteca.json"):
        with open("biblioteca.json", "r") as f:
            livros = json.load(f)
     else:
        livros = []

    titulo = request.form["titulo"]
    autor = request.form["autor"]
    livros.append({"titulo": titulo, "autor": autor})
    with open("biblioteca.json", "w") as f:
        json.dump(livros, f, indent=4)
    return redirect("/")
 

if __name__ == '__main__':    app.run(debug=True)