# Magic Deck Analyzer

Um programa em Python para analisar decks de Magic: The Gathering a partir de arquivos `.txt` ou entrada manual.

Ele permite:

- Carregar decks de arquivos `.txt`.
- Analisar o deck separando cartas por tipo (lands, criaturas, instants, sorceries, artifacts, enchantments).
- Detectar automaticamente o tipo de deck (Aggro, Midrange ou Controle).
- Visualizar estatísticas detalhadas do deck.

## Estrutura do Projeto

magic-deck-analyzer/
│
├─ decks/ # arquivos .txt com decks
├─ deck_source.py # funções para carregar decks
├─ analyzer.py # funções para analisar decks
├─ main.py # interface principal
└─ README.md # documentação

### Formato dos arquivos `.txt`

- Primeira linha opcional indicando as cores do deck:

colors: WU

- Linhas seguintes indicando quantidade, nome e tipo da carta:

20 Plains, land
4 Ethereal Armor, enchantment
4 Spellbook Vendor, creature

> Caso o tipo da carta não seja informado, será classificado como `non-classified`.

---

## Como usar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/magic-deck-analyzer.git
cd magic-deck-analyzer
Coloque seus decks na pasta decks/.

Execute o programa:

python main.py
Siga as opções do menu:

1 - Ver decks populares da pasta decks.

2 - Colar deck manualmente.

0 - Sair.

Exemplo de saída
Deck: MyDeck
Cores: W, U
Total de cartas: 60
Lands: 24
Criaturas: 20
Instants: 4
Sorceries: 4
Artifacts: 2
Enchantments: 6
Não classificados: 0
Tipo de deck: Aggro
Dependências
Python 3.x (não requer bibliotecas externas)
```
