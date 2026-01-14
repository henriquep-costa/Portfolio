from deck_source import list_deck_files, load_deck_from_txt
from analyzer import analyze_deck, format_analysis

def show_menu():
    print("\nMagic Deck Analyzer")
    print("-------------------")
    print("1 - Ver decks populares (Standard BO1)")
    print("2 - Colar deck manualmente")
    print("0 - Sair")


def pause():
    input("\nPressione Enter para continuar...")


def read_manual_deck():
    print("\nCole seu deck abaixo.")
    print("Uma carta por linha. Linha vazia para finalizar.\n")

    cards = []

    while True:
        line = input()
        if line.strip() == "":
            break

        card_type = "creature" if "creature" in line.lower() else "non-creature"

        cards.append({
            "name": line,
            "type": card_type
        })

    return {
        "name": "Deck Manual",
        "colors": ["?"],
        "cards": cards
    }


def main():
    while True:
        show_menu()
        choice = input("\nEscolha uma opção: ")

        if choice == "1":
            files = list_deck_files()

            if not files:
                print("Nenhum deck encontrado.")
                pause()
                continue

            print("\nDecks disponíveis:\n")
            for i, filename in enumerate(files):
                print(f"{i + 1} - {filename}")

            deck_choice = input("\nEscolha um deck pelo número: ")

            if not deck_choice.isdigit():
                print("Digite apenas números.")
                pause()
                
                continue

            index = int(deck_choice) - 1

            if index < 0 or index >= len(files):
                print("Número fora da lista.")
                pause()
                continue

            deck = load_deck_from_txt(files[index])

            analysis = analyze_deck(deck)
            text = format_analysis(analysis)

            print("\n=== ANÁLISE DO DECK ===")
            print(text)
            pause()


        elif choice == "2":
            deck = read_manual_deck()

            if len(deck["cards"]) == 0:
                print("Nenhuma carta inserida.")
                pause()
                continue

            analysis = analyze_deck(deck)
            text = format_analysis(analysis)

            print("\n=== ANÁLISE DO DECK ===")
            print(text)
            pause()

        elif choice == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")
            pause()


if __name__ == "__main__":
    main()
