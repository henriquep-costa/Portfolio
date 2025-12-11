import requests
import json
from datetime import datetime
import os

API_KEY = "SUA_API_KEY_AQUI"
CIDADE = "São Paulo"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

produtos_info = {
    "banana maçã": {"compra": 5, "venda": 12},
    "banana prata": {"compra": 4, "venda": 10},
    "maçã gala": {"compra": 6, "venda": 14}
}


# -------------------------------------------
# PEGAR PREVISÃO DO FINAL DE SEMANA
# -------------------------------------------
def pegar_previsao():
    resposta = requests.get(URL)
    dados = resposta.json()

    lista = dados["list"]

    # pegar previsão para sábado às 12h
    dia_previsto = None
    previsao_escolhida = None

    for item in lista:
        data_txt = item["dt_txt"]  # exemplo: 2025-12-13 12:00:00
        dia = datetime.strptime(data_txt, "%Y-%m-%d %H:%M:%S")

        if dia.weekday() == 5 and dia.hour == 12:  # sábado 12h
            dia_previsto = dia.strftime("%Y-%m-%d")
            previsao_escolhida = item
            break

    if previsao_escolhida is None:
        print("Não encontrou previsão para sábado.")
        exit()

    descricao = previsao_escolhida["weather"][0]["description"]
    temperatura = previsao_escolhida["main"]["temp"]
    chuva_mm = previsao_escolhida.get("rain", {}).get("3h", 0)
    chuva_pct = previsao_escolhida.get("pop", 0) * 100

    previsao = {
        "data_prevista": dia_previsto,
        "descricao": descricao,
        "temperatura": temperatura,
        "chuva_mm": chuva_mm,
        "chuva_pct": chuva_pct
    }

    return previsao


# -------------------------------------------
# COLETAR KG DOS PRODUTOS
# -------------------------------------------
def coletar_kg():
    relatorio = []

    for nome, preco in produtos_info.items():
        kg = float(input(f"Quantos kg de '{nome}' foram vendidos? "))

        faturamento = kg * preco["venda"]
        custo = kg * preco["compra"]
        lucro = faturamento - custo

        relatorio.append({
            "Produto": nome,
            "Kg": kg,
            "Faturamento": faturamento,
            "Lucro": lucro
        })

    return relatorio


# -------------------------------------------
# GERAR HTML
# -------------------------------------------
def gerar_html(previsao, relatorio):
    data = previsao["data_prevista"]

    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial;
                margin: 40px;
            }}
            .titulo {{
                font-size: 22px;
                font-weight: bold;
            }}
            .produto {{
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="titulo">Previsão para {data} - São Paulo</div>
        <p><b>Descrição:</b> {previsao["descricao"]}</p>
        <p><b>Temperatura:</b> {previsao["temperatura"]}°C</p>
        <p><b>Chuva:</b> {previsao["chuva_mm"]} mm ({previsao["chuva_pct"]:.0f}%)</p>

        <hr>

        <div class="titulo">Relatório de Vendas</div>
    """

    for item in relatorio:
        html += f"""
            <div class="produto">
                <b>{item['Produto']}</b> — {item['Kg']} kg  
                | Fat.: R${item['Faturamento']:.2f}  
                | Lucro: R${item['Lucro']:.2f}
            </div>
        """

    total_fat = sum(x["Faturamento"] for x in relatorio)
    total_luc = sum(x["Lucro"] for x in relatorio)

    html += f"""
        <hr>
        <h3>Total Faturamento: R${total_fat:.2f}</h3>
        <h3>Total Lucro: R${total_luc:.2f}</h3>
    </body>
    </html>
    """

    nome_arquivo = f"relatorio_{data}.html"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✔ HTML gerado: {nome_arquivo}")
    return nome_arquivo


# -------------------------------------------
# SALVAR JSON (para o Programa 2)
# -------------------------------------------
def salvar_json(previsao, relatorio):
    nome_json = f"relatorio_{previsao['data_prevista']}.json"

    with open(nome_json, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, ensure_ascii=False, indent=4)

    print(f"✔ JSON gerado: {nome_json}")


# -------------------------------------------
# EXECUÇÃO PRINCIPAL
# -------------------------------------------
previsao = pegar_previsao()
relatorio = coletar_kg()
gerar_html(previsao, relatorio)
salvar_json(previsao, relatorio)

print("\n✔ Programa 1 finalizado.")
