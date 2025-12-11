import pandas as pd
import os
import json

ARQUIVO = "historico_vendas.xlsx"

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

    if os.path.exists(ARQUIVO):
        df_existente = pd.read_excel(ARQUIVO, sheet_name="Vendas")
        df_final = pd.concat([df_existente, df_semana], ignore_index=True)
    else:
        df_final = df_semana

    # escrever planilha
    with pd.ExcelWriter(ARQUIVO, engine="xlsxwriter") as writer:
        df_dados = pd.read_excel(ARQUIVO, sheet_name="Dados")
        df_dados.to_excel(writer, sheet_name="Dados", index=False)

        df_final.to_excel(writer, sheet_name="Vendas", index=False)

        # gráfico
        workbook = writer.book
        ws = workbook.add_worksheet("Gráfico")

        resumo = df_final[df_final["Produto"] == "TOTAL"][["Semana", "Faturamento", "Lucro"]]

        ws.write_row(0, 0, ["Semana", "Faturamento", "Lucro"])
        for i, row in resumo.iterrows():
            ws.write(i+1, 0, row["Semana"])
            ws.write(i+1, 1, row["Faturamento"])
            ws.write(i+1, 2, row["Lucro"])

        chart1 = workbook.add_chart({"type": "column"})
        chart1.add_series({
            "categories": ["Gráfico", 1, 0, len(resumo), 0],
            "values": ["Gráfico", 1, 1, len(resumo), 1],
            "name": "Faturamento"
        })
        ws.insert_chart("E2", chart1)

        chart2 = workbook.add_chart({"type": "column"})
        chart2.add_series({
            "categories": ["Gráfico", 1, 0, len(resumo), 0],
            "values": ["Gráfico", 1, 2, len(resumo), 2],
            "name": "Lucro"
        })
        ws.insert_chart("E20", chart2)

    print(f"✔ Semana '{semana}' adicionada.")


# -----------------------------------------------------
# EXECUÇÃO
# -----------------------------------------------------
# encontrar JSON existente
jsons = [f for f in os.listdir() if f.startswith("relatorio_") and f.endswith(".json")]

if not jsons:
    print("❌ Nenhum JSON encontrado. Rode o Programa 1 antes.")
    exit()

arquivo = jsons[0]  # pega o mais recente
data_prevista = arquivo.replace("relatorio_", "").replace(".json", "")

with open(arquivo, "r", encoding="utf-8") as f:
    relatorio_semana = json.load(f)

# criar planilha 1x
if not os.path.exists(ARQUIVO):
    produtos_info = {
        "banana maçã": {"compra": 5, "venda": 12},
        "banana prata": {"compra": 4, "venda": 10},
        "maçã gala": {"compra": 6, "venda": 14}
    }
    criar_aba_dados(produtos_info)

registrar_vendas(relatorio_semana, data_prevista)
