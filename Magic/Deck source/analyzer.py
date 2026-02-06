# analyzer.py

def analyze_deck(deck: dict) -> dict:
    """
    Analisa um deck carregado e separa por tipo de carta:
    land, creature, instant, sorcery, artifact, enchantment
    """
    cards = deck.get("cards", [])

    # Separação por tipo
    lands = [c for c in cards if c["type"] == "land"]
    creatures = [c for c in cards if c["type"] == "creature"]
    instants = [c for c in cards if c["type"] == "instant"]
    sorceries = [c for c in cards if c["type"] == "sorcery"]
    artifacts = [c for c in cards if c["type"] == "artifact"]
    enchantments = [c for c in cards if c["type"] == "enchantment"]
    non_classified = [c for c in cards if c["type"] not in ["land", "creature", "instant", "sorcery", "artifact", "enchantment"]]

    total_cards = len(cards)

    deck_type = detect_deck_type(
        total_cards=total_cards,
        creatures=len(creatures),
        non_creatures=len(cards) - len(creatures) - len(lands),
        lands=len(lands)
    )

    return {
        "deck_name": deck.get("name", "Unknown"),
        "colors": deck.get("colors", ["?"]),
        "total_cards": total_cards,
        "lands": len(lands),
        "creatures": len(creatures),
        "instants": len(instants),
        "sorceries": len(sorceries),
        "artifacts": len(artifacts),
        "enchantments": len(enchantments),
        "non_classified": len(non_classified),
        "deck_type": deck_type,
        "creature_list": creatures,
        "land_list": lands,
        "instant_list": instants,
        "sorcery_list": sorceries,
        "artifact_list": artifacts,
        "enchantment_list": enchantments,
        "non_classified_list": non_classified
    }


def format_analysis(analysis: dict) -> str:
    """
    Formata a análise do deck em texto para exibição.
    """
    name = analysis["deck_name"]
    colors = ", ".join(analysis["colors"])
    total = analysis["total_cards"]
    deck_type = analysis["deck_type"]

    text = (
        f"Deck: {name}\n"
        f"Cores: {colors}\n"
        f"Total de cartas: {total}\n"
        f"Lands: {analysis['lands']}\n"
        f"Criaturas: {analysis['creatures']}\n"
        f"Instants: {analysis['instants']}\n"
        f"Sorceries: {analysis['sorceries']}\n"
        f"Artifacts: {analysis['artifacts']}\n"
        f"Enchantments: {analysis['enchantments']}\n"
        f"Não classificados: {analysis['non_classified']}\n"
        f"Tipo de deck: {deck_type}"
    )

    return text


def detect_deck_type(total_cards, creatures, non_creatures, lands):
    """
    Define o tipo de deck baseado em criaturas, não-criaturas e lands.
    Exemplo simples, pode ser refinado depois.
    """
    if creatures >= 20 and non_creatures <= 10:
        return "Aggro"
    elif creatures >= 14 and non_creatures >= 10:
        return "Midrange"
    else:
        return "Controle"
