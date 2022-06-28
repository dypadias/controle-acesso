from dataclasses import field, fields
from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf",
            "setor", "placa_veiculo", "cargo_visitante", "empresa_visitante"   
        ] 
class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)
    
    class Meta:
        model = Visitante
        fields=[
            "morador_responsavel"
        ]
        error_messages = {
            "morador_responsavel":{
                "required": "Por favor informe o responsável pela entrada do visitante."
            }
        }