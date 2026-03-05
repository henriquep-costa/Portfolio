# pip install XlsxWriter
# pip install openpyxl

import pandas as pd
import os
import json

ARQUIVO = "historico_vendas.xlsx"

# -----------------------------------------------------
# Produtos atuais
# -----------------------------------------------------
produtos_info = {
    "banana maçã": {"compra": 5, "venda": 12},
    "banana prata": {"compra": 4, "venda": 12},
    "banana nanica": {"compra": 4, "venda": 12},
    "mamao": {"compra": 7, "venda": 10},
    "abacate": {"compra": 7, "venda": 10},
    "limao": {"compra": 4, "venda": 7},
}

# -----------------------------------------------------
# Criar aba Dados
# -----------------------------------------------------
def criar_aba_dados(produtos_info):
    df_dados = pd.DataFrame([
        {"Produto": nome,
         "Preço Compra (kg)": info["compra"],
         "Preço Venda (kg)": info["venda"]}
        for nome, info in produtos_info.items()
    ])

    with pd.ExcelWriter(ARQUIVO, engine="xlsxwriter") as writer:
        df_dados.to_excel(writer, sheet_name="Dados", index=False)
        writer.book.add_worksheet("Vendas")
        writer.book.add_worksheet("Gráfico")

    print("✔ Planilha criada.")

# -----------------------------------------------------
# Registrar vendas da semana
# -----------------------------------------------------
def registrar_vendas(relatorio_semana, data_prevista):
    semana = f"Semana {data_prevista}"

    df_semana = pd.DataFrame(relatorio_semana)
    df_semana["Semana"] = semana

    total_fat = df_semana["Faturamento"].sum()
    total_luc = df_semana["Lucro"].sum()

    df_total = pd.DataFrame([{
        "Semana": semana,
        "Produto": "TOTAL",
        "Kg": "",
        "Faturamento": total_fat,
        "Lucro": total_luc
    }])

    df_semana = pd.concat([df_semana, df_total], ignore_index=True)

    # Carregar existente e remover semana duplicada
    if os.path.exists(ARQUIVO):
        df_existente_vendas = pd.read_excel(ARQUIVO, sheet_name="Vendas", engine="openpyxl")
        df_existente_vendas = df_existente_vendas[df_existente_vendas["Semana"] != semana]
        df_final = pd.concat([df_existente_vendas, df_semana], ignore_index=True)
    else:
        df_final = df_semana

    # Escrever planilha com gráficos
    with pd.ExcelWriter(ARQUIVO, engine="xlsxwriter") as writer:
        # aba Dados
        df_dados = pd.DataFrame([
            {"Produto": nome,
             "Preço Compra (kg)": info["compra"],
             "Preço Venda (kg)": info["venda"]}
            for nome, info in produtos_info.items()
        ])
        df_dados.to_excel(writer, sheet_name="Dados", index=False)

        # aba Vendas
        df_final.to_excel(writer, sheet_name="Vendas", index=False)

        # aba Gráfico
        workbook = writer.book
        ws = workbook.add_worksheet("Gráfico")

        # pegar só TOTAL para gráfico
        resumo = df_final[df_final["Produto"] == "TOTAL"][["Semana", "Faturamento", "Lucro"]]

        # cabeçalho
        ws.write_row(0, 0, ["Semana", "Faturamento", "Lucro"])
        for i, row in resumo.iterrows():
            ws.write(i+1, 0, row["Semana"])
            ws.write(i+1, 1, row["Faturamento"])
            ws.write(i+1, 2, row["Lucro"])

        # gráfico Faturamento
        chart1 = workbook.add_chart({"type": "column"})
        chart1.add_series({
            "categories": ["Gráfico", 1, 0, len(resumo), 0],
            "values": ["Gráfico", 1, 1, len(resumo), 1],
            "name": "Faturamento",
        })
        chart1.set_title({"name": "Faturamento Semanal"})
        ws.insert_chart("E2", chart1)

        # gráfico Lucro
        chart2 = workbook.add_chart({"type": "column"})
        chart2.add_series({
            "categories": ["Gráfico", 1, 0, len(resumo), 0],
            "values": ["Gráfico", 1, 2, len(resumo), 2],
            "name": "Lucro",
        })
        chart2.set_title({"name": "Lucro Semanal"})
        ws.insert_chart("E20", chart2)

    print(f"✔ Semana '{semana}' registrada com sucesso e gráfico atualizado.")

# -----------------------------------------------------
# EXECUÇÃO
# -----------------------------------------------------
# encontrar JSON mais recente
jsons = [f for f in os.listdir() if f.startswith("relatorio_") and f.endswith(".json")]

if not jsons:
    print("❌ Nenhum JSON encontrado. Rode o Programa 1 antes.")
    exit()

arquivo = sorted(jsons)[-1]  # pega o mais recente
data_prevista = arquivo.replace("relatorio_", "").replace(".json", "")

with open(arquivo, "r", encoding="utf-8") as f:
    relatorio_semana = json.load(f)

# criar planilha 1x
if not os.path.exists(ARQUIVO):
    criar_aba_dados(produtos_info)

registrar_vendas(relatorio_semana, data_prevista)
