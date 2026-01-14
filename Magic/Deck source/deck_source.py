# deck_source.py

import os

# Pasta onde os arquivos .txt de decks estão
DECKS_FOLDER = "decks"

# -----------------------------------------
# Função para listar todos os arquivos .txt na pasta
# -----------------------------------------
def list_deck_files() -> list:
    """
    Retorna uma lista com todos os arquivos .txt dentro da pasta DECKS_FOLDER
    """
    return [
        f for f in os.listdir(DECKS_FOLDER)
        if f.endswith(".txt")
    ]

# -----------------------------------------
# Função principal para carregar um deck de um arquivo .txt
# -----------------------------------------
def load_deck_from_txt(filename: str) -> dict:
    """
    Carrega um deck a partir de um arquivo .txt.

    Formato do arquivo:
        # colors: WU
        20 Plains, land
        4 Ethereal Armor, enchantment
        4 Spellbook Vendor, creature
        ...

    Cada linha com quantidade, nome da carta, tipo separado por vírgula.
    """
    path = os.path.join(DECKS_FOLDER, filename)  # caminho completo do arquivo

    cards = []          # lista que vai armazenar todas as cartas
    colors = ["?"]      # cores do deck (padrão "?") caso não exista a linha de cores

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()  # remove espaços extras

            if line == "":
                continue  # pula linhas vazias

            # -----------------------
            # Lê a linha de cores do deck
            # -----------------------
            if line.startswith("#"):
                if line.lower().startswith("# colors:"):
                    # Pega tudo que vem depois do ":" e transforma em lista de letras
                    colors = list(line.split(":", 1)[1].strip())
                continue  # pula para a próxima linha depois de ler cores

            # -----------------------
            # Lê o nome e tipo da carta
            # -----------------------
            # Agora esperamos linhas com vírgula separando nome e tipo
            parts = line.split(",", 1)
            if len(parts) == 2:
                left = parts[0].strip()      # "quantidade nome"
                card_type = parts[1].strip().lower()  # tipo da carta
            else:
                left = line
                card_type = "non-classified"  # caso não informe tipo

            # Separar quantidade e nome da carta
            left_parts = left.split(" ", 1)
            if len(left_parts) != 2:
                continue  # ignora linhas mal formatadas

            qty = int(left_parts[0])  # quantidade de cópias
            card_name = left_parts[1] # nome da carta

            # Adiciona a carta à lista, repetindo conforme a quantidade
            for _ in range(qty):
                cards.append({
                    "name": card_name,
                    "type": card_type
                })

    # -----------------------
    # Separar lands do resto das cartas
    # -----------------------
    lands = [c for c in cards if c["type"] == "land"]
    non_lands = [c for c in cards if c["type"] != "land"]

    # Retorna um dicionário com todas as informações do deck
    return {
        "name": filename.replace(".txt", ""),  # nome do deck (sem .txt)
        "colors": colors,                       # cores do deck
        "cards": cards,                         # lista completa d
    }