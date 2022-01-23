from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ProdavnicaTrotineta.models import Trotinet
from .korpa import Korpa
from .forms import FormaZaDodavanjeTrotinetaUKorpu

@require_POST
def DodajUKorpu(request, trotinet_id):
    korpa = Korpa(request)
    trotinet = get_object_or_404(Trotinet, id=trotinet_id)
    form = FormaZaDodavanjeTrotinetaUKorpu(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        korpa.Dodaj(trotinet=trotinet, kolicina=cd['kolicina'], dodati_na_kolicinu=cd['dodati_na_kolicinu'])

    return redirect('KorpaZaKupovinu:DetaljiKorpe')

@require_POST
def UkloniIzKorpe(request, trotinet_id):
    korpa = Korpa(request)
    trotinet = get_object_or_404(Trotinet, id=trotinet_id)
    korpa.Ukloni(trotinet)
    return redirect('KorpaZaKupovinu:DetaljiKorpe')


def DetaljiKorpe(request):
    korpa = Korpa(request)
    for stavka in korpa:
        stavka['formazaazuriranjekolicine'] = FormaZaDodavanjeTrotinetaUKorpu(initial={'kolicina': 1, 'dodati_na_kolicinu': True})
    return render(request, 'KorpaZaKupovinu/detail.html', {'korpa': korpa})









