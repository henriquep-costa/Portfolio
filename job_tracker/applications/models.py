# Importa o módulo base de models do Django.
# É ele que permite criar tabelas através de classes Python.
from django.db import models

# Importa o modelo padrão de usuário do Django.
# Assim não precisamos criar nossa própria tabela de usuários.
from django.contrib.auth.models import User


# ================================
# TABELA: Company
# ================================

# Toda classe que herda de models.Model vira uma tabela no banco
class Company(models.Model):

    # Campo de texto com limite máximo de 255 caracteres.
    # No banco PostgreSQL isso vira VARCHAR(255).
    name = models.CharField(max_length=255)

    # Campo específico para URLs.
    # blank=True -> permite deixar vazio em formulários.
    # null=True  -> permite salvar como NULL no banco.
    website = models.URLField(blank=True, null=True)

    # Define como o objeto será exibido no Django Admin e em prints.
    # Boa prática sempre implementar.
    def __str__(self):
        return self.name


# ================================
# TABELA: Application
# ================================

class Application(models.Model):

    # Lista de opções permitidas para o campo "status".
    # Isso cria um campo controlado (tipo um ENUM).
    # O primeiro valor é o que será salvo no banco.
    # O segundo é o que aparece para o usuário.
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('INTERVIEW', 'Interview'),
        ('REJECTED', 'Rejected'),
        ('OFFER', 'Offer'),
    ]

    # ForeignKey cria relacionamento com outra tabela.
    # Aqui estamos dizendo:
    # Um usuário pode ter várias aplicações.
    # on_delete=models.CASCADE significa:
    # Se o usuário for deletado, todas as aplicações dele também serão.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Relacionamento com a tabela Company.
    # Uma empresa pode ter várias aplicações.
    # Se a empresa for deletada, as aplicações relacionadas também serão.
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # Nome da vaga.
    # Campo de texto limitado a 255 caracteres.
    position = models.CharField(max_length=255)

    # Campo de texto com opções limitadas ao STATUS_CHOICES.
    # max_length=20 porque o maior valor ('INTERVIEW') tem menos que isso.
    # default='APPLIED' significa que toda nova aplicação começa como APPLIED.
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='APPLIED'
    )

    # Campo de data e hora.
    # auto_now_add=True faz o Django salvar automaticamente
    # a data/hora no momento da criação do registro.
    applied_at = models.DateTimeField(auto_now_add=True)

    notes = models.CharField(max_length=500, blank=True, null=True)

    # Define como o objeto será exibido no Admin.
    def __str__(self):
        return f"{self.position} - {self.company.name}"