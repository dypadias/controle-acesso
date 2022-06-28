from django.shortcuts import (
    render, redirect, get_object_or_404
)

from datetime import datetime

from django.contrib.auth.decorators import login_required
from veiculos.models import Veiculo

from veiculos.forms import (
    VeiculoForm, AutorizaVeiculoForm
    )

from django.http import HttpResponseNotAllowed

from django.contrib import messages

from django.utils import timezone


@login_required
def registrar_saida(request):

    form = VeiculoForm()

    if request.method == "POST":
        form = VeiculoForm(request.POST)

        if form.is_valid():
            veiculo = form.save(commit=False)

            veiculo.registrado_por = request.user.porteiro
            veiculo.status="NA_RUA"
            
            veiculo.horario_saida = timezone.now()
            veiculo.save()

            messages.success(
                request,
                "Saida de veiculo registrada com sucesso"
            )

            return redirect("saida_veiculos")

    context = {
        "nome_pagina": "Registrar saída",
        "form": form
    }

    return render(request, "registrar_saida.html", context)


@login_required
def saida_veiculos(request):

    todas_saidas = Veiculo.objects.order_by(
        "-horario_saida"
    )

    veiculos_fora = todas_saidas.filter(
        status="NA_RUA"
    )

    veiculos_empresa = todas_saidas.filter(
        status="NA_EMPRESA"
    )


    hora_atual = timezone.now()
    mes_atual = hora_atual.month

    saidas_mes = todas_saidas.filter(
        horario_retorno__month=mes_atual
    )

    context = {
        "nome_pagina": "Controle de veículos",
        "todas_saidas": todas_saidas,
        "veiculos_fora": veiculos_fora.count(),
        "veiculos_empresa": veiculos_empresa.count(),
        "saidas_mes": saidas_mes.count(),
    }

    return render(request, "saida_veiculos.html", context)

@login_required
def veiculo_retorno(request, id):
        
        if request.method == "POST":
            veiculo = get_object_or_404(
                Veiculo,
                id=id
            )

            veiculo.status = "NA_EMPRESA"
            veiculo.horario_retorno =  timezone.now()
            veiculo.save()
                
            messages.success(
                request,
                "Retorno do veículo registrado com sucesso"
            )    
            return redirect ("saida_veiculos")
        else:
            return HttpResponseNotAllowed(
                ["POST"],
                "Método não permitido"
            )


@login_required
def informacoes_saida(request,id):
    veiculo = get_object_or_404(
        Veiculo,
        id=id
    )

    form = AutorizaVeiculoForm()

    if request.method == "POST":
        form = AutorizaVeiculoForm(
            request.POST,
            instance=veiculo
        )

        if form.is_valid():
            veiculo = form.save(commit=False)

            veiculo.status = "NA_RUA"
            hora_atual = timezone.now()
            veiculo.horario_saida = hora_atual

            veiculo.save()

            messages.success(
                request,
                "Saida autorizada com sucesso."
            )

            return redirect("saida_veiculos")

    context = {
        "nome_pagina": "Informações de veiculos",
        "veiculo": veiculo,
        "form": form
    }
    return render(request, "informacoes_saida.html", context)
