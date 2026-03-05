# Previsão e Registro de Vendas de Orgânicos

Este projeto em Python auxilia pequenas empresas ou feiras a **prever vendas de produtos orgânicos** e **registrar resultados semanais** em uma planilha Excel com gráficos. Ele é composto por dois programas:

1. **Programa 1**: Coleta previsão do tempo e registra kg vendidos, faturamento e lucro em HTML e JSON.
2. **Programa 2**: Lê o JSON gerado e registra as vendas semanais em uma planilha Excel, criando gráficos de faturamento e lucro.

---

## Estrutura do Projeto

previsao-vendas-organicos/
│
├─ programa1.py # coleta dados de vendas + previsão do tempo, gera HTML e JSON
├─ programa2.py # registra vendas semanais em Excel e gera gráficos
└─ README.md # documentação

> Opcional: criar uma pasta `relatorios/` para organizar os HTML e JSON gerados.

---

## Programa 1 — Coleta de Vendas e Previsão do Tempo

### Funcionalidades

- Consulta a **previsão do tempo** para sábado às 12h usando a API do OpenWeatherMap.
- Coleta a quantidade em kg de cada produto orgânico.
- Calcula **faturamento e lucro** de cada produto.
- Gera:
  - Um arquivo **HTML** com o relatório completo.
  - Um arquivo **JSON** para uso posterior no Programa 2.

### Produtos monitorados

```text
- banana maçã
- banana prata
- banana nanica
- mamão
- abacate
- limão
Como usar
python programa1.py
Siga as instruções para inserir os kg vendidos de cada produto.

Programa 2 — Registro em Excel
Funcionalidades
Lê o JSON gerado pelo Programa 1.

Cria uma planilha historico_vendas.xlsx com três abas:

Dados — preços de compra e venda dos produtos.

Vendas — registro semanal com faturamento e lucro.

Gráfico — gráficos de faturamento e lucro por semana.

Atualiza a planilha com novas semanas sem duplicar registros.

Como usar
python programa2.py
Certifique-se de que existe um JSON gerado pelo Programa 1 antes de rodar.

Dependências
pandas

XlsxWriter

openpyxl

Instalação:

pip install pandas XlsxWriter openpyxl
Exemplo de saída
HTML gerado pelo Programa 1:
Previsão para 2026-02-07 - São Paulo
Descrição: nublado
Temperatura: 28°C
Chuva: 2 mm (30%)

Relatório de Vendas:
banana maçã — 10 kg | Fat.: R$120.00 | Lucro: R$70.00
mamão — 5 kg | Fat.: R$50.00 | Lucro: R$15.00
...
Total Faturamento: R$350.00
Total Lucro: R$120.00
Planilha Excel gerada pelo Programa 2:
Aba Dados: preços de compra e venda por produto.

Aba Vendas: registros semanais.

Aba Gráfico: gráficos de faturamento e lucro por semana.
```
