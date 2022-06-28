from tabnanny import verbose
from django.db import models


class Visitante(models.Model):
    
    STATUS_VISITANTE = [
        ("AGUARDANDO","Aguardando autorização"),
        ("EM_VISITA","Em visita"),
        ("FINALIZADO", "Visita finalizada"),
    ]
    
    status = models.CharField(
        verbose_name="Status", 
        max_length=10,
        choices=STATUS_VISITANTE,
        default="AGUARDANDO",
    )
    
    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11
    )
    
    CARGO_VISITANTE = [
        ("MOTORISTA", "Motorista"),
        ("AJUDANTE", "Ajudante"),
        ("DIRETORIA", "Funcionario da Direção"),
        ("COMUM", "Funcionario comum"),
    ]
    
    cargo_visitante = models.CharField(
        verbose_name = "Cargo visitante",
        max_length=20,
        choices=CARGO_VISITANTE,
        default="COMUM"
    )
    
    empresa_visitante = models.CharField(
        verbose_name="Empresa",
        max_length=30,
        null=True,
        blank=True,
        )
    
    SETOR_VISITADO = [
        ("MANUTENCAO", "Manutenção"),
        ("RH", "Rh"),
        ("DIRETORIA", "Diretoria"),
        ("ALMOXARIFADO", "Almoxarifado"),
        ("ACABAMENTO", "Acabamento"),
        ("PRODUCAO", "Produção"),
        ("SESMT", "Segurança do Trabalho"),
    ]

    setor = models.CharField(
        verbose_name="Setor a ser visitada",
        choices=SETOR_VISITADO,
        default="ALMOXARIFADO",
        max_length=20
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do veículo",
        max_length=7,
        null=True,
        blank=True,
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada na portaria",
        auto_now_add=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saida",
        auto_now=False,
        blank=True,
        null=True,
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        auto_now=False,
        blank=True,
        null=True,
    )

    morador_responsavel = models.CharField(
        verbose_name="Responsável pela entrada do visitante",
        max_length=194,
        blank=True,
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT
    )
    
    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        return "Horário de saída não registrado"

    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        return "Aguardando autorização "

    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        return "Aguardando autorização"
    
    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        return "Placa não cadastrada"

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"
        
    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)
            
            cpf_parte_um = cpf[0:3]
            cpf_parte_dois = cpf[3:6]
            cpf_parte_tres = cpf[6:9]
            cpf_parte_quatro = cpf[9:]

            cpf_formatado = f"{cpf_parte_um}.{cpf_parte_dois }.{ cpf_parte_tres}-{cpf_parte_quatro}"

            return cpf_formatado
        
    def __str__(self):
        return self.nome_completo
