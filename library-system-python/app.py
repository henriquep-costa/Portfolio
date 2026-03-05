from core import load_books, add_books
from flask import Flask, request, redirect, render_template

NOME_ARQUIVO = "biblioteca.json"

app = Flask(__name__)

@app.route('/')

def home():
    
    livros = load_books(NOME_ARQUIVO)

    return render_template("index.html", livros=livros)


@app.route("/add", methods=["POST"])

def add_livro():
   
    titulo = request.form["titulo"]
    autor = request.form["autor"]
    add_books(NOME_ARQUIVO, titulo, autor)
    return redirect("/")
 

if __name__ == '__main__':    app.run(debug=True)