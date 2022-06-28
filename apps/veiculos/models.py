from tabnanny import verbose
from django.db import models
from django.utils import timezone
from datetime import timedelta


class Veiculo(models.Model):

    STATUS_VEICULO = [
        ("NA_RUA", "Veículo fora da empresa"),
        ("NA_EMPRESA", "Veículo na empresa"),
    ]

    status = models.CharField(
        verbose_name="Status",
        max_length=10,
        choices=STATUS_VEICULO,
        default="NA_RUA",
    )

    nome_motorista = models.CharField(
        verbose_name="Nome motorista",
        max_length=194
    )
    
    CARROS=[
        ("GOL","Gol"),
        ("SAVEIRO", "Saveiro")
    ]
    
    veiculo = models.CharField(
        verbose_name="Carro",
        max_length=50,
        choices= CARROS,
        default="SAVEIRO")

    destino = models.CharField(
        verbose_name="Destino da saida",
        max_length=50
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do veículo",
        max_length=7,
        null=True,
        blank=True,
    )
    
    horario_saida = models.DateTimeField(
        verbose_name="Horário de saida",
        auto_now=False,
        blank=True,
        null=True,
    )
    
    

    horario_retorno = models.DateTimeField(
        verbose_name="Horário de retorno a empresa",
        auto_now=False,
        blank=True,
        null=True,
    )
    
    

  
    responsavel = models.CharField(
        verbose_name="Responsável pela saida do veiculo",
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
    
    def get_horario_chegada(self):
        if self.horario_retorno:
            return self.horario_retorno
        return "Horário de chegada não registrado"


    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        return "Placa não cadastrada"

    class Meta:
        verbose_name = "Veiculo"
        verbose_name_plural = "Veiculos"
        db_table = "veiculo"


    def __str__(self):
        return self.veiculo



