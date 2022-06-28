from dataclasses import field, fields
from django import forms
from veiculos.models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = [
            "nome_motorista","destino",
            "veiculo", "placa_veiculo",
        ]

class AutorizaVeiculoForm(forms.ModelForm):
    responsavel = forms.CharField(required=True)
    
    class Meta:
        model = Veiculo
        fields=[
            "responsavel"
        ]
        error_messages = {
            "responsavel":{
                "required": "Por favor informe o responsável pela saida do veículo."
            }
        }