from django.shortcuts import render, get_object_or_404
from .models import Segment,Trotinet

from KorpaZaKupovinu.forms import FormaZaDodavanjeTrotinetaUKorpu
from KorpaZaKupovinu.korpa import Korpa

def ListaTrotineta(request, segment_slug = None):
    segment = None
    segmenti = Segment.objects.all()
    trotineti = Trotinet.objects.filter(raspoloziv=True)
    if segment_slug:
        segment = get_object_or_404(Segment, slug=segment_slug)
        trotineti = trotineti.filter(segment=segment)
    korpa = Korpa(request)
    return render(request, 'ProdavnicaTrotineta/Trotinet/list.html', {'segment': segment, 'segmenti': segmenti, 'trotineti': trotineti, 'korpa':korpa})

def DetaljiTrotineta(request, id, slug):
    trotinet = get_object_or_404(Trotinet, id=id, slug = slug, raspoloziv = True)

    korpa = Korpa(request)
    formazadodavanjetrotinetaukorpu = FormaZaDodavanjeTrotinetaUKorpu()

    return render(request, 'ProdavnicaTrotineta/Trotinet/detail.html', {'trotinet': trotinet, 'formazadodavanjetrotinetaukorpu': formazadodavanjetrotinetaukorpu, 'korpa': korpa})


