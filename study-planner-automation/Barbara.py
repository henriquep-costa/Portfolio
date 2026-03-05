#listas materias TJSP, dividir em 3 horas de estudo, 2 materias por dia + resoluçao de questoes

materias = ['Português', 'Matemática', 'Raciocínio lógico', 'Atualidades', 'Informática', 'Direito Constitucional', 'Direito Administrativo', 'Direito processual Civil', 'Direito Penal', 'Direito Processual Penal', 'Normas da Corregedoria']

horas_por_dia = 3
materias_por_dia = 2
questoes_por_materia = 20
horas_por_materia = horas_por_dia / materias_por_dia

#Dividir as materias por dia

dias = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
cronograma = {}

for i in range(0, len(materias), 2):
    dia = dias[i // 2]
    materia1 = materias[i]

    if i + 1 < len(materias):
        materia2 = materias[i + 1]
        cronograma[dia] = [materia1, materia2]
    else:
        cronograma[dia] = [materia1]

print(cronograma)

html = """
<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cronograma TJSP</title>
</head>
<body>
<h1>Cronograma TJSP</h1>
"""

for dia, materias_do_dia in cronograma.items():
    html += f"<h2>{dia.capitalize()}</h2>\n"
    html += "<ul>\n"

    for materia in materias_do_dia:
        html += f"<li>{materia} – {horas_por_materia}h – {questoes_por_materia} questões</li>\n"

    html += "</ul>\n"

html += """
</body>
</html>
"""

with open("cronograma.html", "w", encoding="utf-8") as f:
    f.write(html)